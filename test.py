import pygame, sys, os 
from FNivel1 import *  #IMPORTA NIVEL 1 Facil
from FNivel2 import *  #IMPORTA NIVEL 2 Facil
from FNivel3 import *  #IMPORTA NIVEL 3 Facil
from DNivel1 import *  #IMPORTA NIVEL 1 Dificil
from DNivel2 import *  #IMPORTA NIVEL 2 Dificil
from DNivel3 import *  #IMPORTA NIVEL 3 Dificil
from personaje import *
from constantes import *  #IMPORTA CONSTANTES COMO COLORES
from idiomas import *



#INICIALIZA PYGAME Y DEFINE LA PANTALLA
pygame.init()
screen = pygame.display.set_mode((W, H))



#IDIOMA DE INICIO
global current_leng 
current_leng = "es"



#FONDO
background = pygame.image.load("imagenes/fp5.jpg")
about = pygame.image.load("imagenes/cre4.png")

#ACOMODA EL FONDO JUSTO AL MEDIO
aspect_ratio = background.get_width() / background.get_height()
new_height = H
new_width = int(new_height * aspect_ratio)

x = (W - new_width) // 2
y = 0

background = pygame.transform.scale(background, (new_width, new_height))

#IMAGEN DE BUZO DE FONDO
buzo = pygame.image.load("imagenes/bbuzooo.png")
buzo = pygame.transform.scale(buzo, (400,90))

#RELOJ PARA FPS
clock = pygame.time.Clock()




# BOTONES
button_surface = pygame.image.load("imagenes/buttons88.png")
button_surface = pygame.transform.scale(button_surface, (350, 90))
button_surfacee = pygame.image.load("imagenes/buttons88.png")
button_surfacee = pygame.transform.scale(button_surfacee, (300, 95))
buttonlg = pygame.image.load("imagenes/settingsssss.png")
buttonlg = pygame.transform.scale(buttonlg, (120,120))
buttonctl = pygame.image.load("imagenes/ctl3.png")
buttonctl = pygame.transform.scale(buttonctl, (120,120))
buttonesp = pygame.image.load("imagenes/spain.png")
buttonesp = pygame.transform.scale(buttonesp, (200,150))
buttoneng = pygame.image.load("imagenes/uk.png")
buttoneng = pygame.transform.scale(buttoneng, (200,150))


#Imagenes botones
salir = pygame.image.load("imagenes/playicon.png")
salir = pygame.transform.scale(salir, (42 ,42))
playy = pygame.image.load("imagenes/playyy.png")
playy = pygame.transform.scale(playy, (42 ,42))
easyimg = pygame.image.load("imagenes/happyface.png")
easyimg = pygame.transform.scale(easyimg, (45,45))
hardimg = pygame.image.load("imagenes/angryface.png")
hardimg = pygame.transform.scale(hardimg, (45,45))
backimg = pygame.image.load("imagenes/back.png")
backimg = pygame.transform.scale(backimg, (45,45))
creimg = pygame.image.load("imagenes/user.png")
creimg = pygame.transform.scale(creimg, (47,47))
easyone = pygame.image.load("imagenes/tortuga/tortuga1.png")
easyone = pygame.transform.scale(easyone, (55,48))


# Fuentes
buttonfont = pygame.font.Font("fuentes/Springwood Display DEMO.otf", 40)
titlefontt = pygame.font.Font("fuentes/Kid Games.ttf", 120)
titlefont = pygame.font.Font("fuentes/Cosplay Culture.ttf", 100)
ttfont = pygame.font.Font("fuentes/Cosplay Culture.ttf", 140)
subfont = pygame.font.SysFont("themevck_text", 20)




#SUPERFIICIES DE TEXTO
titletext = titlefontt.render("SEA", True, NARANJA)
tttext = ttfont.render("ADVENTURE", True, AZULL)
difftext = titlefont.render("DIFICULTAD", True, AMARILLO)
levelstext = titlefont.render("NIVELES", True, LIGHT_BLUE)
lengtext = titlefont.render("IDIOMAS", True, BLANCO)
abouttext = titlefont.render("CREDITOS", True, BLANCO)
ctltext = titlefont.render("Controles", True, BLANCO)
overtext = titlefont.render("GAME OVER", True, BLANCO)





