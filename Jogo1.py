import pygame

pygame.init()
screen = pygame.display.set_mode((900, 800))
done = False
is_blue = True
x = 30
y = 30

#cria o gerenciamento de taxa de quadros
clock = pygame.time.Clock()

# 1. Cria uma surpefície do mesmo tamanho da tela
white_surface = pygame.Surface((400, 300)) # As mesmas dimensões da tela

#2. Preenche a superficie com branco
white_surface.fill((255, 255, 255))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    
    #rescreve a tela toda em preto
    screen.fill((0, 0, 0))
    
    #3. Desenha a superfície branca sobre a tela
    screen.blit(white_surface, (100, 100)) #Desenha no canto superior esquerdo (0,0)

    if is_blue: color = (0, 128, 255)
    else: color = (225, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    #Atualiza a tela com as alterações feitas
    pygame.display.flip()

    surface = pygame.Surface((100, 100))
    clock.tick(60)