#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, warrior
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.font.init()
ele=pygame.mixer.Sound("sonidos/Lift.wav")
ent=pygame.mixer.Sound("sonidos/Weappick.wav")
fon=pygame.mixer.Sound("sonidos/Menumus.ogg")
class Menu:
    fon.play(-1)
    def __init__(self, opciones):
        self.opciones = opciones
        self.font = pygame.font.Font('fuentes/Pretendo.ttf', 60)
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        k = pygame.key.get_pressed()
        
        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
                ele.play()
            elif k[K_DOWN]:
                self.seleccionado += 1
                ele.play()
            elif k[K_RETURN]:
                ent.play()
                titulo, funcion = self.opciones[self.seleccionado]
                funcion()
                
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]


    def imprimir(self, screen):
        total = self.total
        indice = 0
        altura_de_opcion = 75
        x = 100
        y = 180
        
        for (titulo, funcion) in self.opciones:
            if indice == self.seleccionado:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)

            imagen = self.font.render(titulo, 1, color)
            posicion = (x, y + altura_de_opcion * indice)
            indice += 1
            screen.blit(imagen, posicion)


def comenzar_nuevo_juego():
    fuente   = pygame.font.Font('fuentes/zrnic___.ttf', 20)
    pant = pygame.display.set_mode((800,600))
    Intro=True
    elec=0
    FonInt=0
    Fondo=None
    fuente1 = fuente.render("Enter - Continuar. B - Volver atras", 1, (255,255,255))
    fuentep = fuente1
    while Intro:
        for k in pygame.event.get():
            if k.type == pygame.QUIT:
                fon.stop()
                Intro=False
            if k.type == pygame.KEYDOWN:
                if k.key == pygame.K_RETURN:
                    ent.play()
                    if FonInt==0:
                        FonInt=1
                    elif FonInt==1:
                        FonInt=2
                if k.key == pygame.K_b:
                    if FonInt==0:
                        salir = True
                        opciones = [("Jugar", comenzar_nuevo_juego),
                                    ("Instrucciones", instrucciones),
                                    ("Mejor Puntaje", best_score),
                                    ("Salir", salir_del_programa)]
                        fondo = pygame.image.load("imagenes/Backg.jpg")
                        menu = Menu(opciones)
                        while salir:
                            for e in pygame.event.get():
                                if e.type == QUIT:
                                    salir = False
                                    fon.stop()
                                    import sys
                                    pygame.quit()
                                    sys.exit(0)

                            screen.blit(fondo, (0, 0))
                            menu.actualizar()
                            menu.imprimir(screen)

                            pygame.display.flip()
                    elif FonInt==1:
                        FonInt=0
                    elif FonInt==2:
                        FonInt=1
                        fuentep=fuente1
            if FonInt==0:
                Fondo="imagenes/Prologo1.png"
            elif FonInt==1:
                Fondo="imagenes/Prologo1.2.jpg"
            elif FonInt==2:
                Intro=False
            Hist=pygame.image.load(Fondo)
            pant.blit(Hist, [0, 0])
            pant.blit(fuentep, (10,550))
            pygame.display.flip()
    fon.stop()
    warrior.main()
    fon.play()

def instrucciones():
    fuente = pygame.font.Font("fuentes/zrnic___.ttf", 20)
    pant = pygame.display.set_mode((800, 600))
    instrucciones = pygame.image.load("imagenes/instrucciones.jpg")
    fuente1 = fuente.render("Presione b para volver al menu", 1, (255,255,255))
    Salir = False
    while not Salir:
        k = pygame.key.get_pressed()        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Salir = True            
        if k[K_b]:
            Salir = True
            
        pant.blit(instrucciones, [0, 0])
        pant.blit(fuente1, (10,550))
        pygame.display.flip()

def best_score():
    fuente   = pygame.font.Font("fuentes/zrnic___.ttf", 24)
    fuenteal = pygame.font.Font("fuentes/zrnic___.ttf", 20)
    pant = pygame.display.set_mode((800, 600))
    best_score = pygame.image.load("imagenes/b_menu.jpg")
    f_score = open("data/puntaje.txt", "r")
    fuente1 = fuenteal.render("Presione b para volver al menu", 1, (255,255,255))
    fuenter = fuente1.get_rect()
    texto_x = 640/2
    texto_y = 380/2
    Exit = False
    
    for li in f_score:
        p = fuente.render(li, True, (255, 255, 255))

    while not Exit:
        k = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit = True

            if k[K_b]:
                Exit = True
        pant.blit(best_score, (0, 0))
        pant.blit(p,[texto_x,texto_y])
        pant.blit(fuente1, (10,550))
        pygame.display.flip()
        
        f_score.close()

def salir_del_programa():
    fon.stop()
    import sys
    pygame.quit()
    sys.exit(0)


if __name__ == '__main__':

    salir = False
    opciones = [
        ("Jugar", comenzar_nuevo_juego),
        ("Instrucciones", instrucciones),
        #("MejoR Puntaje", best_score),
        ("Salir", salir_del_programa)
        ]
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("The Warrior: Ultimo Intento")
    fondo = pygame.image.load("imagenes/warr.png")
    fondo = pygame.transform.scale(fondo,(800,600))
    menu = Menu(opciones)

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True
                fon.stop()
                import sys
                pygame.quit()
                sys.exit(0)

        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)
