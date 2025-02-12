import chainlit as cl
from litellm import completion
from chainlit.input_widget import Select, Slider


@cl.on_chat_start
async def on_chat_start():
    """
    Let the user choose between various model options.

    Returns:
        None
    """
    # Set default settings
    default_settings = {
        "Model": "llama2",
        "Streaming": True,
        "Temperature": 1
    }
    cl.user_session.set("settings", default_settings)

    settings = await cl.ChatSettings(
        [
            Select(
                id="Model",
                label="Choose between Llama2 and Llama3",
                values=["llama2", "llama3"],
                initial_index=0,
            ),
            Slider(
                id="Temperature",
                label="Llama - Temperature",
                initial=1,
                min=0,
                max=1,
                step=0.1,
            ),
        ]
    ).send()


@cl.on_settings_update
async def on_settings_update(settings):
    """ Update the user session with the new settings """
    cl.user_session.set("settings", settings)


@cl.on_message
async def on_message(message: cl.Message) -> None:
    """
    Receive a message from the user, send it to the LLM, and send a generated reply
    message back to the user.

    Args:
        message (cl.Message): The message from the user

    Returns:
        None
    """

    settings = cl.user_session.get("settings")

    msg = cl.Message(content="")
    await msg.send()

    response = completion(
        model=f"ollama_chat/{settings['Model']}",
        temperature=settings["Temperature"],
        messages=[{"content": message.content, "role": "user"}],
        stream=True,
    )

    for chunk in response:
        token = chunk.choices[0].delta.content
        if token:
            await msg.stream_token(token)

    await msg.update()



