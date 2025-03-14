import pygame
from time import sleep

#Iniciando o jogo
pygame.init()

#Criando a tela com pixels 800x600
screen = pygame.display.set_mode((800, 600))

#Criando o plano de fundo
background = pygame.image.load("FundoFloresta.jpg")

#Nome da janela e Icone
pygame.display.set_caption("Iago - Game")
icon = pygame.image.load("Icon.png")
pygame.display.set_icon(icon)

#Player
player_image = pygame.image.load("Player.png")
PlayerX = 350
PlayerY = 435

#Movimentos dos player
def player(x, y):
    screen.blit(player_image, (x, y))


tela = False
#Loop do jogo
while not tela:
    screen.fill((160, 160, 160))
    #Mostrando o plano de fundo
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tela = True

    #Evento do movimento do personagem
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            PlayerX += 2
        if event.key == pygame.K_LEFT:
            PlayerX -= 2
    
    #Colocando limite da tela
    if PlayerX >= 750:
        PlayerX = -50
    elif PlayerX <= -50:
        PlayerX = 750
    
    player(PlayerX, PlayerY)
    #Atualiza com as alterações feitas
    pygame.display.update()