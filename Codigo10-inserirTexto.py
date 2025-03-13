import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False

fonte = pygame.font.SysFont("comicsansms", 72)

texto = fonte.render("SENAI NA VEIA", True, (0, 128, 0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    
    screen.fill((255, 255, 255))
    
    # O comando abaixo escreve o texto na tela, calculando sua largura e sua 
    # altura para centralizar o texto
    # texto.get_width() // 2 -> pega a largura da tela e divide por 2
    # depois faz 320 menos esse valor para saber onde começar o texto
    screen.blit(texto,
                (320 - texto.get_width() // 2, 240 - texto.get_height() // 2))
    
    pygame.display.flip()
    clock.tick(60)