import pygame
import random
from NiñaFNivel3 import *
from personaje import EnemigoF, Oxigeno, JugadorM, Foca, LiberarFoca  # Importa las clases desde sprites.py
from constantes import *  # Importa las variables desde config.py
from musica import cargar_musica_fondo, gestionar_audio, reproducir_sonido_colision_tortuga, reproducir_sonido_oxigeno, reproducir_sonido_colision_enemigo, reproducir_sonido_ganar, reproducir_sonido_pausar, reproducir_sonido_perder, estado_sonido, reiniciar_estado_sonido, manejar_pausa  # Importa las funciones de audio
x = 0



def mostrar_pantalla_inicial(pantalla, imagen_inicial):
    """Muestra una pantalla inicial hasta que el usuario presione una tecla."""
    reloj = pygame.time.Clock()
    mostrar = True
    
    # Configura la fuente y el mensaje
    fuente = pygame.font.Font(None, 36)  # Usa una fuente predeterminada, tamaño 36
    texto = fuente.render("Presiona cualquier tecla para jugar", True, (255, 0, 0))  # Texto en blanco
    texto_rect = texto.get_rect(center=(W // 1.3, H - 50))  # Centra el texto en la parte inferior

    while mostrar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Si el usuario cierra la ventana
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:  # Si presiona cualquier tecla
                mostrar = False

        pantalla.blit(imagen_inicial, (0, 0))  # Dibuja la imagen inicial
        pantalla.blit(texto, texto_rect)  # Dibuja el texto
        pygame.display.update()
        reloj.tick(30)  # Controla la velocidad del bucle





def ñaeasy2():

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
    
     # Imagen inicial
    imagen_inicial = pygame.image.load('imagen/fondo/controles.jpg')  # Ruta de la imagen inicial
    imagen_inicial = pygame.transform.scale(imagen_inicial, (W, H))  # Ajusta el tamaño de la imagen al tamaño de la pantalla
    
    # Mostrar pantalla inicial
    mostrar_pantalla_inicial(PANTALLA, imagen_inicial)
    
    # Crear instancia del jugador
    jugador = JugadorM()
    
    # Música de fondo
    cargar_musica_fondo()
    
    # Crear grupos de sprites
    sprites = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    focas = pygame.sprite.Group()
    oxigeno = pygame.sprite.Group()
    liberaciones = pygame.sprite.Group()
    
    # Añadir el jugador al grupo de sprites
    sprites.add(jugador)
    
    # Crear enemigos y focas
    for _ in range(1):
        foca = Foca()
        sprites.add(foca)
        focas.add(foca)
    
    for _ in range(6):
        enemigo = EnemigoF()
        enemigos.add(enemigo)
    
    for _ in range(3):
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
    
         # Clase para botones clickeables
    class Boton(pygame.sprite.Sprite):
        def __init__(self, x, y, texto, imagen_path="imagen/botonme.png"):
            super().__init__()
            # Cargar la imagen en lugar de crear un color de fondo
            self.image = pygame.image.load(imagen_path)
            self.image = pygame.transform.scale(self.image, (300, 100))  # Redimensionar si es necesario

            # Añadir texto sobre la imagen
            fuente = pygame.font.SysFont(None, 40)
            texto_render = fuente.render(texto, True, (255, 255, 255))  # Texto blanco o de otro color

            # Obtener el rectángulo del texto y centrarlo dentro de la imagen
            texto_rect = texto_render.get_rect(center=self.image.get_rect().center)

            # Poner el texto centrado sobre la imagen
            self.image.blit(texto_render, texto_rect)

            # Obtener el rectángulo para posicionar el botón
            self.rect = self.image.get_rect(center=(x, y))

    # Crear botones
    boton_pausa = BotonPausa()
    boton_reiniciar = Boton(W // 3, H // 3 + 50, "REINICIAR")
    boton_salir = Boton(W // 3, H // 3 + 120, "SALIR")
    boton_continuar = Boton(W // 3, H // 2 + 50, "CONTINUAR")
    boton_siguiente_nivel = Boton(W // 3, H // 2 + 50, "CONTINUAR")
    
    # Variables de control
    x = 0
    reloj = pygame.time.Clock()
    contador_liberaciones = 0
    ejecuta = True
    pausado = False
    jugador_ganador = False
    tiempo_total = 120
    tiempo_restante = tiempo_total * 1000
    musica_silenciada = False  # Bandera para verificar si la música está silenciada
    volumen_original = 0.5  # Volumen inicial de la música (ajústalo según sea necesario)
    pygame.mixer.music.set_volume(volumen_original)  # Configura el volumen inicial

    
    
    # Carga la imagen de "PAUSA"
    imagen_pausa = pygame.image.load("imagen/pausaimg.png")
    imagen_rescate = pygame.image.load("imagen/rescatasteatodos.png")
    imagen_felicidades = pygame.image.load("imagen/felicidades.png")
    imagen_sinoxigeno = pygame.image.load("imagen/tequedastesinoxigeno.png")
    imagen_intentar = pygame.image.load("imagen/volverintentar.png")       
    def mostrar_imagen_pausa(pantalla, imagen, x, y):
        pantalla.blit(imagen, (x, y))       
    def mostrar_imagen_rescate(pantalla, imagen, x, y):
        pantalla.blit(imagen, (x, y))       
    def mostrar_imagen_felicidades(pantalla, imagen, x, y):
        pantalla.blit(imagen, (x, y))       
    def mostrar_imagen_sinoxigeno(pantalla, imagen, x, y):
        pantalla.blit(imagen, (x, y))       
    def mostrar_imagen_intentar(pantalla, imagen, x, y):
        pantalla.blit(imagen, (x, y))
    
    
    
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
        imagen_liberacion = pygame.image.load('imagen/foca/foca.png')
        imagen_liberacion = pygame.transform.scale(imagen_liberacion, (100, 100))
        pantalla.blit(imagen_liberacion, (210, 1))
        texto_liberaciones = f": {contador} / 5"
        mostrar_texto(pantalla, texto_liberaciones, 40, (255, 255, 255), 300, 40)
        
    
    def reproducir_sonido_perder():
    # Cargar y reproducir el sonido de pausa
     pygame.mixer.Sound('sonido/perder.wav').play()
    
    def reproducir_sonido_pausar():
    # Cargar y reproducir el sonido de pausa
     pygame.mixer.Sound('sonido/pausa.wav').play()
     
    
     
    def reproducir_sonido_ganar():
    # Cargar y reproducir el sonido de pausa
     pygame.mixer.Sound('sonido/Ganaste.wav').play()

    
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
    
    # Variables de control para los sonidos
    sonido_pausa_reproducido = False
    sonido_ganar_reproducido = False
    sonido_perder_reproducido = False








#---------------------------------------------------------------------------------------------------------------------------------------






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
                        sonido_pausa_reproducido = False  # Permitir que el sonido de pausa se reproduzca nuevamente
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
                        sonido_ganar_reproducido = False
                        sonido_perder_reproducido = False
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
                    sonido_pausa_reproducido = False  # Restablece el sonido de pausa

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

                # Colisión con focas
                for foca in focas:
                    if pygame.sprite.spritecollide(jugador, focas, False):
                        if foca.colision_con_jugador():
                            reproducir_sonido_colision_tortuga()
                            contador_liberaciones += 1
                            liberacion = LiberarFoca(foca.rect.x, foca.rect.y)
                            liberacion.start_animation()
                            sprites.add(liberacion)
                            liberaciones.add(liberacion)
                            foca.rect.x = random.randint(W, W + 200)
                            foca.rect.y = random.randint(0, H - foca.rect.height)
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
            if not sonido_pausa_reproducido:
                reproducir_sonido_pausar()
                sonido_pausa_reproducido = True  # Marcar como reproducido
            mostrar_imagen_pausa(PANTALLA, imagen_pausa, W // 2.8 - 100, H // 3 - 100)
            boton_continuar.rect.center = (W // 2, H // 2 + 50)
            boton_salir.rect.center = (W // 2, H // 2 + 120)
            PANTALLA.blit(boton_pausa.image, boton_pausa.rect)
            PANTALLA.blit(boton_continuar.image, boton_continuar.rect)
            PANTALLA.blit(boton_salir.image, boton_salir.rect)

        # Pantalla de victoria
         # Pantalla de victoria
        if jugador_ganador:
            PANTALLA.blit(fondopantallas, (0, 0))
            if not sonido_ganar_reproducido:
                reproducir_sonido_ganar()
                sonido_ganar_reproducido = True  # Marcar como reproducido
            mostrar_imagen_rescate(PANTALLA, imagen_rescate, W // 6.8 - 100, H // 3 - 100)
            mostrar_imagen_felicidades(PANTALLA, imagen_felicidades, W // 2.2 - 300, H // 2 - 100)
            boton_reiniciar.rect.center = (W // 2, H // 2 + 50)
            boton_salir.rect.center = (W // 2, H // 2 + 120)
            boton_siguiente_nivel.rect.center = (W // 2, H // 2 + 180)  # Posicionar el botón de siguiente nivel
            PANTALLA.blit(boton_reiniciar.image, boton_reiniciar.rect)
            PANTALLA.blit(boton_salir.image, boton_salir.rect)
            PANTALLA.blit(boton_siguiente_nivel.image, boton_siguiente_nivel.rect)  # Mostrar el botón

            # Comprobar si el jugador hace clic en "Siguiente Nivel"
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if boton_siguiente_nivel.rect.collidepoint(mouse_pos):
                    ñaeasy3()  # Llama a la función para el siguiente nivel

        # Pantalla de derrota
        if perdedor:
            PANTALLA.blit(fondopantallas, (0, 0))
            if not sonido_perder_reproducido:
                reproducir_sonido_perder()
                sonido_perder_reproducido = True  # Marcar como reproducido
            mostrar_imagen_sinoxigeno(PANTALLA, imagen_sinoxigeno, W // 11.8 - 100, H // 3 - 100)
            mostrar_imagen_intentar(PANTALLA, imagen_intentar, W // 2.8 - 300, H // 2 - 100)
            boton_reiniciar.rect.center = (W // 2, H // 2 + 50)
            boton_salir.rect.center = (W // 2, H // 2 + 120)
            PANTALLA.blit(boton_reiniciar.image, boton_reiniciar.rect)
            PANTALLA.blit(boton_salir.image, boton_salir.rect)

        pygame.display.update()





