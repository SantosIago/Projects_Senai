import pygame

pygame.init()
pygame.mixer.init()  # Inicializa o mixer para tocar músicas

# Define o nome do arquivo MP3
nome_musica = "musica.mp3"  # Substitua pelo nome do seu arquivo

try:
    # Carrega a música
    pygame.mixer.music.load(nome_musica)

    # Toca a música em loop (-1 significa loop infinito)
    pygame.mixer.music.play(-1)

    # Mantém o programa rodando para que a música continue tocando
    print("Tocando a música. Pressione Ctrl+C para parar.")
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Mantém o loop rodando sem consumir muita CPU

except pygame.error as e:
    print(f"Erro ao carregar ou reproduzir a música: {e}")

pygame.quit()