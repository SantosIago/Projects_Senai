from os import system
import random 
system("cls")

aleatorio = random.randint(0, 10)
erros = 0

val = int(input("De 0 a 10, adivinhe qual número estou pensando: "))

while (val != aleatorio):
    print("\033[31mVocê errou o número!\033[m")
    val = int(input("Digite o número novamente: "))
    erros += 1
print("\033[32mPARABÉNS, VOCÊ ACERTOU!!")
print("\033[31mVocê teve", erros, "erros!\033[m")