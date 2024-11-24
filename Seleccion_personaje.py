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

# Lista de personajes
characters = ["Niño", "Niña"]
selected_index = 0  # Índice del personaje seleccionado

def draw_menu():
    screen.fill(BLACK)
    title = font.render("Selecciona un Personaje", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
    
    # Dibujar cada personaje en el menú
    for i, character in enumerate(characters):
        color = YELLOW if i == selected_index else WHITE
        text = font.render(character, True, color)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 200 + i * 100))

def main():
    global selected_index
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    selected_index = (selected_index + 1) % 2  # Cambiar entre 0 y 1
                elif event.key == pygame.K_RETURN:  # Confirmar selección con Enter
                    print(f"Has seleccionado: {characters[selected_index]}")
                    # Aquí podrías pasar a la siguiente pantalla o cargar el personaje

        draw_menu()
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
