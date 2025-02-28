import calculos as calc
from time import sleep as esperar

print("*" * 20)
print("CALCULO ÁREA")
print("*" * 20)

formas = {"1": "Quadrado",
          "2": "Circulo",
          "3": "Triângulo Retângulo",
          "4": "Retângulo"}

while(True):
    print("Formas")
    print("1 -", formas["1"])
    print("2 -", formas["2"])
    print("3 -", formas["3"])
    print("4 -", formas["4"])

    forma = input("Digite o número da forma que deseja calcular: ")
    if forma == '2':#Calculo da área do circulo
        print("VOCÊ SELECIONOU \"CÍRCULO\"")
        raio = float(input("Digite o raio da área: "))
        input(f"A área do círculo com raio de {raio} é de: {calc.circulo(raio):.2f}m²")
        break
    elif forma == '1':#Calculo da área do quadrado
        print("VOCÊ SELECIONOU \"QUADRADO\"")#Cálculo da área do quadrado
        lado = float(input("Digite o valor do lado do quadrado: "))
        input(f"O valor da área do quadrado com lado {lado} é de: {calc.quadrado(lado):.2f}m²")
        break
    elif forma == '4':#Calculo da área do retângulo
        print("VOCÊ SELECIONOU A FORMA \"RETÂNGULO\"")
        base = float(input("Digite o valor da base: "))
        altura = float(input("Digite o valor da altura: "))
        print(f"A área do Retângulo com {base}cm e {altura}cm é de: {calc.retangulo(base, altura)}")
        break
    elif forma == '3':#Calculo da área do triangulo
        print("VOCÊ SELECIONOU A FORMA \"TRIÂNGULO RETÂNGULO\"")
        base = float(input("Digite o valor da base: "))
        altura = float(input("Digite o valor da altura: "))
        print(f"O valor da área do triângulo com {base}cm e {altura}cm é de: {calc.triangulo(base, altura)}m²")
    else:
        print("Esse número não está na biblioteca\nDigite a forma existente")
        esperar(2)