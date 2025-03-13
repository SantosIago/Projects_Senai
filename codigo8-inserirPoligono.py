import pygame
import math

pygame.init()

# Configuração da tela
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
    "ativo": False, # Desativado para focar na estrela
    "cor": vermelho,
    "x": 50,
    "y": 50,
    "largura": 100,
    "altura": 50
}

circulo = {
    "ativo": False, # Desativado para focar na estrela
    "cor": vermelho,
    "x": 200,
    "y": 150,
    "raio": 40
}

linha = {
    "ativo": False, # Desativado para focar na estrela
    "cor": azul,
    "inicio_x": 350,
    "inicio_y": 200,
    "fim_x": 450,
    "fim_y": 250,
    "espressura": 5
}

# Definição da estrela
poligono = {
    "ativo": True,
    "cor": amarelo,
    "pontos": [] # Os pontos são gerados abaixo
}

# Gerar os pontos da estrela
num_pontas = 20 # Número de pontas da estrela
raio_externo = 100 # Raios dos pontos externos
raio_interno = 50 # Raio dos pontos internos
centro_x = largura // 2 #centro da tela
centro_y = altura // 2

for i in range(num_pontas * 2):
    angulo = math.pi / num_pontas * i - math.pi / 2 # Ajuste para a ponta estar para cima
    raio = raio_externo if i % 2 == 0 else raio_interno
    x = centro_x + int(raio * math.cos(angulo))
    y = centro_y + int(raio * math.sin(angulo))
    poligono["pontos"].append((x, y))

# Loop principal
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    # Limpa a teça
    tela.fill(preto) # Fundo branco

    # Desenha as Figuras (baseado nas definições)
    if retangulo["ativo"]:
        pygame.draw.rect(tela, retangulo["cor"], pygame.Rect(retangulo["x"], retangulo["y"], retangulo["largura"], retangulo["largura"]))

    if linha["ativo"]:
        pygame.draw.line(tela, linha["cor"], (linha["inicio_x"], linha["inicio_y"]), 
                         (linha["fim_x"], linha["fim_y"]), linha["espressura"])
        
    if circulo["ativo"]:
        pygame.draw.circle(tela, circulo["cor"], (circulo["x"], circulo["y"]), 
                           circulo["raio"])
        
    if poligono["ativo"]:
        pygame.draw.polygon(tela, poligono["cor"], poligono["pontos"])

    # Atualiza a tela com as alterações feitas
    pygame.display.flip()

pygame.quit()