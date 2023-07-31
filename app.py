import openai
import gradio
import os
from dotenv import load_dotenv


def CustomChatGPT(user_input):
    openai.api_key = os.getenv("API_KEY") # Add API_KEY in .env file
    messages = [{"role": "system", "content": "You are a kindergarten teacher who specializes in helping kids understand more easily"}]
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


def main():
    demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "My teacher, GPT")
    demo.launch(server_name="0.0.0.0", share=True)  

if __name__ == '__main__':
    # Load variables from .env file
    load_dotenv()
    main()