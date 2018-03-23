from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from time import sleep

bot = ChatBot('DazOS Bot')
bot.set_trainer(ListTrainer)

while True:
    mensagem = input('Você: ')
    if mensagem.strip() != 'tchau':
        resposta = bot.get_response(mensagem)
        print('\nDazOS Bot está digitando...\n')
        sleep(1)
        print('DazOS Bot: ', resposta, '\n')
    if mensagem.strip() == 'tchau':
        print('\nDazOS Bot está digitando...\n')
        sleep(1)
        print('DazOS Bot: Tchau! :)')
        break
