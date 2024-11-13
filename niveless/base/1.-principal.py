import pygame
import random
 

# Iniciación de Pygame
pygame.init()


NEGRO = (0, 0, 0)

# Pantalla - ventana

W, H = 1200, 600
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('Aventura en el mar')
icono = pygame.image.load('imagenes/Buzo.png')
pygame.display.set_icon(icono)

# Fondo del juego
fondo = pygame.image.load('imagenes/foceano.png')

quieto = pygame.image.load('imagenes/Buzo_1.png')

# Música de fondo
pygame.mixer.music.load('sonido/MusicaN.mp3')
pygame.mixer.music.play(-1)






# Jugador
quieto = pygame.image.load('imagenes/buzo_1.png')

caminaDerecha = [
    pygame.image.load('imagenes/buzo_1.png'),
    pygame.image.load('imagenes/buzo_1.png'),
    pygame.image.load('imagenes/buzo_1.png'),
    pygame.image.load('imagenes/buzo_1.png'),
    pygame.image.load('imagenes/buzo_1.png'),
    pygame.image.load('imagenes/buzo_1.png'),
]

caminaIzquierda = [
    pygame.image.load('imagenes/buzo_1.png'),
    pygame.image.load('imagenes/buzo_1.png'),
    pygame.image.load('imagenes/buzo_1.png'),
    pygame.image.load('imagenes/buzo_1.png'),
    pygame.image.load('imagenes/buzo_1.png'),
    pygame.image.load('imagenes/buzo_1.png')
]


# Tortuga

class Tortuga(pygame.sprite.Sprite):
    # Sprite de la tortuga
    def __init__(self):
        super().__init__()
        # Cargar la imagen de la tortuga con transparencia
        self.image = pygame.image.load("imagenes/tortuga.png")
        # Obtener el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Posición inicial aleatoria fuera de la pantalla a la derecha
        self.rect.x = random.randint(W, W + 1000)
        self.rect.y = random.randint(0, H - self.rect.height)
        # Velocidad de movimiento
        self.speed = random.randint(2, 20)
    
    def update(self):
        # Mover la tortuga hacia la izquierda
        self.rect.x -= self.speed
        # Si la tortuga sale de la pantalla por la izquierda, reubicarlo a la derecha
        if self.rect.x < -self.rect.width:
            self.rect.x = random.randint(W, W + 1000)
            self.rect.y = random.randint(0, H - self.rect.height)
            self.speed = random.randint(2, 5)


# Enemigos

class Enemigo(pygame.sprite.Sprite):
    # Sprite de la tortuga
    def __init__(self):
        super().__init__()
        # Cargar la imagen de la tortuga con transparencia
        self.image = pygame.image.load("imagenes/pescado.png")
        # Obtener el rectángulo (sprite)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)
        # Posición inicial aleatoria fuera de la pantalla a la derecha
        self.rect.x = random.randint(W, W + 200)
        self.rect.y = random.randint(0, H - self.rect.height)
        # Velocidad de movimiento
        self.speed = random.randint(2, 8)
    
    def update(self):
        # Mover la tortuga hacia la izquierda
        self.rect.x -= self.speed
        # Si la tortuga sale de la pantalla por la izquierda, reubicarlo a la derecha
        if self.rect.x < -self.rect.width:
            self.rect.x = random.randint(W, W + 1000)
            self.rect.y = random.randint(0, H - self.rect.height)
            self.speed = random.randint(2, 5)











# Crear un grupo de sprites para los enemigos
sprites = pygame.sprite.Group()


# Crear múltiples enemigos
for _ in range(1):  # Puedes ajustar el número de peces globo aquí
    tortuga = Tortuga()
    sprites.add(tortuga)


# Crear múltiples enemigos
for _ in range(4):  # Puedes ajustar el número de peces globo aquí
    enemigo = Enemigo()
    sprites.add(enemigo)


  
    
    

# Sonido

sonido_mute = pygame.image.load('sonido/volume_muted.png')
sonido_max = pygame.image.load('sonido/volume_max.png')

x = 0
px = 50
py = 200
ancho = 40
velocidad = 10

# Control de FPS
reloj = pygame.time.Clock()

# Variables dirección
izquierda = False
derecha = False

# Pasos
cuentaPasos = 0

# Movimiento
def recargaPantalla():
    global cuentaPasos
    global x

    # Fondo en movimiento
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fondo, (x_relativa, 0))
    x -= 5

    # Contador de pasos
    if cuentaPasos + 1 >= 6:
        cuentaPasos = 0

    # Movimiento a la izquierda
    if izquierda:
        PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    # Movimiento a la derecha
    elif derecha:
        PANTALLA.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    else:
        PANTALLA.blit(quieto, (int(px), int(py)))

    # Dibujar todos los enemigos
    sprites.draw(PANTALLA)

ejecuta = True


# Bucle de acciones y controles
while ejecuta:
    # FPS
    reloj.tick(18)

    # Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    # Opción tecla pulsada
    keys = pygame.key.get_pressed()

    # Tecla izquierda - Movimiento a la izquierda
    if keys[pygame.K_LEFT] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False

    # Tecla derecha - Movimiento a la derecha
    elif keys[pygame.K_RIGHT] and px < 900 - velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True

    # Personaje quieto
    else:
        izquierda = False
        derecha = False
        cuentaPasos = 0

    # Tecla arriba - Movimiento hacia arriba
    if keys[pygame.K_UP] and py > 5:
        py -= velocidad

    # Tecla abajo - Movimiento hacia abajo
    if keys[pygame.K_DOWN] and py < 500:
        py += velocidad

    # Control del audio

    # Desactivar sonido
    if keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0.0)
        PANTALLA.blit(sonido_mute, (1050, 500))

    # Reactivar sonido
    if keys[pygame.K_COMMA]:
        pygame.mixer.music.set_volume(1.0)
        PANTALLA.blit(sonido_max, (1050, 500))

    # Actualizar posición de los enemigos
    sprites.update()

    # Llamada a la función de actualización de la ventana
    recargaPantalla()

    # Actualización de la ventana
    pygame.display.update()

# Salida del juego
pygame.quit()
