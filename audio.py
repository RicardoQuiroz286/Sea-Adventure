import pygame



def cargar_musica():
    pygame.mixer.music.load('sonidos/MusicaN.mp3')
    pygame.mixer.music.play(-1)

def gestionar_audio(keys):
    if keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0.5)
    elif keys[pygame.K_COMMA]:
        pygame.mixer.music.set_volume(1.0)
