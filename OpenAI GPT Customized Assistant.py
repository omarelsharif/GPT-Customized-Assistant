
# Omar El-Sharif
# Feel free to tweak this code - going through the API documentation is a hassle but worth it! 

import openai
import gradio

openai.api_key = "Hey! Put your OpenAI API key here to run my code"

messages = [{"role": "system", "content": "You are an Electrical Engineering expert that specializes in embedded systems and electric vehicles"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Electrical Engineering Pro")

demo.launch(share=True)
