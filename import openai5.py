import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a Car Expert"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Yusuf's Car Expert Chatbot")

demo.launch(share=True)
