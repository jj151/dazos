from os import listdir
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot = ChatBot('DazOS Bot')
bot.set_trainer(ListTrainer)

for files in listdir('/home/daniel/projetos/python3/dazos/chatterbot_corpus/data/portuguese/'):
    data = open('/home/daniel/projetos/python3/dazos/chatterbot_corpus/data/portuguese/' + files, 'r').readlines()
    bot.train(data)

while True:
    mensagem = input('Você: ')
    if mensagem.strip() != 'tchau':
        resposta = bot.get_response(mensagem)
        print('DazOS Bot: ', resposta)
    if mensagem.strip() == 'tchau':
        print('DazOS Bot: Tchau! :)')
        break
