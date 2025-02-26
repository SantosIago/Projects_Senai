from os import system
from time import sleep
system("cls")

#PROJETO CALCULADORA


print("=" * 20)
print("CALCULADORA SENAI")
print("=" * 20)

while (True):
    veri_opera = 1
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    while(veri_opera == 1):
        opera = str(input("Digite o operador a ser feito o cálculo: "))
        system("cls")

        def soma(x, y):
            res = x + y
            return res

        def sub(x, y):
            res = x - y
            return res

        def mult(x, y):
            res = x * y
            return res

        def divi(x, y):
            res = x / y
            return res

        if opera == '+':
            print("A soma dos valores é de:", soma(valor1, valor2))
            veri_opera = 0
        elif opera == '-':
            print("A subtração dos valores é de:", sub(valor1, valor2))
            veri_opera = 0
        elif opera == '*':
            print("A multiplicação desses valores é de:", mult(valor1, valor2))
            veri_opera = 0
        elif opera == '/':
            print("A divisão desses valores é de:", divi(valor1, valor2))
            veri_opera = 0
        else:
            print("Esse operador não existe!\n"
                "Por favor, digite operadores existentes.")
