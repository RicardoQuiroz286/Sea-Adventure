import pygame
import random
from PIL import Image
from constantes import W, H, NEGRO







# --------------------------------------------------------------------------------------------------------------------------





#   TORTUGA

class Tortuga(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Cargar las imágenes para la animación
        self.imagenes = [
            pygame.image.load('imagen/tortuga/tortugacapturada1.png'),
            pygame.image.load('imagen/tortuga/tortugacapturada2.png')
        ]
        
       # Cambiar el tamaño de la imagen (por ejemplo, 50x50 píxeles)
        self.imagenes = [pygame.transform.scale(imagen, (150, 120)) for imagen in self.imagenes]
        
        self.image = self.imagenes[0]  # Establecer la imagen inicial
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)

        # Establecer la posición inicial
        self.rect.x = random.randint(W, W + 200)
        self.rect.y = random.randint(0, H - self.rect.height)

        # Aumentar el rango de velocidad
        self.speed = random.randint(8, 12)  # Rango ajustado para mayor velocidad

        self.contador_animacion = 0  # Contador para cambiar entre imágenes
        
        # Variables para el cooldown de colisiones
        self.cooldown = 2000  # 2 segundos de cooldown
        self.ultimo_impacto = 0  # Tiempo del último impacto registrado

    def update(self):
        # Actualizar la animación
        self.contador_animacion += 1
        if self.contador_animacion >= len(self.imagenes) * 5:  # Cambiar la imagen cada 5 fotogramas
            self.contador_animacion = 0
        self.image = self.imagenes[self.contador_animacion // 5]

        # Mover la tortuga
        self.rect.x -= self.speed
        if self.rect.x < -self.rect.width:
            self.rect.x = random.randint(W, W + 1000)
            self.rect.y = random.randint(0, H - self.rect.height)
            # Mantener el rango de velocidad al reaparecer
            self.speed = random.randint(8, 12)  # Rango ajustado para mayor velocidad

    def colision_con_jugador(self):
        # Verifica si el cooldown ha pasado desde el último impacto
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.ultimo_impacto >= self.cooldown:
            self.ultimo_impacto = tiempo_actual  # Actualiza el tiempo del último impacto
            return True  # Indica que la colisión es válida
        return False  # Si no ha pasado el cooldown, la colisión no es válida







#   FOCA

class Foca(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Cargar las imágenes para la animación
        self.imagenes = [
            pygame.image.load('imagen/foca/foca_capturada1.png'),
            pygame.image.load('imagen/foca/foca_capturada2.png'),
            pygame.image.load('imagen/foca/foca_capturada3.png')
        ]
        
        # Cambiar el tamaño de la imagen (por ejemplo, 50x50 píxeles)
        self.imagenes = [pygame.transform.scale(imagen, (150, 120)) for imagen in self.imagenes]
        
        self.image = self.imagenes[0]  # Establecer la imagen inicial
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)

        # Establecer la posición inicial
        self.rect.x = random.randint(W, W + 200)
        self.rect.y = random.randint(0, H - self.rect.height)

        # Aumentar el rango de velocidad
        self.speed = random.randint(8, 12)  # Rango ajustado para mayor velocidad

        self.contador_animacion = 0  # Contador para cambiar entre imágenes
        
        # Variables para el cooldown de colisiones
        self.cooldown = 2000  # 2 segundos de cooldown
        self.ultimo_impacto = 0  # Tiempo del último impacto registrado

    def update(self):
        # Actualizar la animación
        self.contador_animacion += 1
        if self.contador_animacion >= len(self.imagenes) * 5:  # Cambiar la imagen cada 5 fotogramas
            self.contador_animacion = 0
        self.image = self.imagenes[self.contador_animacion // 5]

        # Mover la tortuga
        self.rect.x -= self.speed
        if self.rect.x < -self.rect.width:
            self.rect.x = random.randint(W, W + 1000)
            self.rect.y = random.randint(0, H - self.rect.height)
            # Mantener el rango de velocidad al reaparecer
            self.speed = random.randint(8, 12)  # Rango ajustado para mayor velocidad

    def colision_con_jugador(self):
        # Verifica si el cooldown ha pasado desde el último impacto
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.ultimo_impacto >= self.cooldown:
            self.ultimo_impacto = tiempo_actual  # Actualiza el tiempo del último impacto
            return True  # Indica que la colisión es válida
        return False  # Si no ha pasado el cooldown, la colisión no es válida






#   DELFIN

class Delfin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Cargar las imágenes para la animación
        self.imagenes = [
            pygame.image.load('imagen/delfin/delfin_capturado1.png'),
            pygame.image.load('imagen/delfin/delfin_capturado2.png'),
            pygame.image.load('imagen/delfin/delfin_capturado3.png')
        ]
        
        # Cambiar el tamaño de la imagen (por ejemplo, 50x50 píxeles)
        self.imagenes = [pygame.transform.scale(imagen, (150, 120)) for imagen in self.imagenes]
        
        self.image = self.imagenes[0]  # Establecer la imagen inicial
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)

        # Establecer la posición inicial
        self.rect.x = random.randint(W, W + 200)
        self.rect.y = random.randint(0, H - self.rect.height)

        # Aumentar el rango de velocidad
        self.speed = random.randint(8, 12)  # Rango ajustado para mayor velocidad

        self.contador_animacion = 0  # Contador para cambiar entre imágenes
        
        # Variables para el cooldown de colisiones
        self.cooldown = 2000  # 2 segundos de cooldown
        self.ultimo_impacto = 0  # Tiempo del último impacto registrado

    def update(self):
        # Actualizar la animación
        self.contador_animacion += 1
        if self.contador_animacion >= len(self.imagenes) * 5:  # Cambiar la imagen cada 5 fotogramas
            self.contador_animacion = 0
        self.image = self.imagenes[self.contador_animacion // 5]

        # Mover la tortuga
        self.rect.x -= self.speed
        if self.rect.x < -self.rect.width:
            self.rect.x = random.randint(W, W + 1000)
            self.rect.y = random.randint(0, H - self.rect.height)
            # Mantener el rango de velocidad al reaparecer
            self.speed = random.randint(8, 12)  # Rango ajustado para mayor velocidad

    def colision_con_jugador(self):
        # Verifica si el cooldown ha pasado desde el último impacto
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.ultimo_impacto >= self.cooldown:
            self.ultimo_impacto = tiempo_actual  # Actualiza el tiempo del último impacto
            return True  # Indica que la colisión es válida
        return False  # Si no ha pasado el cooldown, la colisión no es válida







# --------------------------------------------------------------------------------------------------------------------------















class EnemigoF(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Definir el tamaño deseado para las imágenes
        ancho, alto = 100, 100  # Cambia estos valores para ajustar el tamaño
        
        # Cargar y escalar las imágenes para la animación
        self.imagenes = [
            pygame.transform.scale(pygame.image.load(f'imagen/Pezglobo/globo{i}.png'), (ancho, alto))
            for i in range(1, 18)
        ]
        self.image = self.imagenes[0]  # Establecer la imagen inicial
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)

        # Posición y velocidad iniciales
        self.rect.x = random.randint(W, W + 200)
        self.rect.y = random.randint(0, H - self.rect.height)
        self.speed = random.randint(5, 12)  # Aumentar el rango de velocidad

        self.contador_animacion = 0  # Contador para cambiar entre imágenes

    def update(self):
        # Actualizar la animación
        self.contador_animacion += 1
        if self.contador_animacion >= len(self.imagenes) * 17:  # Cambiar la imagen cada 17 fotogramas
            self.contador_animacion = 0
        self.image = self.imagenes[self.contador_animacion // 17]

        # Mover el enemigo
        self.rect.x -= self.speed
        if self.rect.x < -self.rect.width:
            self.rect.x = random.randint(W, W + 1000)
            self.rect.y = random.randint(0, H - self.rect.height)
            self.speed = random.randint(5, 12)  # Mantener rango de velocidad al reaparecer





class EnemigoD(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Definir el tamaño deseado para las imágenes
        ancho, alto = 100, 100  # Cambia estos valores para ajustar el tamaño
        
        # Cargar y escalar las imágenes para la animación
        self.imagenes = [
            pygame.transform.scale(pygame.image.load(f'imagen/Pezglobo/globo{i}.png'), (ancho, alto))
            for i in range(1, 18)
        ]
        self.image = self.imagenes[0]  # Establecer la imagen inicial
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)

        # Posición y velocidad iniciales
        self.rect.x = random.randint(W, W + 200)
        self.rect.y = random.randint(0, H - self.rect.height)
        self.speed = random.randint(10, 20)  # Incrementar el rango de velocidad

        self.contador_animacion = 0  # Contador para cambiar entre imágenes

    def update(self):
        # Actualizar la animación
        self.contador_animacion += 1
        if self.contador_animacion >= len(self.imagenes) * 17:  # Cambiar la imagen cada 17 fotogramas
            self.contador_animacion = 0
        self.image = self.imagenes[self.contador_animacion // 17]

        # Mover el enemigo
        self.rect.x -= self.speed
        if self.rect.x < -self.rect.width:
            self.rect.x = random.randint(W, W + 1000)
            self.rect.y = random.randint(0, H - self.rect.height)
            self.speed = random.randint(10, 20)  # Mantener rango de velocidad al reaparecer








# --------------------------------------------------------------------------------------------------------------------------













class Oxigeno(pygame.sprite.Sprite):
    velocidad_comun = 4  # Puedes cambiar este valor a la velocidad deseada

    def __init__(self):
        super().__init__()
        # Cargar las imágenes para la animación
        self.imagenes = [
            pygame.image.load('imagen/tanqueo1.png')
        ]
        self.image = self.imagenes[0]  # Establecer la imagen inicial
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)

        self.rect.x = random.randint(W, W + 200)
        self.rect.y = random.randint(0, H - self.rect.height)
        self.tiempo_respawn = 5000  # Tiempo de respawn en milisegundos (5 segundos)
        self.recogido = False  # Para controlar si fue recogido
        self.tiempo_recogido = 0  # Tiempo cuando fue recogido

        # Asignar la velocidad común a cada instancia
        self.speed = Oxigeno.velocidad_comun

        self.contador_animacion = 0  # Contador para cambiar entre imágenes
    
    def update(self):
        # Actualizar la animación
        self.contador_animacion += 1
        if self.contador_animacion >= len(self.imagenes) * 1:  # Cambiar la imagen cada 5 fotogramas
            self.contador_animacion = 0
        self.image = self.imagenes[self.contador_animacion // 1]
        
        if self.recogido:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_recogido >= self.tiempo_respawn:
                self.recogido = False  # Marcar como no recogido para reaparecer

        # Mover el tanque de oxígeno con la velocidad común
        self.rect.x -= self.speed
        if self.rect.x < -self.rect.width:
            self.rect.x = random.randint(W, W + 1000)
            self.rect.y = random.randint(0, H - self.rect.height)
            self.speed = Oxigeno.velocidad_comun  # Mantener la misma velocidad








# --------------------------------------------------------------------------------------------------------------------------








NEGRO = (0, 0, 0)

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Cargar las imágenes de animación del buzo
        self.imagenes = [
            pygame.image.load('imagen/personajes/nadar1.gif'),
            pygame.image.load('imagen/personajes/nadar2.gif'),
            pygame.image.load('imagen/personajes/nadar3.gif'),
            pygame.image.load('imagen/personajes/nadar4.gif'),
            pygame.image.load('imagen/personajes/nadar5.gif'),
            pygame.image.load('imagen/personajes/nadar6.gif'),
            pygame.image.load('imagen/personajes/nadar7.gif'),
            pygame.image.load('imagen/personajes/nadar8.gif'),
            pygame.image.load('imagen/personajes/nadar9.gif'),
            pygame.image.load('imagen/personajes/nadar10.gif'),
            pygame.image.load('imagen/personajes/nadar11.gif')
        ]
        
        # Asegurarse de que el fondo negro sea transparente
        for i in range(len(self.imagenes)):
            self.imagenes[i] = self.imagenes[i].convert()  # Convierte a formato optimizado
            self.imagenes[i].set_colorkey(NEGRO)  # Establece el color negro como transparente

        self.indice_animacion = 0
        self.image = self.imagenes[self.indice_animacion]

        # Definir el rectángulo de colisión y ajustar tamaño
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-self.rect.width * 0.5, -self.rect.height * 0.3)  # Ajuste de colisión

        # Posición inicial del personaje
        self.rect.topleft = (30, 250)

        # Atributos del jugador
        self.velocidad = 10
        self.oxigeno = 3  # Tanques de oxígeno iniciales

        # Variables de animación
        self.tiempo_ultimo_frame = pygame.time.get_ticks()
        self.velocidad_animacion = 150  # Cambiar imagen cada 100 ms

        # Variables de invulnerabilidad
        self.invulnerable = False
        self.tiempo_invulnerable = 2000  # Tiempo de invulnerabilidad en ms
        self.ultimo_daño = 0  # Momento del último daño

    def mover(self, keys):
        # Movimiento del jugador si tiene oxígeno
        if self.oxigeno > 0:
            if keys[pygame.K_LEFT] and self.rect.left > self.velocidad:
                self.rect.x -= self.velocidad
            if keys[pygame.K_RIGHT] and self.rect.right < W:
                self.rect.x += self.velocidad
            if keys[pygame.K_UP] and self.rect.top > self.velocidad:
                self.rect.y -= self.velocidad
            if keys[pygame.K_DOWN] and self.rect.bottom < H:
                self.rect.y += self.velocidad

    def cambiar_tamano(self, factor):
        # Cambia el tamaño de todas las imágenes según el factor proporcionado
        self.imagenes = [
            pygame.transform.scale(imagen, (int(imagen.get_width() * factor), int(imagen.get_height() * factor)))
            for imagen in self.imagenes
        ]
        # Actualiza la imagen actual y el rectángulo con el nuevo tamaño
        self.image = self.imagenes[self.indice_animacion]
        self.rect = self.image.get_rect(center=self.rect.center)

    def cambiar_tamano_por_valores(self, ancho, alto):
        # Cambia el tamaño de todas las imágenes según el ancho y alto proporcionados
        self.imagenes = [
            pygame.transform.scale(imagen, (ancho, alto))
            for imagen in self.imagenes
        ]
        # Actualiza la imagen actual y el rectángulo con el nuevo tamaño
        self.image = self.imagenes[self.indice_animacion]
        self.rect = self.image.get_rect(center=self.rect.center)

    def perder_oxigeno(self):
        if not self.invulnerable and self.oxigeno > 0:
            self.oxigeno -= 1
            self.invulnerable = True
            self.ultimo_daño = pygame.time.get_ticks()

    def recuperar_oxigeno(self):
        if self.oxigeno < 3:
            self.oxigeno += 1

    def dibujar_tanques_oxigeno(self, pantalla):
        tanque_img = pygame.image.load('imagen/tanqueo1.png')
        for i in range(self.oxigeno):
            pantalla.blit(tanque_img, (10 + (i * 40), 10))

    def actualizar_animacion(self):
        # Cambia de imagen en base a la velocidad de animación
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_frame > self.velocidad_animacion:
            self.indice_animacion = (self.indice_animacion + 1) % len(self.imagenes)
            self.image = self.imagenes[self.indice_animacion]
            self.tiempo_ultimo_frame = tiempo_actual

    def update(self):
        # Actualizar animación y verificar invulnerabilidad
        self.actualizar_animacion()
        
        if self.invulnerable and pygame.time.get_ticks() - self.ultimo_daño > self.tiempo_invulnerable:
            self.invulnerable = False







# --------------------------------------------------------------------------------------------------------------------------





#   Clase LiberarTortuga
class LiberarTortuga(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Cargar las imágenes para la animación
        self.imagenes = [
            pygame.image.load('imagen/tortuga/tortuga1.png'),
            pygame.image.load('imagen/tortuga/tortuga2.png'),
            pygame.image.load('imagen/tortuga/tortuga3.png'),
            pygame.image.load('imagen/tortuga/tortuga4.png'),
            pygame.image.load('imagen/tortuga/tortuga5.png')
        ]
        
        # Cambiar el tamaño de la imagen (por ejemplo, 50x50 píxeles)
        self.imagenes = [pygame.transform.scale(imagen, (150, 120)) for imagen in self.imagenes]
        
        self.image = self.imagenes[0]  # Establecer la imagen inicial
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)

        self.rect.x = x  # Posición inicial
        self.rect.y = y
        self.contador_animacion = 0  # Contador para cambiar entre imágenes
        self.animating = False  # Estado de la animación

    def update(self):
        # Mover hacia la izquierda
        self.rect.x -= 5  # Cambia la dirección a la izquierda

        # Actualizar la animación
        if self.animating:
            self.contador_animacion += 1
            if self.contador_animacion >= len(self.imagenes) * 5:  # Cambiar la imagen cada 5 fotogramas
                self.animating = True  # Detener la animación al completar
                self.contador_animacion = 0  # Reiniciar el contador
            else:
                self.image = self.imagenes[self.contador_animacion // 5]

        # Desactivar el sprite al salir del borde izquierdo de la pantalla
        if self.rect.x < -self.rect.width:  # Si sale del límite izquierdo
            self.kill()  # Elimina el sprite de todos los grupos

    def start_animation(self):
        self.animating = True  # Iniciar la animación
        self.contador_animacion = 0  # Reiniciar el contador de animación






#   Liberar Foca

class LiberarFoca(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Cargar las imágenes para la animación
        self.imagenes = [
            pygame.image.load('imagen/foca/foca2.png'),
            pygame.image.load('imagen/foca/foca3.png'),
            pygame.image.load('imagen/foca/foca4.png')
        ]
        
        # Cambiar el tamaño de la imagen (por ejemplo, 50x50 píxeles)
        self.imagenes = [pygame.transform.scale(imagen, (150, 120)) for imagen in self.imagenes]
        
        self.image = self.imagenes[0]  # Establecer la imagen inicial
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)

        self.rect.x = x  # Posición inicial
        self.rect.y = y
        self.contador_animacion = 0  # Contador para cambiar entre imágenes
        self.animating = False  # Estado de la animación

    def update(self):
        # Mover hacia la izquierda
        self.rect.x -= 5  # Cambia la dirección a la izquierda

        # Actualizar la animación
        if self.animating:
            self.contador_animacion += 1
            if self.contador_animacion >= len(self.imagenes) * 5:  # Cambiar la imagen cada 5 fotogramas
                self.animating = True  # Detener la animación al completar
                self.contador_animacion = 0  # Reiniciar el contador
            else:
                self.image = self.imagenes[self.contador_animacion // 5]

        # Desactivar el sprite al salir del borde izquierdo de la pantalla
        if self.rect.x < -self.rect.width:  # Si sale del límite izquierdo
            self.kill()  # Elimina el sprite de todos los grupos

    def start_animation(self):
        self.animating = True  # Iniciar la animación
        self.contador_animacion = 0  # Reiniciar el contador de animación






#   Liberar Delfin

class LiberarDelfin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Cargar las imágenes para la animación
        self.imagenes = [
            pygame.image.load('imagen/delfin/delfin2.png'),
            pygame.image.load('imagen/delfin/delfin3.png'),
            pygame.image.load('imagen/delfin/delfin4.png')
        ]
        
        # Cambiar el tamaño de la imagen (por ejemplo, 50x50 píxeles)
        self.imagenes = [pygame.transform.scale(imagen, (150, 120)) for imagen in self.imagenes]
        
        self.image = self.imagenes[0]  # Establecer la imagen inicial
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)

        self.rect.x = x  # Posición inicial
        self.rect.y = y
        self.contador_animacion = 0  # Contador para cambiar entre imágenes
        self.animating = False  # Estado de la animación

    def update(self):
        # Mover hacia la izquierda
        self.rect.x -= 5  # Cambia la dirección a la izquierda

        # Actualizar la animación
        if self.animating:
            self.contador_animacion += 1
            if self.contador_animacion >= len(self.imagenes) * 5:  # Cambiar la imagen cada 5 fotogramas
                self.animating = True  # Detener la animación al completar
                self.contador_animacion = 0  # Reiniciar el contador
            else:
                self.image = self.imagenes[self.contador_animacion // 5]

        # Desactivar el sprite al salir del borde izquierdo de la pantalla
        if self.rect.x < -self.rect.width:  # Si sale del límite izquierdo
            self.kill()  # Elimina el sprite de todos los grupos

    def start_animation(self):
        self.animating = True  # Iniciar la animación
        self.contador_animacion = 0  # Reiniciar el contador de animación