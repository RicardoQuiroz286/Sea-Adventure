import pygame
import random
from personaje import Enemigo, Tortuga, Oxigeno, Jugador  # Importa las clases desde sprites.py
from constantes import *  # Importa las variables desde config.py
from audio import cargar_musica, gestionar_audio  # Importa las funciones de audio

# Inicialización de Pygame
pygame.init()

# Pantalla - ventana
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('Aventura en el mar')
icono = pygame.image.load('imagenes/Buzo.png')
pygame.display.set_icon(icono)

# Fondo del juego
fondo = pygame.image.load('imagenes/fondo/foceano.png')

# Sprite que aparece al colisionar con la tortuga
class TortugaSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagenes = [
            pygame.image.load('imagenes/tortuga.png'),
            pygame.image.load('imagenes/tortugac.png'),
            pygame.image.load('imagenes/tortuga.png'),
            pygame.image.load('imagenes/tortugac.png'),
            pygame.image.load('imagenes/tortuga.png'),
            pygame.image.load('imagenes/tortugac.png')
        ]
        self.index = 0
        self.image = self.imagenes[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(W, W + 1000)
        self.animating = False
        self.tocada = False
        self.frame_count = 0

    def start_animation(self):
        self.animating = True

    def update(self):
        if self.animating:
            self.frame_count += 1
            if self.frame_count % 5 == 0:  # Cambiar imagen cada 5 frames
                self.index = (self.index + 1) % len(self.imagenes)
                self.image = self.imagenes[self.index]
            if self.index == len(self.imagenes) - 1:
                self.animating = False  # Detener animación al finalizar

# Crear instancia del jugador
jugador = Jugador()

# Música de fondo
cargar_musica()  # Función de audio.py

# Crear grupos de sprites
sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
tortugas = pygame.sprite.Group()
oxigeno = pygame.sprite.Group()

# Añadir el jugador al grupo de sprites
sprites.add(jugador)

# Crear enemigos y tortugas
for _ in range(1):
    tortuga = Tortuga()
    sprites.add(tortuga)
    tortugas.add(tortuga)  # Añadir al grupo de tortugas

for _ in range(4):
    enemigo = Enemigo()
    enemigos.add(enemigo)

for _ in range(2):
    oxigeno_sprite = Oxigeno()  # Crear instancia de Oxigeno
    sprites.add(oxigeno_sprite)  # Agregar al grupo general de sprites
    oxigeno.add(oxigeno_sprite)  # Agregar al grupo de oxigeno

# Clase para el botón de pausa
class BotonPausa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('imagenes/boton_pausa.png')  # Cargar imagen del botón
        self.image = pygame.transform.scale(self.image, (100, 50))  # Cambiar tamaño de la imagen (ancho, alto)
        self.rect = self.image.get_rect()
        self.rect.topleft = (550, 10)  # Posición del botón en la pantalla

    def update(self):
        pass  # No hay actualización necesaria para el botón

# Crear el botón de pausa
boton_pausa = BotonPausa()
sprites.add(boton_pausa)

# Variables de control
x = 0
reloj = pygame.time.Clock()
contador_tortugas = 0  # Contador de tortugas colisionadas

# Función para mostrar texto en pantalla
def mostrar_texto(pantalla, texto, tamaño, color, x, y):
    fuente = pygame.font.SysFont(None, tamaño)
    render = fuente.render(texto, True, color)
    pantalla.blit(render, (x, y))

# *** Función para mostrar el temporizador ***
def mostrar_temporizador(pantalla, tiempo_restante):
    minutos = tiempo_restante // 60000
    segundos = (tiempo_restante % 60000) // 1000
    tiempo_texto = f"{minutos:02}:{segundos:02}"
    mostrar_texto(pantalla, tiempo_texto, 50, (255, 255, 255), W - 150, 10)

# *** Función para mostrar el contador de tortugas ***
def mostrar_contador_tortugas(pantalla, contador):
    # Cargar la imagen de la tortuga
    imagen_tortuga = pygame.image.load('imagenes/tortuga.png')  # Cambia esta ruta a la ubicación de tu imagen
    imagen_tortuga = pygame.transform.scale(imagen_tortuga, (100, 100))  # Ajusta el tamaño de la imagen si es necesario

    # Dibujar la imagen de la tortuga en la pantalla
    pantalla.blit(imagen_tortuga, (220, 10))  # Dibuja la imagen en la posición deseada

    # Mostrar el texto del contador
    texto_tortugas = f": {contador} / 5"
    mostrar_texto(pantalla, texto_tortugas, 40, (255, 255, 255), 300, 40)  # Ajusta la posición x para que no se superponga a la imagen

# *** Función para mostrar la pantalla de victoria ***
def mostrar_pantalla_ganaste(pantalla):
    overlay = pygame.Surface((W, H))
    overlay.set_alpha(150)  # Ajusta la transparencia
    overlay.fill((0, 0, 0))  # Fondo negro semitransparente
    pantalla.blit(overlay, (0, 0))  # Dibujar el overlay

    mostrar_texto(pantalla, "¡GANASTE!", 100, (255, 255, 255), 400, H // 2 - 100)
    mostrar_texto(pantalla, "Presiona S para salir", 40, (255, 255, 255), W // 2 - 150, H // 2 + 10)

    pygame.display.update()  # Actualiza la pantalla

# Función para actualizar la pantalla
def recargaPantalla():
    global x
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fondo, (x_relativa, 0))
    x -= 5

    # Dibujar todos los sprites
    sprites.draw(PANTALLA)
    enemigos.draw(PANTALLA)

    # Dibujar los tanques de oxígeno del jugador
    jugador.dibujar_tanques_oxigeno(PANTALLA)

    # *** Mostrar el temporizador ***
    mostrar_temporizador(PANTALLA, tiempo_restante)

    # *** Mostrar el contador de tortugas ***
    mostrar_contador_tortugas(PANTALLA, contador_tortugas)

# *** Función para mostrar el menú de pausa ***
def mostrar_menu_pausa(pantalla):
    # Crear una superficie semitransparente del tamaño de la pantalla
    overlay = pygame.Surface((W, H))  
    overlay.set_alpha(50)  # Ajusta la transparencia (0-255, donde 255 es opaco y 0 es completamente transparente)
    overlay.fill((0, 0, 0))  # Llena la superficie con color negro
    
    # Dibujar la superficie semitransparente sobre la pantalla
    pantalla.blit(overlay, (0, 0))  
     
    # Mostrar texto del menú
    mostrar_texto(pantalla, "PAUSA",                    100, (255, 255, 255), W // 2 - 100, H // 2 - 100)
    mostrar_texto(pantalla, "Presiona C para continuar", 40, (255, 255, 255), W // 2 - 150, H // 2 + 10)
    mostrar_texto(pantalla, "Presiona S para salir",     40, (255, 255, 255), W // 2 - 150, H // 2 + 50)
    
    pygame.display.update()  # Actualiza la pantalla

# Bucle principal del juego
ejecuta = True
tortuga_sprite = True  # Controlar el sprite de tortuga al colisionar
pausado = False  # Variable para controlar la pausa
jugador_ganador = False

# *** Agregar temporizador ***
tiempo_total = 120  # Duración del temporizador en segundos
tiempo_restante = tiempo_total * 1000  # Convertir segundos a milisegundos

while ejecuta:
    dt = reloj.tick(18)
    if not pausado and not jugador_ganador:  # Solo disminuir tiempo si no está en pausa o si el jugador no ha ganado
        tiempo_restante -= dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if boton_pausa.rect.collidepoint(mouse_pos):
                pausado = not pausado

    keys = pygame.key.get_pressed()

    if not pausado and not jugador_ganador:
        if jugador.oxigeno > 0 and tiempo_restante > 0:
            jugador.mover(keys)
            gestionar_audio(keys)
            sprites.update()
            enemigos.update()

            # Verificar colisión del jugador con los enemigos
            colision_con_enemigos = pygame.sprite.spritecollide(jugador, enemigos, False)
            if colision_con_enemigos:
                jugador.perder_oxigeno()

            # Verificar colisión con tortuga
            colision_con_tortuga = pygame.sprite.spritecollide(jugador, tortugas, False)
            if colision_con_tortuga:
                if tortuga_sprite is None:
                    tortuga_sprite = TortugaSprite()  # Crear una instancia de TortugaSprite
                    sprites.add(tortuga_sprite)
                    tortuga_sprite.start_animation()

                # Incrementar el contador de tortugas
                contador_tortugas += 1

            # Verificar colisión con tanques de oxígeno
            colision_con_oxigeno = pygame.sprite.spritecollide(jugador, oxigeno, False)  # False para no eliminar el sprite
            for tanque in colision_con_oxigeno:
                if not tanque.recogido:  # Solo si el tanque no ha sido recogido
                    jugador.recuperar_oxigeno()  # Recuperar oxígeno al recoger
                    tanque.recogido = True  # Marcar el tanque como recogido
                    tanque.tiempo_recogido = pygame.time.get_ticks()  # Registrar el tiempo en que fue recogido

            # *** Si el contador de tortugas llega a 6, el jugador gana **6*
            if contador_tortugas >= 6:
                jugador_ganador = True  # Cambiar el estado a ganador
                mostrar_pantalla_ganaste(PANTALLA)

        # Recargar pantalla
        recargaPantalla()

        # *** Si el oxígeno o el tiempo se acaban ***
        if jugador.oxigeno <= 0 or tiempo_restante <= 0:
            pausado = False  # Pausar el juego
            mostrar_texto(PANTALLA, "GAME OVER", 100, (255, 255, 255), W // 2 - 200, H // 2 - 50)
            pygame.display.update()

    elif jugador_ganador:
        mostrar_pantalla_ganaste(PANTALLA)
        if keys[pygame.K_s]:  # Salir del juego al presionar 'S'
            ejecuta = False

    else:
        mostrar_menu_pausa(PANTALLA)
        if keys[pygame.K_c]:  # Reanudar el juego al presionar 'C'
            pausado = False
        if keys[pygame.K_s]:  # Salir del juego al presionar 'S'
            ejecuta = False

    pygame.display.update()

pygame.quit()
