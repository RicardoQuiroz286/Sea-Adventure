import pygame
import random
from personaje import Enemigo, Oxigeno, Jugador, Tortuga, Liberar  # Importa las clases desde sprites.py
from constantes import *  # Importa las variables desde config.py
from musica import cargar_musica_fondo, gestionar_audio, reproducir_sonido_colision_tortuga, reproducir_sonido_oxigeno, reproducir_sonido_colision_enemigo  # Importa las funciones de audio
x = 0
#hola

def easy1():

    # Inicialización de Pygame
    pygame.init()

    # Pantalla - ventana
    PANTALLA = pygame.display.set_mode((W, H))
    pygame.display.set_caption('Aventura en el mar')
    icono = pygame.image.load('imagen/Buzo.png')
    pygame.display.set_icon(icono)
    
    # Fondo del juego
    fondo = pygame.image.load('imagen/fondo/foceano.png')
    fondopantallas = pygame.image.load('imagen/fondo/Fondoganaste.jpg')
    
    # Crear instancia del jugador
    jugador = Jugador()
    
    # Música de fondo
    cargar_musica_fondo()
    
    # Crear grupos de sprites
    sprites = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    tortugas = pygame.sprite.Group()
    oxigeno = pygame.sprite.Group()
    liberaciones = pygame.sprite.Group()
    
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
    
    # Clase para botones clickeables
    class Boton(pygame.sprite.Sprite):
        def __init__(self, x, y, texto, imagen_path="imagen/botonme.png"):
            super().__init__()
            # Cargar la imagen en lugar de crear un color de fondo
            self.image = pygame.image.load(imagen_path)
            self.image = pygame.transform.scale(self.image, (200, 100))  # Redimensionar si es necesario
    
            # Añadir texto sobre la imagen
            fuente = pygame.font.SysFont(None, 40)
            texto_render = fuente.render(texto, True, (255, 255, 255))  # Texto blanco o de otro color
            self.image.blit(texto_render, (35, 35))  # Alineación del texto
    
            # Obtener el rectángulo para posicionar el botón
            self.rect = self.image.get_rect(center=(x, y))
    
    # Clase para el botón de pausa
    class BotonPausa(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load('imagen/boton_pausa.png')
            self.image = pygame.transform.scale(self.image, (100, 50))
            self.rect = self.image.get_rect()
            self.rect.topleft = (550, 10)
    
    # Crear botones
    boton_pausa = BotonPausa()
    boton_reiniciar = Boton(W // 2, H // 2 + 50, "Reiniciar")
    boton_salir = Boton(W // 2, H // 2 + 120, "Salir")
    boton_continuar = Boton(W // 2, H // 2 + 50, "Continuar")
    
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
    
    # Función para mostrar el contador de tortugas
    def mostrar_contador_liberaciones(pantalla, contador):
        imagen_liberacion = pygame.image.load('imagen/tortuga.png')
        imagen_liberacion = pygame.transform.scale(imagen_liberacion, (100, 100))
        pantalla.blit(imagen_liberacion, (220, 10))
        texto_liberaciones = f": {contador} / 5"
        mostrar_texto(pantalla, texto_liberaciones, 40, (255, 255, 255), 300, 40)
    
    # Función para actualizar la pantalla
    def recargaPantalla():
        global x
        if not pausado and not jugador_ganador and not perdedor:
            x_relativa = x % fondo.get_rect().width
            PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
            if x_relativa < W:
                PANTALLA.blit(fondo, (x_relativa, 0))
            x -= 5
            sprites.draw(PANTALLA)
            enemigos.draw(PANTALLA)
            jugador.dibujar_tanques_oxigeno(PANTALLA)
            liberaciones.draw(PANTALLA)
            mostrar_temporizador(PANTALLA, tiempo_restante)
            mostrar_contador_liberaciones(PANTALLA, contador_liberaciones)
    
    # Variables de estado
    perdedor = False
    TIEMPO_INICIAL = 120000  # Tiempo inicial en milisegundos
    OXIGENO_INICIAL = 3  # Oxígeno inicial del jugador
    posicion_inicial_jugador = (100, 100)  # Posición inicial del jugador
    
    while ejecuta:
        dt = reloj.tick(18)
        if not pausado and not jugador_ganador and not perdedor:
            tiempo_restante -= dt
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecuta = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if boton_pausa.rect.collidepoint(mouse_pos) and not (jugador_ganador or perdedor):
                    pausado = True
                elif pausado:
                    if boton_continuar.rect.collidepoint(mouse_pos):
                        pausado = False
                    elif boton_salir.rect.collidepoint(mouse_pos):
                        ejecuta = False
                elif jugador_ganador or perdedor:
                    if boton_reiniciar.rect.collidepoint(mouse_pos):
                        # Reinicia los valores del juego
                        jugador.oxigeno = OXIGENO_INICIAL
                        contador_liberaciones = 0
                        tiempo_restante = TIEMPO_INICIAL
                        jugador_ganador = False
                        perdedor = False
                        jugador.rect.topleft = posicion_inicial_jugador
                        # Reposicionar enemigos y oxígeno
                        for enemigo in enemigos:
                            enemigo.rect.x = random.randint(W, W + 200)
                            enemigo.rect.y = random.randint(0, H - enemigo.rect.height)
                        for oxigeno_sprite in oxigeno:
                            oxigeno_sprite.rect.x = random.randint(W, W + 200)
                            oxigeno_sprite.rect.y = random.randint(0, H - oxigeno_sprite.rect.height)
                    elif boton_salir.rect.collidepoint(mouse_pos):
                        ejecuta = False
    
            if event.type == pygame.KEYDOWN and not (jugador_ganador or perdedor):
                if event.key == pygame.K_SPACE:  # Espacio para pausar o continuar
                    pausado = not pausado  # Cambia el estado de pausa
    
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
    
                # Colisión con tortugas
                for tortuga in tortugas:
                    if pygame.sprite.spritecollide(jugador, tortugas, False):
                        if tortuga.colision_con_jugador():
                            reproducir_sonido_colision_tortuga()
                            contador_liberaciones += 1
                            liberacion = Liberar(tortuga.rect.x, tortuga.rect.y)
                            liberacion.start_animation()
                            sprites.add(liberacion)
                            liberaciones.add(liberacion)
                            tortuga.rect.x = random.randint(W, W + 200)
                            tortuga.rect.y = random.randint(0, H - tortuga.rect.height)
                            break
                        
                # Colisión con oxígeno
                for oxigeno_sprite in oxigeno:
                    if pygame.sprite.spritecollide(jugador, oxigeno, False):
                        jugador.recuperar_oxigeno()
                        reproducir_sonido_oxigeno()
                        oxigeno_sprite.kill()
    
                # Condiciones para ganar
                if contador_liberaciones >= 5:
                    jugador_ganador = True
                # Condiciones para perder
                elif jugador.oxigeno <= 0 or tiempo_restante <= 0:
                    perdedor = True
    
            # Mostrar la pantalla de juego
            recargaPantalla()
    
            # Mostrar el botón de pausa
            PANTALLA.blit(boton_pausa.image, boton_pausa.rect)
    
        # Pantalla de pausa
        if pausado:
            PANTALLA.blit(fondopantallas, (0, 0))
            mostrar_texto(PANTALLA, "PAUSA", 60, (255, 255, 255), W // 2 - 100, H // 2 - 100)
            boton_continuar.rect.center = (W // 2, H // 2 + 50)
            boton_salir.rect.center = (W // 2, H // 2 + 120)
            PANTALLA.blit(boton_pausa.image, boton_pausa.rect)
            PANTALLA.blit(boton_continuar.image, boton_continuar.rect)
            PANTALLA.blit(boton_salir.image, boton_salir.rect)
    
        # Pantalla de victoria
        if jugador_ganador:
            PANTALLA.blit(fondopantallas, (0, 0))
            mostrar_texto(PANTALLA, "¡RESCATASTE TODAS LAS TORUGAS!", 80, (255, 255, 255), W // 4 - 200, H // 3 - 100)
            mostrar_texto(PANTALLA, "¡FELICIDADES!", 80, (255, 255, 255), W // 2 - 200, H // 2 - 100)
            boton_reiniciar.rect.center = (W // 2, H // 2 + 50)
            boton_salir.rect.center = (W // 2, H // 2 + 120)
            PANTALLA.blit(boton_reiniciar.image, boton_reiniciar.rect)
            PANTALLA.blit(boton_salir.image, boton_salir.rect)
    
        # Pantalla de derrota
        if perdedor:
            PANTALLA.blit(fondopantallas, (0, 0))
            mostrar_texto(PANTALLA, "¡TE QUEDASTE SIN OXIGENO!", 100, (255, 255, 255), W // 4 - 200, H // 4 - 100)
            mostrar_texto(PANTALLA, "¿VOLVER A INTENTAR?", 100, (255, 255, 255), W // 3 - 200, H // 2 - 100)
            boton_reiniciar.rect.center = (W // 2, H // 2 + 50)
            boton_salir.rect.center = (W // 2, H // 2 + 120)
            PANTALLA.blit(boton_reiniciar.image, boton_reiniciar.rect)
            PANTALLA.blit(boton_salir.image, boton_salir.rect)
    
        pygame.display.update()







