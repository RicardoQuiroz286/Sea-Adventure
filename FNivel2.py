import pygame
import random
from personaje import Enemigo, Oxigeno, Jugador, Tortuga, Liberar  # Importa las clases desde sprites.py
from constantes import *  # Importa las variables desde config.py
from musica import cargar_musica_fondo, gestionar_audio, reproducir_sonido_colision_tortuga, reproducir_sonido_oxigeno, reproducir_sonido_colision_enemigo  # Importa las funciones de audio
x = 0

def easy2():

    # Inicialización de Pygame
    pygame.init()
    
    # Pantalla - ventana
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
    
    # Crear grupos de sprites
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
    
    # Función para mostrar el contador de tortugas
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
    
    def recargaPantalla():
        global x  # Define x como global para que la función pueda acceder a ella y modificar su valor
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
    
    
    # Al inicio del código, carga la imagen de fondo
    imagen_fondo_perder = pygame.image.load( "imagen/Fondo/oceano parte_1.png").convert()  # Cambia la ruta a la imagen de perder
    imagen_fondo_pausa = pygame.image.load(  "imagen/Fondo/oceano parte_1.png").convert()  # Cambia la ruta a la imagen de pausa
    imagen_fondo_ganaste = pygame.image.load("imagen/Fondo/oceano parte_1.png").convert()  # Cambia la ruta a la imagen de ganar
    
    # Agrega una variable para controlar el estado de pérdida
    perdedor = False
    
    # Valores iniciales
    TIEMPO_INICIAL = 120000  # Tiempo inicial en milisegundos
    OXIGENO_INICIAL = 3  # Oxígeno inicial del jugador
    
    # Guarda la posición inicial del jugador (buzo)
    posicion_inicial_jugador = (100, 100)  # Cambia esto a las coordenadas iniciales deseadas
    
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
                liberaciones.update()  # Actualizar las liberaciones
    
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
                            
                            # Reposicionar la tortuga
                            tortuga.rect.x = random.randint(W, W + 200)
                            tortuga.rect.y = random.randint(0, H - tortuga.rect.height)
                            break
                        
                # Ganar condiciones
                if contador_liberaciones >= 5:
                    jugador_ganador = True
    
                # Colisiones con oxígeno
                for oxigeno_sprite in oxigeno:
                    if jugador.rect.colliderect(oxigeno_sprite.rect):
                        reproducir_sonido_oxigeno()
                        jugador.recuperar_oxigeno()
                        oxigeno_sprite.rect.x = random.randint(W, W + 200)
    
                # Verificar condición de victoria por tiempo
                if tiempo_restante <= 0:
                    jugador_ganador = True
    
            else:
                # Si el jugador se queda sin oxígeno o el tiempo se acaba
                perdedor = True  # Cambia el estado a perdedor
    
        # Dibuja todo en la pantalla
        recargaPantalla()
    
        # Mostrar pantalla de victoria
        if jugador_ganador:
            # Dibuja la imagen de fondo de ganar
            PANTALLA.blit(imagen_fondo_ganaste, (0, 0))  # Dibuja la imagen en la esquina superior izquierda
    
            # Mostrar el texto de victoria
            mostrar_texto(PANTALLA, "¡GANASTE!", 100, (255, 255, 255), W // 3, H // 2 - 50)
            mostrar_texto(PANTALLA, "Presiona R para reiniciar", 40, (255, 255, 255), W // 3, H // 2 + 50)
            mostrar_texto(PANTALLA, "Presiona S para salir", 40, (255, 255, 255), W // 3, H // 2 + 100)
            pygame.display.update()
    
            # Lógica para reiniciar o salir
            if keys[pygame.K_r]:  # Reiniciar el nivel
                # Reiniciar el juego aquí
                jugador.oxigeno = OXIGENO_INICIAL  # Resetea el oxígeno a su valor inicial
                contador_liberaciones = 0
                tiempo_restante = TIEMPO_INICIAL  # Resetea el tiempo a su valor inicial
                jugador_ganador = False
                perdedor = False
                
                # Restablecer la posición del jugador
                jugador.rect.topleft = posicion_inicial_jugador  # Regresar a la posición inicial
    
                # Aquí puedes agregar la lógica para reiniciar enemigos y objetos
                for enemigo in enemigos:
                    enemigo.rect.x = random.randint(W, W + 200)  # Reposicionar enemigo
                    enemigo.rect.y = random.randint(0, H - enemigo.rect.height)
    
                # Reposicionar tanques de oxígeno si es necesario
                for oxigeno_sprite in oxigeno:
                    oxigeno_sprite.rect.x = random.randint(W, W + 200)  # Reposicionar oxígeno
    
            if keys[pygame.K_s]:  # Salir del juego
                ejecuta = False
    
        # Mostrar pantalla de perder
        elif perdedor:
            # Dibuja la imagen de fondo de perder
            PANTALLA.blit(imagen_fondo_perder, (0, 0))  # Dibuja la imagen en la esquina superior izquierda
    
            # Mostrar opciones de volver a intentar o salir
            mostrar_texto(PANTALLA, "¿VOLVER A INTENTAR?", 100, (255, 255, 255), W // 3 - 200, H // 2 - 50)
            mostrar_texto(PANTALLA, "Presiona R para reiniciar", 40, (255, 255, 255), W // 3 - 150, H // 2 + 50)
            mostrar_texto(PANTALLA, "Presiona S para salir", 40, (255, 255, 255), W // 3 - 150, H // 2 + 100)
            pygame.display.update()
    
            # Lógica para reiniciar o salir
            if keys[pygame.K_r]:  # Reiniciar el nivel
                # Reiniciar el juego aquí
                jugador.oxigeno = OXIGENO_INICIAL  # Resetea el oxígeno a su valor inicial
                contador_liberaciones = 0
                tiempo_restante = TIEMPO_INICIAL  # Resetea el tiempo a su valor inicial
                perdedor = False
                jugador_ganador = False
                
                # Restablecer la posición del jugador
                jugador.rect.topleft = posicion_inicial_jugador  # Regresar a la posición inicial
    
                # Aquí puedes agregar la lógica para reiniciar enemigos y objetos
                for enemigo in enemigos:
                    enemigo.rect.x = random.randint(W, W + 200)  # Reposicionar enemigo
                    enemigo.rect.y = random.randint(0, H - enemigo.rect.height)
    
                # Reposicionar tanques de oxígeno si es necesario
                for oxigeno_sprite in oxigeno:
                    oxigeno_sprite.rect.x = random.randint(W, W + 200)  # Reposicionar oxígeno
    
            if keys[pygame.K_s]:  # Salir del juego
                ejecuta = False
    
        # Mostrar la pantalla de pausa solo si está pausado
        elif pausado:
            # Dibuja la imagen de fondo de pausa
            PANTALLA.blit(imagen_fondo_pausa, (0, 0))  # Dibuja la imagen en la esquina superior izquierda
    
            # Aquí se muestra la pausa
            mostrar_texto(PANTALLA, "PAUSA", 100, (255, 255, 255), W // 2 - 100, H // 2 - 100)
            mostrar_texto(PANTALLA, "Presiona C para continuar", 40, (255, 255, 255), W // 2 - 160, H // 2)
            mostrar_texto(PANTALLA, "Presiona S para salir", 40, (255, 255, 255), W // 2 - 140, H // 2 + 50)
            
            if keys[pygame.K_c]:
                pausado = False
            if keys[pygame.K_s]:
                ejecuta = False
    
        pygame.display.update()
    
    pygame.quit()






