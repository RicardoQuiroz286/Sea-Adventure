import pygame

# Inicializar Pygame y el mezclador de audio
def inicializar_pygame():
    pygame.init()
    pygame.mixer.init()  # Inicializa el mezclador de audio

# Cargar y reproducir música de fondo
def cargar_musica_fondo():
    pygame.mixer.music.load('sonido/MusicaN.mp3')
    pygame.mixer.music.play(-1)  # Reproduce en bucle
    pygame.mixer.music.set_volume(0.3)  # Volumen bajo por defecto

# Cargar efectos de sonido
def cargar_sonidos():
    global sonido_colision_tortuga, sonido_oxigeno, sonido_colision_enemigo
    sonido_colision_tortuga = pygame.mixer.Sound('sonido/colision.wav')  # Archivo para colisión con tortuga
    sonido_oxigeno = pygame.mixer.Sound('sonido/colision.wav')  # Archivo para recoger oxígeno
    sonido_colision_enemigo = pygame.mixer.Sound('sonido/colision.wav')  # Archivo para colisión con enemigo

# Gestionar el volumen y la reproducción de la música de fondo
def gestionar_audio(keys):
    if keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0.5)  # Volumen medio
    elif keys[pygame.K_COMMA]:
        pygame.mixer.music.set_volume(1.0)  # Volumen máximo
    elif keys[pygame.K_PERIOD]:  # Tecla para pausar/reanudar música
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.set_volume(0.3)  # Volumen bajo por defecto

# Reproducir sonido de colisión con tortuga
def reproducir_sonido_colision_tortuga():
    sonido_colision_tortuga.play()

# Reproducir sonido al recolectar oxígeno
def reproducir_sonido_oxigeno():
    sonido_oxigeno.play()

# Reproducir sonido de colisión con enemigo
def reproducir_sonido_colision_enemigo():
    sonido_colision_enemigo.play()

# Inicializar Pygame y cargar los sonidos al inicio del juego
inicializar_pygame()
cargar_musica_fondo()
cargar_sonidos()
