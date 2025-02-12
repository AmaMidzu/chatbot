import chainlit as cl
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.document_loaders import PyPDFLoader


EMBEDDING_MODEL = "nomic-embed-text"
PDF_EMB_VECTOR_STORE = "pdf-embeddings"


def extract_pdf_content(pdf_file_path):
    loader = PyPDFLoader(pdf_file_path)
    pdf_pages = loader.load_and_split()
    pdf_content = " ".join([page.page_content for page in pdf_pages])
    return pdf_content


def split_text_into_chunks(text, chunk_size=1000, chunk_overlap=100):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    text_chunks = text_splitter.split_text(text)
    return text_chunks


def create_pdf_vector_db(text_chunks, embedding_model, collection_name):
    pdf_vector_db = Chroma.from_texts(
        texts=text_chunks,
        embedding=OllamaEmbeddings(model=embedding_model),
        collection_name=collection_name
    )
    return pdf_vector_db


@cl.on_chat_start
async def on_chat_start():
    pdf_files = None

    while pdf_files is None:
        pdf_files = await cl.AskFileMessage(
        content="Upload a PDF",
        accept=["application/pdf"],
     ).send()

    pdf_file = pdf_files[0]

    msg = cl.Message(content=f"Processing {pdf_file.name}")
    await msg.send()


    pdf_content = extract_pdf_content(pdf_file.path)
    text_chunks = split_text_into_chunks(pdf_content)
    pdf_vector_db = create_pdf_vector_db(text_chunks, EMBEDDING_MODEL, PDF_EMB_VECTOR_STORE)

    message_history = ChatMessageHistory()
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        chat_memory=message_history,
        return_messages=True
        )

    chain = ConversationalRetrievalChain.from_llm(
        ChatOllama(model="llama3.1", temperature=0),
        chain_type="stuff",
        retriever=pdf_vector_db.as_retriever(),
        memory=memory
        )

    msg.content = f"{pdf_file.name} processed. You can now ask questions."
    await msg.update()

    cl.user_session.set("chain", chain)


@cl.on_message
async def on_message(message: cl.Message) -> None:
    chain = cl.user_session.get("chain")

    langchain_callback = cl.AsyncLangchainCallbackHandler()
    response = await chain.ainvoke(message.content, callbacks=[langchain_callback])
    content = response["answer"]

    await cl.Message(content=content).send()

