
# Omar El-Sharif
# Feel free to tweak this code - going through the API documentation to understand and piece this code together is a hassle but worth it! 

import openai
import gradio

openai.api_key = "Hey! Put your OpenAI API key here to run my code"

messages = [{"role": "system", "content": "You are an Electrical Vehicle expert that specializes in electric vehicles. Continue asking the user prompting questions until you identify the perfect electric vehicle for them. Once you find it, reccomend it to them and make note of their location. End the conversation with mentioning a dealership near them that offers the car you reccomended, or a way to purchase the car online."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Electric Vehicle Pro")

demo.launch(share=True)
