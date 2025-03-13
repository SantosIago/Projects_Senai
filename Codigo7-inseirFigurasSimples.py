import pygame
import math

pygame.init()

# Configurações da Tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Controle de Figuras Geométricas")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)

# Definições das Figuras (EDITE AQUI!)
retangulo = {
    "ativo": True,  # True para mostrar, False para esconder
    "cor": vermelho,
    "x": 50,
    "y": 50,
    "largura": 100,
    "altura": 50
}

circulo = {
    "ativo": True,
    "cor": verde,
    "x": 200,
    "y": 150,
    "raio": 40
}

linha = {
    "ativo": True,
    "cor": azul,
    "inicio_x": 350,
    "inicio_y": 200,
    "fim_x": 450,
    "fim_y": 250,
    "espessura": 5
}

poligono = {
    "ativo": True,
    "cor": amarelo,
    "pontos": [(500, 10), (600, 150), (700, 100), (650, 50), (550, 50)]  # Lista de tuplas (x, y)
}


# Loop Principal
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Limpa a tela
    tela.fill(preto)  # Fundo branco

    # Desenha as Figuras (baseado nas definições)
    if retangulo["ativo"]:
        pygame.draw.rect(tela, retangulo["cor"],
                         pygame.Rect(retangulo["x"], retangulo["y"], retangulo["largura"], retangulo["altura"]))

    if circulo["ativo"]:
        pygame.draw.circle(tela, circulo["cor"], (circulo["x"], circulo["y"]), circulo["raio"])

    if linha["ativo"]:
        pygame.draw.line(tela, linha["cor"], (linha["inicio_x"], linha["inicio_y"]),
                         (linha["fim_x"], linha["fim_y"]), linha["espessura"])

    if poligono["ativo"]:
        pygame.draw.polygon(tela, poligono["cor"], poligono["pontos"])

    #Atualiza a tela com as alterações feitas
    pygame.display.flip()

pygame.quit()