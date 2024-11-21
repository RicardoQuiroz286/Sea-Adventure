import pygame

# Inicializar Pygame y el mezclador de audio
def inicializar_pygame():
    pygame.init()
    pygame.mixer.init()  # Inicializa el mezclador de audio

# Variables globales para las banderas de control
estado_sonido = {
    "perder": False,
    "ganar": False,
    "pausa": False
}

# Estado del juego (ejemplo de control de pausa)
juego_pausado = False  # Bandera para saber si el juego está en pausa

# Cargar y reproducir música de fondo
def cargar_musica_fondo():
    pygame.mixer.music.load('sonido/MusicaN.mp3')
    pygame.mixer.music.play(-1)  # Reproduce en bucle
    pygame.mixer.music.set_volume(1)  # Volumen bajo por defecto

# Cargar efectos de sonido
def cargar_sonidos():
    global sonido_colision_tortuga, sonido_oxigeno, sonido_colision_enemigo
    global sonido_perder, sonido_ganar, sonido_pausar
    sonido_colision_tortuga = pygame.mixer.Sound('sonido/Rescate.wav')  # Archivo para colisión con tortuga
    sonido_oxigeno = pygame.mixer.Sound('sonido/colision.wav')  # Archivo para recoger oxígeno
    sonido_colision_enemigo = pygame.mixer.Sound('sonido/poxigeno.wav')  # Archivo para colisión con enemigo
    sonido_perder = pygame.mixer.Sound('sonido/perder.wav')  # Sonido para evento de pérdida
    sonido_ganar = pygame.mixer.Sound('sonido/ganaste.wav')  # Sonido para evento de victoria
    sonido_pausar = pygame.mixer.Sound('sonido/pausa.wav')  # Sonido para evento de pausa

# Gestionar el volumen y la reproducción de la música de fondo
def gestionar_audio(keys):
    if keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0.5)  # Volumen medio
    elif keys[pygame.K_COMMA]:
        pygame.mixer.music.set_volume(1)  # Volumen máximo
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

# Reproducir sonido al perder
def reproducir_sonido_perder():
    if not estado_sonido["perder"]:
        sonido_perder.play()
        estado_sonido["perder"] = True

# Reproducir sonido al ganar
def reproducir_sonido_ganar():
    if not estado_sonido["ganar"]:
        sonido_ganar.play()
        estado_sonido["ganar"] = True

# Reproducir sonido al pausar
def reproducir_sonido_pausar():
    if not estado_sonido["pausa"]:
        sonido_pausar.play()
        estado_sonido["pausa"] = True

# Manejar la pausa del juego y reproducir sonido al cambiar de estado
def manejar_pausa(keys):
    global juego_pausado
    if keys[pygame.K_p]:  # Suponiendo que la tecla P activa/desactiva la pausa
        juego_pausado = not juego_pausado  # Cambiar el estado de pausa
        if juego_pausado:
            reproducir_sonido_pausar()  # Reproducir sonido solo al entrar en pausa
        else:
            estado_sonido["pausa"] = False  # Restablecer para permitir reproducir nuevamente al pausar

# Restablecer el estado de los sonidos
def reiniciar_estado_sonido():
    for clave in estado_sonido:
        estado_sonido[clave] = False

# Inicializar Pygame y cargar los sonidos al inicio del juego
inicializar_pygame()
cargar_musica_fondo()
cargar_sonidos()
