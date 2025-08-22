import os
import dotenv
from flask import Flask, render_template, request
from openai import AzureOpenAI
import httpcore

dotenv.load_dotenv()

app = Flask(__name__)

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

system_prompt = {
        "role": "system",
	"content": "You are the best chatbot in the world!"
}

conversation = [
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    global conversation
    conversation.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=conversation
        )
    except:
        print("RemoteProtocolError")
        conversation = []
        conversation.append(system_prompt)
        reply = "Blocked by Prisma AIRS"
    else:
        reply = response.choices[0].message.content


    conversation.append({"role": "assistant", "content": reply})

    return reply

if __name__ == '__main__':
    conversation.append(sytem_prompt)
    app.run(debug=True)
