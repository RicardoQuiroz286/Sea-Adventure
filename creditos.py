import pygame
import sys
import cv2


def reproducir_video():
    # Inicializa pygame y el mixer
    pygame.init()
    pygame.mixer.init()

    clock = pygame.time.Clock()

    global musica_silenciada  # Asegúrate de que la variable sea global si es necesario
    # Silenciar la música de fondo
    pygame.mixer.music.set_volume(0)
    
    # Lógica para reproducir el video (asegúrate de tener la implementación del video)
    # video.play() o similar aquí (si estás usando alguna librería de video)

    # Después de reproducir el video, restaurar el volumen
    musica_silenciada = False  # O cualquier bandera que utilices
    
    # Configura la pantalla
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption('Video con Sonido')

    # Cargar el sonido desde la ruta proporcionada
    sound = pygame.mixer.Sound('imagen/fondo/Musica_creditos.wav')

    # Reproduce el sonido
    sound.play()

    # Cargar el video usando OpenCV desde la ruta proporcionada
    cap = cv2.VideoCapture('imagenes/credits.mp4')

    # Asegúrate de que el video se haya cargado correctamente
    if not cap.isOpened():
        print("Error al abrir el video")
        sys.exit()

    # Obtener las dimensiones del video
    video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Calcular la posición para centrar el video
    center_x = (1200 - video_width) // 2
    center_y = (600 - video_height) // 2

    # Bucle principal del juego
    running = True
    while running:
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Comprobar si se presionan las teclas Espacio o Enter
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    running = False

        # Leer frame por frame del video
        ret, frame = cap.read()
        if not ret:
            break  # Si no hay más frames, termina el bucle

        frame = cv2.flip(frame, 1)
        
        # Rotar el frame 90 grados en sentido antihorario
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # Convertir el frame de BGR (OpenCV) a RGB (Pygame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convertir a superficie de Pygame
        frame_surface = pygame.surfarray.make_surface(frame)


        # Mostrar el frame centrado en la pantalla
        screen.fill((0, 0, 0))  # Limpiar pantalla con color negro
        screen.blit(frame_surface, (center_x, center_y))

        clock.tick(20)


        # Actualizar la pantalla
        pygame.display.update()

    # Liberar el video y cerrar Pygame
    cap.release()

    return True

def reproducir_videoo():
    # Inicializa pygame y el mixer
    pygame.init()
    pygame.mixer.init()

    clock = pygame.time.Clock()

    global musica_silenciada  # Asegúrate de que la variable sea global si es necesario
    # Silenciar la música de fondo
    pygame.mixer.music.set_volume(0)
    
    # Lógica para reproducir el video (asegúrate de tener la implementación del video)
    # video.play() o similar aquí (si estás usando alguna librería de video)

    # Después de reproducir el video, restaurar el volumen
    musica_silenciada = False  # O cualquier bandera que utilices
    
    # Configura la pantalla
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption('Video con Sonido')

    # Cargar el sonido desde la ruta proporcionada
    sound = pygame.mixer.Sound('imagen/fondo/Musica_creditos.wav')

    # Reproduce el sonido
    sound.play()

    # Cargar el video usando OpenCV desde la ruta proporcionada
    cap = cv2.VideoCapture('imagenes/credit.mp4')

    # Asegúrate de que el video se haya cargado correctamente
    if not cap.isOpened():
        print("Error al abrir el video")
        sys.exit()

    # Obtener las dimensiones del video
    video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Calcular la posición para centrar el video
    center_x = (1200 - video_width) // 2
    center_y = (600 - video_height) // 2

    # Bucle principal del juego
    running = True
    while running:
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Comprobar si se presionan las teclas Espacio o Enter
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    running = False

        # Leer frame por frame del video
        ret, frame = cap.read()
        if not ret:
            break  # Si no hay más frames, termina el bucle

        frame = cv2.flip(frame, 1)

        # Rotar el frame 90 grados en sentido antihorario
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # Convertir el frame de BGR (OpenCV) a RGB (Pygame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convertir a superficie de Pygame
        frame_surface = pygame.surfarray.make_surface(frame)

        # Mostrar el frame centrado en la pantalla
        screen.blit(frame_surface, (center_x, center_y))

        clock.tick(20)

        # Actualizar la pantalla
        pygame.display.update()

    # Liberar el video y cerrar Pygame
    cap.release()

    return True