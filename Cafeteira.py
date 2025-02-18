from os import system
from time import sleep
system ("cls")


print("\033[31m*****Cafés Senai*****")
print("Selecione uma bebida\n"
    "\n"
    "1- Expresso\n"
    "2- Torrado\n"
    "3- Extra Torrado\n"
    "4 - Chá verde\n"
    "5- Café com leite")
print("**" * 10, "\033[m")
beb = int(input("Coloque o número de sua bebida:"))

if beb == 1:#Se a bebida for a primeira, deixará uma mensagem
        print("Você selecionou a bebida \"Expresso\"")
if beb == 2:#Se a bebida for a segunda, deixará uma mensagem
        print("Você selecionou a bebida \"Torrado\"")
if beb == 3:#Se a bebida for a terceira, deixará uma mensagem
        print("Você escolheu a bebida \"Extra Torrado\"")
if beb == 4:#Se a bebida for a quarta, deixará uma mensagem
        print("Você esolheu a bebida \"Chá verde\"")
if beb == 5:#Se a bebida for a quinta, deixará uma mensagem
    print("Você  escolheu a bebida \"Café com leite\"")

confirm = str(input("Confirme com S ou N se essa é a bebida que deseja: "))
if confirm == 's' or confirm == 'S':#Função se a confirmação for 'sim'
    print("PREPARANDO.")
    sleep(1)
    print("PREPARANDO..")
    sleep(1)
    print("PREPARANDO...")
    sleep(1)
    print("PREPARANDO.....")
    sleep(1)
    print("\033[32mSua bebida está pronta, aproveite e volte sempre!!\033[m")
    
if confirm == 'n' or confirm == 'N':
    print("Perdão, volte a programação e peça sua bebida novamente!!")