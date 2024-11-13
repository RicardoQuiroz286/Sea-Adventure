import pygame
import random
from personaje import Enemigo, Oxigeno, Jugador, Tortuga, Liberar  # Importa las clases desde sprites.py
from constantes import *  # Importa las variables desde config.py
from musica import cargar_musica_fondo, gestionar_audio, reproducir_sonido_colision_tortuga, reproducir_sonido_oxigeno, reproducir_sonido_colision_enemigo  # Importa las funciones de audio

def easy():
    # Inicialización de Pygame
    pygame.init()
    
    # Configuración de la ventana del juego
    PANTALLA = pygame.display.set_mode((W, H))
    pygame.display.set_caption('Aventura en el mar')
    icono = pygame.image.load('imagen/Buzo.png')
    pygame.display.set_icon(icono)
    
    # Fondo del juego
    fondo = pygame.image.load('imagen/fondo/foceano.png')
    
    # Crear instancia del jugador
    jugador = Jugador()
    
    # Música de fondo
    cargar_musica_fondo()
    
    # Crear grupos de sprites para organizar los elementos del juego
    sprites = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    tortugas = pygame.sprite.Group()
    oxigeno = pygame.sprite.Group()
    liberaciones = pygame.sprite.Group()  # Grupo para las liberaciones
    
    # Añadir el jugador al grupo de sprites
    sprites.add(jugador)
    
    # Crear enemigos y tortugas
    for _ in range(1):
        tortuga = Tortuga()
        sprites.add(tortuga)
        tortugas.add(tortuga)
    
    for _ in range(8):
        enemigo = Enemigo()
        enemigos.add(enemigo)
    
    for _ in range(2):
        oxigeno_sprite = Oxigeno()
        sprites.add(oxigeno_sprite)
        oxigeno.add(oxigeno_sprite)
    
    # Clase para el botón de pausa
    class BotonPausa(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load('imagen/boton_pausa.png')
            self.image = pygame.transform.scale(self.image, (100, 50))
            self.rect = self.image.get_rect()
            self.rect.topleft = (550, 10)
    
    # Crear el botón de pausa
    boton_pausa = BotonPausa()
    sprites.add(boton_pausa)
    
    # Variables de control
    x = 0
    reloj = pygame.time.Clock()
    contador_liberaciones = 0
    ejecuta = True
    pausado = False
    jugador_ganador = False
    tiempo_total = 120
    tiempo_restante = tiempo_total * 1000
    
    # Función para mostrar texto en pantalla
    def mostrar_texto(pantalla, texto, tamaño, color, x, y):
        fuente = pygame.font.SysFont(None, tamaño)
        render = fuente.render(texto, True, color)
        pantalla.blit(render, (x, y))
    
    # Función para mostrar el temporizador
    def mostrar_temporizador(pantalla, tiempo_restante):
        minutos = tiempo_restante // 60000
        segundos = (tiempo_restante % 60000) // 1000
        tiempo_texto = f"{minutos:02}:{segundos:02}"
        mostrar_texto(pantalla, tiempo_texto, 50, (255, 255, 255), W - 150, 10)
    
    # Función para mostrar el contador de tortugas liberadas
    def mostrar_contador_liberaciones(pantalla, contador):
        imagen_liberacion = pygame.image.load('imagen/tortuga.png')
        imagen_liberacion = pygame.transform.scale(imagen_liberacion, (100, 100))
        pantalla.blit(imagen_liberacion, (220, 10))
        texto_liberaciones = f": {contador} / 5"
        mostrar_texto(pantalla, texto_liberaciones, 40, (255, 255, 255), 300, 40)
    
    # Función para mostrar la pantalla de victoria
    def mostrar_pantalla_ganaste(pantalla):
        overlay = pygame.Surface((W, H))
        overlay.set_alpha(150)
        overlay.fill((0, 0, 0))
        pantalla.blit(overlay, (0, 0))
        mostrar_texto(pantalla, "¡GANASTE!", 100, (255, 255, 255), W // 2 - 100, H // 2 - 100)
        mostrar_texto(pantalla, "Presiona S para salir", 40, (255, 255, 255), W // 2 - 150, H // 2 + 10)
        pygame.display.update()
    
    # Función para mostrar la pantalla de pausa
    def mostrar_pantalla_pausa(pantalla):
        overlay = pygame.Surface((W, H))
        overlay.set_alpha(150)
        overlay.fill((0, 0, 0))
        pantalla.blit(overlay, (0, 0))
        mostrar_texto(pantalla, "PAUSA", 100, (255, 255, 255), W // 2 - 100, H // 2 - 100)
        mostrar_texto(pantalla, "Presiona C para continuar", 40, (255, 255, 255), W // 2 - 160, H // 2)
        mostrar_texto(pantalla, "Presiona S para salir", 40, (255, 255, 255), W // 2 - 140, H // 2 + 50)
        pygame.display.update()
    
    # Función para mostrar la pantalla de volver a intentar
    def mostrar_pantalla_intentar(pantalla):
        overlay = pygame.Surface((W, H))
        overlay.set_alpha(150)
        overlay.fill((0, 0, 0))
        pantalla.blit(overlay, (0, 0))
        mostrar_texto(pantalla, "¿VOLVER A INTENTAR?", 100, (255, 255, 255), W // 2 - 250, H // 2 - 100)
        mostrar_texto(pantalla, "Presiona C para continuar", 40, (255, 255, 255), W // 2 - 160, H // 2)
        mostrar_texto(pantalla, "Presiona S para salir", 40, (255, 255, 255), W // 2 - 140, H // 2 + 50)
        pygame.display.update()
    
    # Función para actualizar la pantalla y mostrar los elementos de juego
    def recargaPantalla():
        global x
        x_relativa = x % fondo.get_rect().width
        PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
        if x_relativa < W:
            PANTALLA.blit(fondo, (x_relativa, 0))
        x -= 5
        sprites.draw(PANTALLA)
        enemigos.draw(PANTALLA)
        jugador.dibujar_tanques_oxigeno(PANTALLA)
        liberaciones.draw(PANTALLA)  # Dibujar las liberaciones
        mostrar_temporizador(PANTALLA, tiempo_restante)
        mostrar_contador_liberaciones(PANTALLA, contador_liberaciones)
    
    # Cargar imágenes para diferentes estados del juego
    imagen_fondo_perder = pygame.image.load("imagen/Fondo/oceano parte_1.png").convert()
    imagen_fondo_pausa = pygame.image.load("imagen/Fondo/oceano parte_1.png").convert()
    imagen_fondo_ganaste = pygame.image.load("imagen/Fondo/oceano parte_1.png").convert()
    
    # Variables de control de juego y tiempo
    perdedor = False
    TIEMPO_INICIAL = 120000
    OXIGENO_INICIAL = 3
    posicion_inicial_jugador = (100, 100)
    
    while ejecuta:
        dt = reloj.tick(18)
        if not pausado and not jugador_ganador and not perdedor:
            tiempo_restante -= dt
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecuta = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if boton_pausa.rect.collidepoint(mouse_pos):
                    pausado = not pausado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausado = not pausado
    
        keys = pygame.key.get_pressed()
    
        if not pausado and not jugador_ganador and not perdedor:
            if jugador.oxigeno > 0 and tiempo_restante > 0:
                jugador.mover(keys)
                gestionar_audio(keys)
                sprites.update()
                enemigos.update()
                liberaciones.update()
    
                # Colisiones con enemigos
                if pygame.sprite.spritecollide(jugador, enemigos, False):
                    jugador.perder_oxigeno()
                    reproducir_sonido_colision_enemigo()
                    for enemigo in enemigos:
                        if enemigo.rect.colliderect(jugador.rect):
                            enemigo.rect.x = random.randint(W, W + 200)
                            enemigo.rect.y = random.randint(0, H - enemigo.rect.height)
    
                # Colisiones con oxígeno
                if pygame.sprite.spritecollide(jugador, oxigeno, True):
                    jugador.ganar_oxigeno()
                    reproducir_sonido_oxigeno()
    
                # Colisiones con tortugas
                tortuga_colision = pygame.sprite.spritecollide(jugador, tortugas, True)
                if tortuga_colision:
                    for tortuga in tortuga_colision:
                        reproducir_sonido_colision_tortuga()
                        liberacion = Liberar(tortuga.rect.center)
                        liberaciones.add(liberacion)
                        sprites.add(liberacion)
                        contador_liberaciones += 1
    
                # Comprobar condiciones de victoria y derrota
                if contador_liberaciones == 5 or tiempo_restante <= 0:
                    jugador_ganador = True
                elif jugador.oxigeno <= 0:
                    perdedor = True
    
            recargaPantalla()
    
        if pausado:
            mostrar_pantalla_pausa(PANTALLA)
        elif jugador_ganador:
            mostrar_pantalla_ganaste(PANTALLA)
        elif perdedor:
            mostrar_pantalla_intentar(PANTALLA)
    
        pygame.display.flip()

    pygame.quit()
