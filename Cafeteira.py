from os import system
from time import sleep


while(True):
    valida = 0
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
    elif beb == 2:#Se a bebida for a segunda, deixará uma mensagem
            print("Você selecionou a bebida \"Torrado\"")
    elif beb == 3:#Se a bebida for a terceira, deixará uma mensagem
            print("Você escolheu a bebida \"Extra Torrado\"")
    elif beb == 4:#Se a bebida for a quarta, deixará uma mensagem
            print("Você esolheu a bebida \"Chá verde\"")
    elif beb == 5:#Se a bebida for a quinta, deixará uma mensagem
        print("Você  escolheu a bebida \"Café com leite\"")
    elif beb == 666:
         print("Parando a máquina!")
         sleep(2)
         break
    else:
        print("Bebida inválida! por favor, selecione da biblioteca")
        valida = 1
        sleep(2)
    if valida == 0:
        confirm = str(input("Essa é a bebida que deseja? S/N "))
        if confirm == 's' or confirm == 'S':#Função se a confirmação for 'sim'
            system("cls")
            print("Preparando sua bebida", end="")
            for cont in range(6):
                print(end=".")
                sleep(1)
            print("\n\033[32mSua bebida está pronta, aproveite e volte sempre!!\033[m")
            
        elif confirm == 'n' or confirm == 'N':
            print("Perdão, pelo erro! Vamos iniciar novamente")
            sleep(3)
