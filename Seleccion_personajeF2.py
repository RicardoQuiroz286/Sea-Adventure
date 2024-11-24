import pygame
import sys
from NiñaFNivel2 import *
from NiñoFNivel2 import *


# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menú de Selección de Personaje")

# Cargar imágenes
imagen_nino = pygame.image.load("imagen/personajes/nadar1.gif")
imagen_nino = pygame.transform.scale(imagen_nino, (200, 150))
imagen_nina = pygame.image.load("imagen/personajes/bu1.png")
imagen_nina = pygame.transform.scale(imagen_nina, (200, 150))
imagen_fondo = pygame.image.load("imagen/fondo/foceano.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, (WIDTH, HEIGHT))
imagen_titulo = pygame.image.load("imagen/seleccion.png")
imagen_titulo = pygame.transform.scale(imagen_titulo, (800, 120))  # Ajustar tamaño del título

# Función principal de selección
def seleccionN2F():
    # Posiciones de los personajes
    rect_nino = imagen_nino.get_rect(center=(WIDTH // 4, HEIGHT // 2))
    rect_nina = imagen_nina.get_rect(center=(3 * WIDTH // 4, HEIGHT // 2))

    # Bucle principal
    clock = pygame.time.Clock()
    while True:
        # Dibujar fondo
        screen.blit(imagen_fondo, (0, 0))

        # Dibujar título
        title_rect = imagen_titulo.get_rect(center=(WIDTH // 2, 100))
        screen.blit(imagen_titulo, title_rect.topleft)

        # Dibujar personajes
        screen.blit(imagen_nino, rect_nino.topleft)
        screen.blit(imagen_nina, rect_nina.topleft)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Detectar clic en los personajes
                if rect_nino.collidepoint(event.pos):
                    print("Has seleccionado: Niño")
                    ñoeasy2()  # Llamar al nivel de Niño
                    return
                if rect_nina.collidepoint(event.pos):
                    print("Has seleccionado: Niña")
                    ñaeasy2()  # Llamar al nivel de Niña
                    return

        # Actualizar pantalla
        pygame.display.update()
        clock.tick(30)
