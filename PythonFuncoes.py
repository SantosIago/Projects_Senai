import os
os.system("cls")

def sel0():
    print("0" * 30)
    print("Você selecionou a opção 0!!!")
    print("0" * 30)

def sel1():
    print("1" * 30)
    print("Você selecionou a opção 1!!!")
    print("1" * 30)

def sel2():
    print("2" * 30)
    print("Você selecionou a opção 2!!!")
    print("2" * 30)

def sel3():
    print("3" * 30)
    print("Você selecionou a opção 2!!!")
    print("3" * 30)

while(True):
    opcao = int(input("Digite um número de 0 a 3: "))
    if opcao == 0:
        sel0()
    elif opcao == 1:
        sel1()
    elif opcao == 2:
        sel2()
    elif opcao ==3:
        sel3()
