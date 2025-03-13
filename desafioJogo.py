from os import system as limpar
from time import sleep as esperar
import pygame

done = False

limpar("cls")
print("*" * 30)
print("BEM-VINDO AO SISTEMA DE FORMAS")
print("*" * 30)

forma = input("Por favor, digite a forma que deseja desenhar: ")

if forma=='circulo':
    print("Você selecionou círculo!")
elif forma=='quadrado':
    print("Você selecionou quadrado!")

tamanho_X = int(input("Digite o tamanho \"X\" da forma: "))
tamanho_Y = int(input("Digite o tamanho \"Y\" da forma: "))
limpar("cls")

limpar("cls")
print("PROCESSANDO", end="")
for cont in range(6):
    print(end=".")
    esperar(1)

pygame.init()
screen = pygame.display.set_mode((900, 900))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if forma=='quadrado':
        pygame.draw.rect(screen, (160, 160, 160), pygame.Rect(300, 300, tamanho_X, tamanho_Y))
    if forma=='circulo':
        raio = (tamanho_X, tamanho_Y) / 2
        pygame.draw.circle(screen, (160, 160, 160), (450, 300), raio)
    pygame.display.flip()

limpar("cls")
print("OBRIGADO POR USAR O SISTEMA! :)")