#MUSICA DE FONDO
pygame.mixer.music.load("sonidos/adventure.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.25)
 
#SONIDO DE BOTONES
click_sound = pygame.mixer.Sound('sonidos/clickss.mp3')







# Clase Button
class Button:
    def __init__(self, image, pos, text_input='', font=None, base_color=(255, 255, 255), hovering_color=(200, 200, 200), 
                 escala=1.2, draw_border=False, text_offset_x=25, additional_image=None):
        self.image = image
        self.x_pos, self.y_pos = pos
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.escala = escala
        self.draw_border = draw_border
        self.is_hovered = False
        self.is_selected = False
        self.text_offset_x = text_offset_x
        self.additional_image = additional_image

        if self.font:
            self.text = self.font.render(self.text_input, True, self.base_color)
        else:
            self.text = None

        if self.image is None:
            self.image = self.text

        self.anchoo, self.altoo = self.image.get_size()
        self.tamañoi = (self.anchoo, self.altoo)
        self.tamañoa = (int(self.anchoo * self.escala), int(self.altoo * self.escala))
        self.rect = pygame.Rect(self.x_pos - self.anchoo // 2, self.y_pos - self.altoo // 2, self.anchoo, self.altoo)
        self.text_rect = self.text.get_rect(center=(self.x_pos - self.text_offset_x, self.y_pos)) if self.text else None


        if self.additional_image:
            self.original_additional_image_size = self.additional_image.get_size()


    def update(self, screen):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.check_hover((mouse_x, mouse_y))

        if self.rect.collidepoint((mouse_x, mouse_y)):
            imagea = pygame.transform.scale(self.image, self.tamañoa)
            recta = pygame.Rect(self.x_pos - self.tamañoa[0] // 2, self.y_pos - self.tamañoa[1] // 2, *self.tamañoa)
            text_color = self.hovering_color

            if self.additional_image:
                # Escala basada en el tamaño del botón en estado hover
                scale_factor = self.escala
                additional_image_scaled_size = (int(self.original_additional_image_size[0] * scale_factor), 
                                                 int(self.original_additional_image_size[1] * scale_factor))
                additional_image_scaled = pygame.transform.scale(self.additional_image, additional_image_scaled_size)
        
        
        else:
            imagea = pygame.transform.scale(self.image, self.tamañoi)
            recta = pygame.Rect(self.x_pos - self.anchoo // 2, self.y_pos - self.altoo // 2, self.anchoo, self.altoo)
            text_color = self.base_color

            if self.additional_image:
                additional_image_scaled_size = (int(self.original_additional_image_size[0] * (1 / self.escala)), 
                                                 int(self.original_additional_image_size[1] * (1 / self.escala)))
                additional_image_scaled = pygame.transform.scale(self.additional_image, additional_image_scaled_size)


        # Dibuja la imagen del botón
        screen.blit(imagea, recta.topleft)

        # Dibuja el borde si está configurado para dibujarlo y está seleccionado
        if self.draw_border and (self.is_selected or self.is_hovered):
            pygame.draw.rect(screen, (LIMA) , recta, 7)  # Borde rojo de 3 píxeles

        # Dibuja el texto del botón si se proporciona
        if self.text:
            self.text = self.font.render(self.text_input, True, text_color)
            self.text_rect = self.text.get_rect(center=(self.x_pos - self.text_offset_x, self.y_pos))  # Actualiza el rectángulo del texto
            screen.blit(self.text, self.text_rect)

        if self.additional_image:
            additional_image_pos = (self.text_rect.right + 10, self.y_pos - additional_image_scaled.get_height() // 2)  # 10 píxeles de separación
            screen.blit(additional_image_scaled, additional_image_pos)

    def checkForInput(self, position):
        if self.rect.collidepoint(position):
            click_sound.play()
            return True 
        return False
    
    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def set_selected(self, selected):
        self.is_selected = selected

    






#Pantalla Idioma
def lenscreen():
    
    while True:
        global current_leng

        LEN_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(background, (x,y))
        screen.blit(lengtext, (425, 30))

        espbutton = Button(image=buttonesp, pos=(450, 250), text_input="",
                           font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE, draw_border=True )
        engbutton = Button(image=buttoneng, pos=(750, 250), text_input="",
                           font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE, draw_border=True)
        aboutbutton = Button(image=button_surface, pos=(600, 400), text_input="Crèditos", additional_image=creimg,
                             font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE)
        diffback_button = Button(image=button_surface, pos=(600, 500), text_input="Regresar", additional_image=backimg,
                                  font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE)
        
        
        for button in [espbutton, engbutton, aboutbutton, diffback_button]: 
            if button in [espbutton, engbutton]:
                button.set_selected((button == espbutton and current_leng == 'es') or
                                    (button == engbutton and current_leng == 'en'))
            else:
                button.set_selected(False)

            button.update(screen)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if espbutton.checkForInput(LEN_MOUSE_POS):
                    current_leng = 'es'
                if engbutton.checkForInput(LEN_MOUSE_POS):
                    current_leng = 'en'
                if aboutbutton.checkForInput(LEN_MOUSE_POS):
                    aboutscreen()
                if diffback_button.checkForInput(LEN_MOUSE_POS):
                    menu()

        pygame.display.update()





def ctlscreen():

    #IMAGEN DE CONTROLES
    controles = pygame.image.load("imagenes/control.jpg")
    controles = pygame.transform.scale(controles, (1200, 600))

    while True:
        CTL_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill(AZUL)
        screen.blit(controles, (0,0))

        mainback_button = Button(image=button_surface, pos=(600, 550), text_input="Regresar", additional_image=backimg,
                                  font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE)
        
        mainback_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  mainback_button.checkForInput(CTL_MOUSE_POS):
                    menu()


        pygame.display.update()


def aboutscreen():
    while True:
        ABOUT_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(about, (0, 0))

        aboutback_button = Button(image=button_surface, pos=(600, 520), text_input="Regresar", additional_image=backimg,
                                  font=buttonfont, base_color=BLANCO, hovering_color=AMARILLO)

        aboutback_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if aboutback_button.checkForInput(ABOUT_MOUSE_POS):
                    lenscreen()

        pygame.display.update()






# Pantalla de dificultad
def diffscreen():
    while True:
        DIFF_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(background, (x, y))
        screen.blit(difftext, (390, 70))

        easybutton = Button(image=button_surface, pos=(600, 250), text_input="Principiante", additional_image=easyimg,
                             font=buttonfont, base_color=BLANCO, hovering_color=AMARILLO)
        hardbutton = Button(image=button_surface, pos=(600, 350), text_input="Avanzado", additional_image=hardimg,
                             font=buttonfont, base_color=BLANCO, hovering_color=AMARILLO)
        diffback_button = Button(image=button_surface, pos=(600, 450), text_input="Regresar", additional_image=backimg,
                                  font=buttonfont, base_color=BLANCO, hovering_color=AMARILLO)
        controlbutton = Button(image=buttonctl, pos=(100, 500), text_input="",
                               font=buttonfont, base_color=BLANCO, hovering_color=AMARILLO)

        for button in [easybutton, hardbutton, diffback_button, controlbutton]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easybutton.checkForInput(DIFF_MOUSE_POS):
                    easyscreen()
                if hardbutton.checkForInput(DIFF_MOUSE_POS):
                    hardscreen()
                if diffback_button.checkForInput(DIFF_MOUSE_POS):
                    menu()
                if controlbutton.checkForInput(DIFF_MOUSE_POS):
                    ctlscreen()

        pygame.display.update()




# Pantalla de niveles principiante
def easyscreen():

    global current_leng

    while True:
        EASY_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(background, (x, y))
        screen.blit(levelstext, (435, 30))

        onelevel = Button(image=button_surface, pos=(600, 210), text_input="Nivel 1", additional_image=easyone,
                              font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE)
        twolevel = Button(image=button_surface, pos=(600,310), text_input="Nivel 2",
                              font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE)
        threelevel = Button(image=button_surface, pos=(600,410), text_input="Nivel 3",
                                font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE)
        levelback_button = Button(image=button_surface, pos=(600, 510), text_input="Regresar", additional_image=backimg,
                                  font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE)
        controlbutton = Button(image=buttonctl, pos=(100, 510), text_input="",
                               font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE)
        
        for button in [onelevel, twolevel, threelevel, levelback_button, controlbutton]:
            button.update(screen)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if onelevel.checkForInput(EASY_MOUSE_POS):
                    easy1()
                if twolevel.checkForInput(EASY_MOUSE_POS):
                    easy2()
                if threelevel.checkForInput(EASY_MOUSE_POS):
                    easy3()
                if levelback_button.checkForInput(EASY_MOUSE_POS):
                    diffscreen()
                if controlbutton.checkForInput(EASY_MOUSE_POS):
                    print("control")

        pygame.display.update()




#Pantalla de niveles avanzado
def  hardscreen():
    global current_leng

    while True:
        HARD_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(background, (x,y))
        screen.blit(levelstext, (435, 30))

        onelevel = Button(image=button_surface, pos=(600, 210), text_input="Nivel 1",
                              font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE)
        twolevel = Button(image=button_surface, pos=(600,310), text_input="Nivel 2",
                              font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE)
        threelevel = Button(image=button_surface, pos=(600,410), text_input="Nivel 3",
                                font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE)
        levelback_button = Button(image=button_surface, pos=(600, 510), text_input="Regresar", additional_image=backimg,
                                  font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE)
        controlbutton = Button(image=buttonctl, pos=(100, 510), text_input="",
                               font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE)
        
        for button in [onelevel, twolevel, threelevel, levelback_button, controlbutton]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if onelevel.checkForInput(HARD_MOUSE_POS):
                    hard1()
                if twolevel.checkForInput(HARD_MOUSE_POS):
                    hard2()
                if threelevel.checkForInput(HARD_MOUSE_POS):
                    hard3()
                if levelback_button.checkForInput(HARD_MOUSE_POS):
                    diffscreen()
                if controlbutton.checkForInput(HARD_MOUSE_POS):
                    print("control")

        pygame.display.update()


# Menú principal
def menu():

    global current_leng

    while True:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                MENU_MOUSE_POS = pygame.mouse.get_pos()
                if playbutton.checkForInput(MENU_MOUSE_POS):
                    diffscreen()
                if lenguagebutton.checkForInput(MENU_MOUSE_POS):
                    lenscreen()
                if controlbutton.checkForInput(MENU_MOUSE_POS):
                    ctlscreen()
                if quitbutton.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        # Actualiza el cuadro actual
        playbutton = Button(image=button_surfacee, pos=(940, 260), text_input=textos[current_leng]["Jugar"], additional_image=playy,
                            font=buttonfont, base_color=BLANCO, hovering_color=NARANJA)
        quitbutton = Button(image=button_surfacee, pos=(940, 365), text_input=textos[current_leng]["Salir"], additional_image=salir,
                            font=buttonfont, base_color=BLANCO, hovering_color=NARANJA)
        lenguagebutton = Button(image=buttonlg, pos=(1100, 500), text_input="",
                                font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE)
        controlbutton = Button(image=buttonctl, pos=(100, 500), text_input="",
                            font=buttonfont, base_color=BLANCO, hovering_color=NAVY_BLUE)

        # Dibuja el fondo (GIF)
        screen.blit(background, (0,0))

        # Dibuja otros elementos
        screen.blit(titletext, (110, 180))
        screen.blit(tttext, (100, 250))
        screen.blit(buzo, (310, 170))

        # Actualiza los botones
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        playbutton.update(screen)
        quitbutton.update(screen)
        lenguagebutton.update(screen)
        controlbutton.update(screen)

        # Actualiza la pantalla
        pygame.display.update()
        clock.tick(30)  # Limita el FPS a 60




menu()
