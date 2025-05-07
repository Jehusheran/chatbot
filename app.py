from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

chatbot = ChatBot('MyBot')

trainer = ListTrainer(chatbot)

file_path = '/Users/wynjehu/Desktop/Zerthwynn/movie_dialogs.txt'  
if os.path.exists(file_path):
    print(f"Training with data from {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n\n')
        for pair in lines:
            messages = pair.strip().split('\n')
            if len(messages) == 2:
                print(f"Training pair: {messages}")
                trainer.train(messages)
else:
    print("Training with default data")
    
    training_data = [
        "Hi",
        "Hello",
        "How are you?",
        "I'm good, thank you!",
        "What is your name?",
        "My name is MyBot.",
        "Goodbye",
        "Bye, have a great day!",
        "Which is the best mobile?",
        "The best mobile depends on your needs, but popular choices include the iPhone and Samsung Galaxy.",
        "Suggest me one movie name",
        "I recommend watching 'Inception'.",
        "Baby",
        "Babies are adorable!"
    ]
    trainer.train(training_data)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.json.get("message")
    response = str(chatbot.get_response(user_text))
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))