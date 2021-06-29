import pyttsx3
from os import system, name
import glob


def limpar_terminal():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def menuproj06():
    print('''Bem Vindo!
    Ao Bootcamp de Projeto Python da DevAprender - Conversor de texto para áudio.
    Escolha um arquivo para leitura.
    É necessário digitar o nome completo do arquivo, apresentado na lista.
    Digite Sair para terminar o código.''')
    print('')


limpar_terminal()
menuproj06()
som_pt = pyttsx3.init()
som_pt.say('''Bem Vindo!
    Ao Bootcamp de Projeto Python da DevAprender - Conversor de texto para áudio.
    Escolha um arquivo para leitura.
    É necessário digitar o nome completo do arquivo, apresentado na lista.
    Digite Sair para terminar o código.''')
som_pt.runAndWait()
input('Pressione "ENTER" para continuar.')

lista_arquivo = [f for f in glob.glob("*.txt")]
while True:
    limpar_terminal()
    menuproj06()
    print(lista_arquivo)
    arquivo_selecao = input('Qual arquivo quer ouvir da lista? ').lower()
    if arquivo_selecao == 'sair':
        limpar_terminal()
        exit()
    else:
        try:
            with open((arquivo_selecao), 'r') as arquivo:
                texto = arquivo.read()
                print(texto)
                som_pt.say(texto)
                som_pt.runAndWait()
                limpar_terminal()
                menuproj06()
        except FileNotFoundError:
            print(
                'Digitar um arquivo da lista apresentada ou sair para finalizar o código.')
            input('"ENTER" para continuar.')
