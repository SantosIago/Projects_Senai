from os import system as limpar
limpar("cls")

valor = 500

def soma(x, y):
    res = x + y
    return res

valor2 = int(input("Digite um valor: "))
resultado = soma(valor, valor2)
print("O resultado é ", resultado)