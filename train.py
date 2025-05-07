from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('MyBot')
trainer = ListTrainer(chatbot)

with open('movie_dialogs.txt', 'r', encoding='utf-8') as file:
    lines = file.read().split('\n\n')
    for pair in lines:
        messages = pair.strip().split('\n')
        if len(messages) == 2:
            trainer.train(messages)
