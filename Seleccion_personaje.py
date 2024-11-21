import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menú de Selección de Personaje")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Fuente
font = pygame.font.Font(None, 50)

# Cargar imágenes de los personajes
imagen_nino = pygame.image.load("imagen/nino.png")
imagen_nino = pygame.transform.scale(imagen_nino, (150, 200))  # Ajustar tamaño si es necesario

imagen_nina = pygame.image.load("imagen/nina.png")
imagen_nina = pygame.transform.scale(imagen_nina, (150, 200))  # Ajustar tamaño si es necesario

# Índice del personaje seleccionado
selected_index = 0  # 0 para "Niño", 1 para "Niña"

def draw_menu():
    screen.fill(BLACK)
    
    # Dibujar título
    title = font.render("Selecciona un Personaje", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
    
    # Dibujar al niño a la izquierda
    color_nino = YELLOW if selected_index == 0 else WHITE
    border_rect_nino = pygame.Rect(WIDTH // 4 - 75, HEIGHT // 2 - 100, 150, 200)
    pygame.draw.rect(screen, color_nino, border_rect_nino, 5)  # Borde alrededor del personaje
    screen.blit(imagen_nino, (WIDTH // 4 - imagen_nino.get_width() // 2, HEIGHT // 2 - imagen_nino.get_height() // 2))
    
    # Dibujar a la niña a la derecha
    color_nina = YELLOW if selected_index == 1 else WHITE
    border_rect_nina = pygame.Rect(3 * WIDTH // 4 - 75, HEIGHT // 2 - 100, 150, 200)
    pygame.draw.rect(screen, color_nina, border_rect_nina, 5)  # Borde alrededor del personaje
    screen.blit(imagen_nina, (3 * WIDTH // 4 - imagen_nina.get_width() // 2, HEIGHT // 2 - imagen_nina.get_height() // 2))

def main():
    global selected_index
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Cambiar selección con flecha izquierda
                    selected_index = 0  # Seleccionar "Niño"
                elif event.key == pygame.K_RIGHT:  # Cambiar selección con flecha derecha
                    selected_index = 1  # Seleccionar "Niña"
                elif event.key == pygame.K_RETURN:  # Confirmar selección con Enter
                    print(f"Has seleccionado: {'Niño' if selected_index == 0 else 'Niña'}")
                    # Aquí podrías pasar a la siguiente pantalla o cargar el personaje

        draw_menu()
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
