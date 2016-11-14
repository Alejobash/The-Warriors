#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, random, Jefe
from pygame.locals import *

ROJO=[255,0,0]
AZUL=[0,0,255]
VERDE=[0,255,0]
AMARILLO=[255,255,0]
GRIS=[128,128,128]
NEGRO=[0,0,0]
Alto=600
Ancho=800
pygame.init()
reloj = pygame.time.Clock()

Fontrans=pygame.image.load("imagenes/01.jpg")
Fontrans1=pygame.image.load("imagenes/11.jpg")
Fontrans2=pygame.image.load("imagenes/3.jpg")
Fontrans3=pygame.image.load("imagenes/nube.jpg")
Fontrans4=pygame.image.load("imagenes/nuv.png")


class Jugador(pygame.sprite.Sprite):
    velx=0
    vely=0
    sprite=0
    spritej=0

    nivel=None

    def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.stand     = pygame.image.load("imagenes/guystatic.png")
                self.run       = pygame.image.load("imagenes/guyrun1.png")
                self.run2      = pygame.image.load("imagenes/guyrun2.png")
                self.run3      = pygame.image.load("imagenes/guyrun3.png")
                self.run4      = pygame.image.load("imagenes/guyrun4.png")
                self.run5      = pygame.image.load("imagenes/guyrun5.png")
                self.run6      = pygame.image.load("imagenes/guyrun6.png")
                self.run7      = pygame.image.load("imagenes/guyrun7.png")
                self.run8      = pygame.image.load("imagenes/guyrun8.png")
                self.run9      = pygame.image.load("imagenes/guyrun9.png")
                self.jump      = pygame.image.load("imagenes/guyjump1.png")
                self.jump2     = pygame.image.load("imagenes/guyjump2.png")
                self.jump3     = pygame.image.load("imagenes/guyjump3.png")
                self.jump4     = pygame.image.load("imagenes/guyjump4.png")
                self.standi    = pygame.image.load("imagenes/guystatici.png")
                self.runi      = pygame.image.load("imagenes/guyrun1i.png")
                self.run2i     = pygame.image.load("imagenes/guyrun2i.png")
                self.run3i     = pygame.image.load("imagenes/guyrun3i.png")
                self.run4i     = pygame.image.load("imagenes/guyrun4i.png")
                self.run5i     = pygame.image.load("imagenes/guyrun5i.png")
                self.run6i     = pygame.image.load("imagenes/guyrun6i.png")
                self.run7i     = pygame.image.load("imagenes/guyrun7i.png")
                self.run8i     = pygame.image.load("imagenes/guyrun8i.png")
                self.run9i     = pygame.image.load("imagenes/guyrun9i.png")
                self.jumpi     = pygame.image.load("imagenes/guyjump1i.png")
                self.jump2i    = pygame.image.load("imagenes/guyjump2i.png")
                self.jump3i    = pygame.image.load("imagenes/guyjump3i.png")
                self.jump4i    = pygame.image.load("imagenes/guyjump4i.png")
                self.fire      = pygame.image.load("imagenes/guyfiring.png")
                self.firei     = pygame.image.load("imagenes/guyfiringi.png")
                self.jumpfire  = pygame.image.load("imagenes/guyjumpfiring.png")
                self.jumpfirei = pygame.image.load("imagenes/guyjumpfiringi.png")
                self.firebfg   = pygame.image.load("imagenes/guyfiringbfg.png")
                self.fireibfg  = pygame.image.load("imagenes/guyfiringbfgi.png")
                self.jumpfirebfg= pygame.image.load("imagenes/guyjumpfiringbfg.png")
                self.jumpfireibfg= pygame.image.load("imagenes/guyjumpfiringbfgi.png")
                
                self.first     = [self.stand, self.run, self.run2, self.run3,
                                  self.run4, self.run5, self.run6, self.run7,
                                  self.run8, self.run9, self.jump, self.jump2,
                                  self.jump3, self.jump4, self.standi, self.runi,
                                  self.run2i, self.run3i, self.run4i, self.run5i,
                                  self.run6i, self.run7i, self.run8i, self.run9i,
                                  self.jumpi, self.jump2i, self.jump3i, self.jump4i,
                                  self.fire, self.firei, self.jumpfire, self.jumpfirei,
                                  self.firebfg, self.fireibfg, self.jumpfirebfg, self.jumpfireibfg]
                #0,14: Stand. 1-9,15-23: Walk. 10-13, 24-27: Jump.
                #28,29: Firing(Plasma). 30,31: Firing while jumping(Plasma).
                #32,33: Firing(BFG). 34,35: Firing while jumping(BFG).
                self.image     = self.first[0]
                self.rect      = self.image.get_rect()
                self.dir       = 0
                self.isjump    = 0
                self.isfiring  = 0
                self.bullets   = 70
                self.isrun     = 0
                self.vidas     = 70

    def update(self):

        self.calc_grav()

        self.rect.x+=self.velx

        bloque_col_list=pygame.sprite.spritecollide(self,self.nivel.plataforma_lista,False)
        for bloque in bloque_col_list:
            
            if self.velx>0:
                self.rect.right=bloque.rect.left
            elif self.velx<0:
                self.rect.left=bloque.rect.right

        self.rect.y+=self.vely

        bloque_col_list=pygame.sprite.spritecollide(self,self.nivel.plataforma_lista,False)
        for bloque in bloque_col_list:
            if self.vely>0:
                self.rect.bottom=bloque.rect.top
                
            elif self.vely<0:
                self.rect.top=bloque.rect.bottom

            self.vely=0
            self.isjump=0

    def calc_grav(self):
        if self.vely==0:
                self.vely=1
                if self.isfiring==0:
                    if self.isrun==0:
                        if self.dir==0:
                            self.image=self.first[0]
                            sprite=0
                            spritej=0
                        elif self.dir==1:
                            self.image=self.first[14]
                            sprite=0
                            spritej=0
                    elif self.isrun==1:
                        if self.dir==0:
                            if self.sprite==0:
                                pygame.time.delay(10)
                                self.image=self.first[1]
                                self.sprite=1
                            elif self.sprite==1:
                                pygame.time.delay(10)
                                self.image=self.first[2]
                                self.sprite=2
                            elif self.sprite==2:
                                self.image=self.first[3]
                                self.sprite=3
                            elif self.sprite==3:
                                self.image=self.first[4]
                                self.sprite=4
                            elif self.sprite==4:
                                self.image=self.first[5]
                                self.sprite=5
                            elif self.sprite==5:
                                self.image=self.first[6]
                                self.sprite=6
                            elif self.sprite==6:
                                self.image=self.first[7]
                                self.sprite=7
                            elif self.sprite==7:
                                self.image=self.first[8]
                                self.sprite=8
                            elif self.sprite==8:
                                self.image=self.first[9]
                                self.sprite=0
                        elif self.dir==1:
                            if self.sprite==0:
                                self.image=self.first[15]
                                self.sprite=1
                            elif self.sprite==1:
                                self.image=self.first[16]
                                self.sprite=2
                            elif self.sprite==2:
                                self.image=self.first[17]
                                self.sprite=3
                            elif self.sprite==3:
                                self.image=self.first[18]
                                self.sprite=4
                            elif self.sprite==4:
                                self.image=self.first[19]
                                self.sprite=5
                            elif self.sprite==5:
                                self.image=self.first[20]
                                self.sprite=6
                            elif self.sprite==6:
                                self.image=self.first[21]
                                self.sprite=7
                            elif self.sprite==7:
                                self.image=self.first[22]
                                self.sprite=8
                            elif self.sprite==8:
                                self.image=self.first[23]
                                self.sprite=0
                elif self.isfiring==1:
                    if self.dir==0:
                        self.image=self.first[28]
                    else:
                        self.image=self.first[29]
                else:
                    if self.dir==0:
                        self.image=self.first[32]
                    else:
                        self.image=self.first[33]
        else:
            self.vely+=.35
            if self.isfiring==0:
                if self.dir==0:
                    if self.spritej==0:
                        self.image=self.first[10]
                        self.spritej=1
                    elif self.spritej==1:
                        self.image=self.first[11]
                        self.spritej=2
                    elif self.spritej==2:
                        self.image=self.first[12]
                        self.spritej=3
                    elif self.spritej==3:
                        self.image=self.first[13]
                elif self.dir==1:
                    if self.spritej==0:
                        self.image=self.first[24]
                        self.spritej=1
                    elif self.spritej==1:
                        self.image=self.first[25]
                        self.spritej=2
                    elif self.spritej==2:
                        self.image=self.first[26]
                        self.spritej=3
                    elif self.spritej==3:
                        self.image=self.first[27]
            elif self.isfiring==1:
                if self.dir==0:
                    self.image=self.first[30]
                else:
                    self.image=self.first[31]
            else:
                if self.dir==0:
                    self.image=self.first[34]
                else:
                    self.image=self.first[35]
                

        if self.rect.y >= Alto - self.rect.height and self.vely >= 0:
            self.vely = 0
            self.rect.y = Alto - self.rect.height

    def salto(self,pantalla):
        self.rect.y += 2
        plataforma_col_lista=pygame.sprite.spritecollide(self,self.nivel.plataforma_lista,False)
        self.rect.y -= 2
        pantalla.blit(self.image, self.rect)
        if len(plataforma_col_lista) > 0 or self.rect.bottom >= Alto:
            self.isjump=1
            self.vely= -12
        
    def ir_izq(self,pantalla):
        self.velx=-6
        self.dir=1
        if self.isjump==0:
            if self.isrun==1:
                self.image=self.first[7]
        pantalla.blit(self.image, self.rect)

    def ir_der(self,pantalla):
        self.velx=6
        self.dir=0
        if self.isjump==0:
            if self.isrun==1:
                self.image=self.first[2]
        pantalla.blit(self.image, self.rect)

    def no_mover(self,pantalla):
        self.velx=0
        if self.isjump==0:
            if self.isfiring==0:
                if self.dir==0:
                    self.image=self.first[0]
                elif self.dir==1:
                    self.image=self.first[14]
            else:
                if self.dir==0:
                    self.image=self.first[28]
                else:
                    self.image=self.first[29]
        pantalla.blit(self.image, self.rect)

    def disparo(self,pantalla):
        if self.isjump==0:
            if self.dir==0:
                self.image=self.first[28]
            else:
                self.image=self.first[29]
        else:
            if self.dir==0:
                self.image=self.first[30]
            else:
                self.image=self.first[31]
        pantalla.blit(self.image, self.rect)

class Vidas():

    def __init__(self,nvidas, pantalla):
        self.alto=3
        self.ancho=10
        self.sep=0
        self.vidas=nvidas
        self.color=ROJO
        self.pos_x=50
        self.pos_yini=280
        self.pos_y=self.pos_yini-(nvidas*(self.alto+self.sep))
        pygame.draw.rect(pantalla,self.color,[self.pos_y,self.pos_x, self.alto,self.ancho])

class Poder():

    def __init__(self,nbal, pantalla):
        self.alto=3
        self.ancho=10
        self.sep=0
        self.vidas=nbal
        self.color=VERDE
        self.pos_x=70
        self.pos_yini=280
        self.pos_y=self.pos_yini-(nbal*(self.alto+self.sep))
        pygame.draw.rect(pantalla,self.color,[self.pos_y,self.pos_x,self.alto, self.ancho])


class Plataforma(pygame.sprite.Sprite):

    def __init__(self,ancho,alto):
        self.Anc=ancho
        self.Alt=alto
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([self.Anc,self.Alt])
        self.rect=self.image.get_rect()
        self.color1=GRIS
        self.image.fill(self.color1)

class Balas (pygame.sprite.Sprite):

        def __init__(self, posx, posy,tipo,dire):
                pygame.sprite.Sprite.__init__(self)
                self.tipo  = tipo
                self.dir   = dire
                self.sprite= 0
                if self.tipo ==0:
                    self.image = pygame.image.load("imagenes/BFGshot1.png")
                    self.vel   =  5
                    self.rect  = self.image.get_rect()
                    self.rect.x = posx + 25
                    self.rect.y = posy + 10
                if self.tipo == 1:
                    self.image = pygame.image.load("imagenes/plasma.png")
                    self.vel   =  12
                    self.rect  = self.image.get_rect()
                    self.rect.x = posx+25
                    self.rect.y = posy+12
                if self.tipo == 2:
                    self.image = pygame.image.load("imagenes/Cacoball.png")
                    self.vel   =  10
                    self.rect  = self.image.get_rect()
                    self.rect.x = posx
                    self.rect.y = posy+34

        def derecha(self, superficie):
            if self.tipo==0:
                if self.sprite==0:
                    self.image = pygame.image.load("imagenes/BFGshot1.png")
                    self.sprite=1
                elif self.sprite==1:
                    self.image = pygame.image.load("imagenes/BFGshot2.png")
                    self.sprite=0
            elif self.tipo==1:
                if self.sprite==0:
                    self.image = pygame.image.load("imagenes/plasma.png")
                    self.sprite=1
                elif self.sprite==1:
                    self.image = pygame.image.load("imagenes/plasma2.png")
                    self.sprite=0
            elif self.tipo==2:
                if self.sprite==0:
                    self.image = pygame.image.load("imagenes/Cacoball.png")
                    self.sprite=1
                elif self.sprite==1:
                    self.image = pygame.image.load("imagenes/Cacoball2.png")
                    self.sprite=0
            if self.dir==0:
                self.rect.x = self.rect.x + self.vel
                superficie.blit(self.image, self.rect)
            else:
                self.rect.x = self.rect.x - self.vel
                superficie.blit(self.image, self.rect)

class Enemigo (pygame.sprite.Sprite):
        sprite=0


        def __init__(self, posx, posy, typee):
                pygame.sprite.Sprite.__init__(self)
                self.tipo   = typee
                self.vidas  = 0
                self.pasos  = 0
                self.lanzar = 0
                if self.tipo == 1:
                    self.image = pygame.image.load("imagenes/Cacodemon1.png")
                    self.vidas  = random.randint(5,7)
                    self.lanzar = random.randint(50,150)
                    self.vel    = 2
                elif self.tipo == 2:
                    self.image  = pygame.image.load("imagenes/Rocket1.png")
                    self.vidas  = 1
                    self.vel    = random.randint(5,10)
                elif self.tipo == 3:
                    self.image  = pygame.image.load("imagenes/Painelem4.png")
                    self.vidas  = random.randint(2,4)
                    self.lanzar = random.randint(150,250)
                    self.vel    = 2
                elif self.tipo == 4:
                    self.image = pygame.image.load("imagenes/Lostsoul1i.png")
                    self.vel   =  11
                    self.vidas = 1
                self.rect   = self.image.get_rect()
                if self.tipo==4:
                    self.rect.x = posx
                    self.rect.y = posy+30
                else:
                    self.rect.x = posx
                    self.rect.y = posy

        def izquierda(self, superficie, pospl, velpl):
            if self.tipo==1:
                if self.sprite ==0:
                    self.image  = pygame.image.load("imagenes/Cacodemon1.png")
                    self.sprite=1
                elif self.sprite ==1:
                    self.image  = pygame.image.load("imagenes/Cacodemon2.png")
                    self.sprite=2
                elif self.sprite ==2:
                    self.image  = pygame.image.load("imagenes/Cacodemon3.png")
                    self.sprite=3
                elif self.sprite ==3:
                    self.image  = pygame.image.load("imagenes/Cacodemon4.png")
                    self.sprite=4
                elif self.sprite ==4:
                    self.image  = pygame.image.load("imagenes/Cacodemon5.png")
                    self.sprite=5
                elif self.sprite ==5:
                    self.image  = pygame.image.load("imagenes/Cacodemon6.png")
                    self.sprite=6
                elif self.sprite ==6:
                    self.image  = pygame.image.load("imagenes/Cacodemon7.png")
                    self.sprite=0
                self.rect.x = self.rect.x - self.vel
            elif self.tipo==2:
                if self.sprite ==0:
                    self.image  = pygame.image.load("imagenes/Rocket1.png")
                    self.sprite=1
                elif self.sprite ==1:
                    self.image  = pygame.image.load("imagenes/Rocket2.png")
                    self.sprite=2
                elif self.sprite ==2:
                    self.image  = pygame.image.load("imagenes/Rocket3.png")
                    self.sprite=3
                elif self.sprite ==3:
                    self.image  = pygame.image.load("imagenes/Rocket4.png")
                    self.sprite=4
                elif self.sprite ==4:
                    self.image  = pygame.image.load("imagenes/Rocket5.png")
                    self.sprite=0
                if pospl<=self.rect.y:
                    self.rect.y-=4
                else:
                    self.rect.y+=4
            elif self.tipo==3:
                if self.sprite ==0:
                    self.image  = pygame.image.load("imagenes/Painelem3.png")
                    self.sprite=1
                elif self.sprite ==1:
                    self.image  = pygame.image.load("imagenes/Painelem2.png")
                    self.sprite=2
                elif self.sprite ==2:
                    self.image  = pygame.image.load("imagenes/Painelem1.png")
                    self.sprite=3
                elif self.sprite ==3:
                    self.image  = pygame.image.load("imagenes/Painelem2.png")
                    self.sprite=0
            elif self.tipo==4:
                if self.sprite ==0:
                    self.image  = pygame.image.load("imagenes/Lostsoul1i.png")
                    self.sprite=1
                elif self.sprite ==1:
                    self.image  = pygame.image.load("imagenes/Lostsoul2i.png")
                    self.sprite=0
            self.rect.x = self.rect.x - self.vel - velpl
            self.pasos+=1
            superficie.blit(self.image, self.rect)

class Nivel(object):

    plataforma_lista=None
    enemigos_lista=None

    fondo1=Fontrans
    fondo2=Fontrans1
    fondo3=Fontrans2
    fondo4=Fontrans3
    fondo5=Fontrans4

    rect1=fondo1.get_rect()
    mov_fondo=0

    def __init__(self,jugador):
        self.plataforma_lista=pygame.sprite.Group()
        self.enemigos_lista=pygame.sprite.Group()
        self.jugador=jugador

    def update(self):
        self.plataforma_lista.update()
        self.enemigos_lista.update()

    def draw(self,pantalla):

        pantalla.fill(AZUL)
        pantalla.blit(self.fondo3,(self.rect1.x-800,self.rect1.y))
        pantalla.blit(self.fondo1,(self.rect1))
        pantalla.blit(self.fondo2,(self.rect1.x+800,self.rect1.y))
        pantalla.blit(self.fondo3,(self.rect1.x+1600,self.rect1.y))
        pantalla.blit(self.fondo1,(self.rect1.x+2400,self.rect1.y))
        pantalla.blit(self.fondo4,(self.rect1.x,self.rect1.y-800))
        pantalla.blit(self.fondo4,(self.rect1.x,self.rect1.y-1600))
        pantalla.blit(self.fondo4,(self.rect1.x,self.rect1.y-2400))
        pantalla.blit(self.fondo5,(self.rect1.x,self.rect1.y-2400))


        self.plataforma_lista.draw(pantalla)
        self.enemigos_lista.draw(pantalla)

    def Mover_fondox(self,mov_x):
        self.mov_fondo += mov_x
        for plataforma in self.plataforma_lista:
            plataforma.rect.x += mov_x
        for enemigos in self.enemigos_lista:
            enemigos.rect.x += mov_x
        self.rect1.x+=mov_x

    def Mover_fondoy(self,mov_y):
        self.mov_fondo += mov_y
        for plataforma in self.plataforma_lista:
            plataforma.rect.y += mov_y
        for enemigos in self.enemigos_lista:
            enemigos.rect.y += mov_y
        self.rect1.y+=mov_y


class Nivel_01(Nivel):

    def __init__(self,jugador):

        Nivel.__init__(self,jugador)
        
        self.limiteder=-1500

        nivel=[[10,600,-30,0],[210,10,1400,200],[210,10,500,400], [210,10,900,300],
               [210,10,1100,400],[210,10,1000,500],[10,300,1000,300],
               [210,10,1760,330],[10,260,1950,340]]


        for plataforma in nivel:
            bloque =Plataforma(plataforma[0],plataforma[1])
            bloque.rect.x=plataforma[2]
            bloque.rect.y=plataforma[3]
            bloque.jugador =self.jugador
            self.plataforma_lista.add(bloque)

class Nivel_02(Nivel):

    def __init__(self,jugador):

        Nivel.__init__(self,jugador)
        
        self.limiteder=-1600

        nivel=[[200,10,-200,330],[10,260,0,340],[150,10,500,500],
               [100,20,540,300], [50,20,600,150],[210,10,200,-50],
               [100,20,540,-250], [50,20,600,-450],[210,10,200,-600],
               [100,20,540,-750], [50,20,600,-850],[210,10,200,-1000],
               [100,20,540,-1100], [50,20,600,-1250],[210,10,200,-1450]]


        for plataforma in nivel:
            bloque =Plataforma(plataforma[0],plataforma[1])
            bloque.rect.x=plataforma[2]
            bloque.rect.y=plataforma[3]
            bloque.jugador =self.jugador
            self.plataforma_lista.add(bloque)

def main():
    pygame.init()
    pygame.mixer.init()
    fuente= pygame.font.Font("fuentes/zrnic___.ttf", 30)
    fuentep=pygame.font.Font("fuentes/zrnic___.ttf",15)
    pygame.display.set_caption("The Warrior: Ultimo Intento")
    Fon        = pygame.mixer.Sound("sonidos/Lev1.ogg").play(-1)
    Enemies    = pygame.mixer.Sound("sonidos/06.mp3")
    Enemies.play(-1)
    Fire       = pygame.mixer.Sound("sonidos/blow.ogg")
    Plasmafire = pygame.mixer.Sound("sonidos/Plasmarifle.wav")
    Bfgfire    = pygame.mixer.Sound("sonidos/BFG.wav")
    Bfghit     = pygame.mixer.Sound("sonidos/BFGhit.wav")
    Enemyhit   = pygame.mixer.Sound("sonidos/Cacohit.wav")
    Painehit   = pygame.mixer.Sound("sonidos/Painhit.wav")
    Cacodeath  = pygame.mixer.Sound("sonidos/Cacodeath.wav")
    Paindeath  = pygame.mixer.Sound("sonidos/Paindeath.wav")
    Lostdeath  = pygame.mixer.Sound("sonidos/Lostdeath.wav")
    tamano=[Ancho,Alto]
    pantalla = pygame.display.set_mode(tamano)
    w_score  = open("data/puntaje.txt", "w")
    r_score  = open("data/puntaje.txt", "r")
    w_temp   = open("data/temp.txt", "w")
    puntos=0
    tipobul=1
    dano=0
    bulc=0
    miscount=0

    for li in r_score:
        p = fuentep.render("Puntaje Máximo: " +li, True, (255, 255, 255))

    jugador=Jugador()

    nivel_lista=[]
    nivel_lista.append(Nivel_01(jugador))
    nivel_lista.append(Nivel_02(jugador))
    nivel_tot=len(nivel_lista)

    nivel_actual_no=0
    nivel_actual=nivel_lista[nivel_actual_no]

    activos_sp_lista = pygame.sprite.Group()
    enemigos_lista   = pygame.sprite.Group()
    enembal_lista    = pygame.sprite.Group()
    balas_lista      = pygame.sprite.Group()
    jugador.nivel    = nivel_actual

    jugador.rect.x=340
    jugador.rect.y=Alto-jugador.rect.height
    activos_sp_lista.add(jugador)

    for i in range (7):
            posx=random.randint(1200,1400)
            posy=random.randint(50,500)
            entipo=random.randint(1,3)
            enem=Enemigo(posx,posy,entipo)
            enemigos_lista.add(enem)
            activos_sp_lista.add(enem)

    fin=False

    while not fin:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                fin=True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    jugador.isfiring=0
                    jugador.isrun=1
                    jugador.ir_der(pantalla)
                if e.key ==pygame.K_LEFT:
                    jugador.isfiring=0
                    jugador.isrun=1
                    jugador.ir_izq(pantalla)
                if e.key ==pygame.K_UP:
                    jugador.isfiring=0
                    jugador.salto(pantalla)
                if e.key ==pygame.K_SPACE:
                    jugador.disparo(pantalla)
                    if tipobul==0:
                        jugador.isfiring=2
                        if bulc < 1:
                            if jugador.bullets>10:
                                Bfgfire.play()
                                Bl1 = Balas(jugador.rect.x,jugador.rect.y,tipobul, jugador.dir)
                                balas_lista.add(Bl1)
                                activos_sp_lista.add(Bl1)
                                jugador.bullets-=10
                                bulc+=1
                    if tipobul==1:
                        jugador.isfiring=1
                        if bulc < 5:
                            if jugador.bullets>0:
                                Plasmafire.play()
                                Bl1 = Balas(jugador.rect.x,jugador.rect.y,tipobul, jugador.dir)
                                balas_lista.add(Bl1)
                                activos_sp_lista.add(Bl1)
                                jugador.bullets-=1
                                bulc+=1
                if e.key ==pygame.K_1:
                    tipobul=1
                if e.key ==pygame.K_2:
                    tipobul=0
                elif e.key == pygame.K_RETURN:
                    Fon.set_volume(2.0)
                    Enemies.stop()
                    imagen= pygame.image.load('imagenes/pause.png')

                    pantalla.blit(imagen,(100,200))

                    pygame.display.flip()
                    Pausa=True
                    while Pausa:
                        for k in pygame.event.get():
                          if k.type == pygame.QUIT:
                              Pausa=False
                              fin=True
                              w_score.write(str(puntos) + "\n")
                              w_score.close()
                          if k.type == pygame.KEYDOWN:
                              if k.key == pygame.K_b:
                                  Fon.set_volume(10.0)
                                  Enemies.play(-1)
                                  Pausa=False
                              if k.key == pygame.K_s:
                                  Pausa=False
                                  fin=True

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT and jugador.velx < 0:
                    jugador.isrun=0
                    jugador.no_mover(pantalla)
                if e.key ==pygame.K_RIGHT and jugador.velx > 0:
                    jugador.isrun=0
                    jugador.no_mover(pantalla)

        activos_sp_lista.update()

        txt_puntos = fuentep.render("Puntaje: " + str(puntos),True,(255,255,255))
        pantalla.blit(txt_puntos,[10,10])

        for en in enemigos_lista:
            if en.tipo==2:
                if nivel_actual_no==0:
                    en.izquierda(pantalla,jugador.rect.y, jugador.velx)
                else:
                    en.izquierda(pantalla,jugador.rect.y, 0)
            else:
                if nivel_actual_no==0:
                    en.izquierda(pantalla,0, jugador.velx)
                else:
                    en.izquierda(pantalla,0, 0)
            if en.pasos==en.lanzar:
                if en.tipo==1:
                    enbl = Balas(en.rect.x, en.rect.y, 2, 1)
                elif en.tipo==3:
                    enbl = Enemigo(en.rect.x, en.rect.y, 4)
                if enbl.tipo==4:
                    enemigos_lista.add(enbl)
                else:
                    enembal_lista.add(enbl)
                activos_sp_lista.add(enbl)
                en.pasos  = 0
                en.lanzar = random.randint(20,100)
            if (en.rect.x < 0 or en.rect.y >630) and en.tipo!=4:
              enemigos_lista.remove(en)
              activos_sp_lista.remove(en)
              posx=random.randint(800,1200)
              posy=random.randint(50,500)
              entipo=random.randint(1,3)
              ene=Enemigo(posx,posy,entipo)
              enemigos_lista.add(ene)
              activos_sp_lista.add(ene)
              if jugador.bullets<=68:
                  jugador.bullets+=2

        if jugador.vidas<=0:
            fin=True
            activos_sp_lista.remove(jugador)
            w_score.write(str(puntos) + "\n")
            w_score.close()

        for buld in balas_lista:
            buld.derecha(pantalla)
            if buld.rect.x > 850 or buld.rect.x < 0:
                balas_lista.remove(buld)
                activos_sp_lista.remove(buld)
                bulc-=1
            bulimp = pygame.sprite.spritecollide(buld,enemigos_lista,False)
            for en in bulimp:
                if buld.tipo == 1:
                      balas_lista.remove(buld)
                      activos_sp_lista.remove(buld)
                      bulc-=1
                if buld.tipo==0:
                      Bfghit.play()
                #print en.vidas
                if en.vidas <=0:
                      if en.tipo==1:
                          Cacodeath.play()
                      elif en.tipo==2 or en.tipo==4:
                          Lostdeath.play()
                      elif en.tipo==3:
                          Paindeath.play()
                      enemigos_lista.remove(en)
                      activos_sp_lista.remove(en)
                      posx=random.randint(800,1200)
                      posy=random.randint(50,500)
                      entipo=random.randint(1,3)
                      ene=Enemigo(posx,posy,entipo)
                      enemigos_lista.add(ene)
                      activos_sp_lista.add(ene)
                      puntos +=1000
                else:
                      en.vidas-=random.randint(2,3)
                      if en.tipo==1:
                          Enemyhit.play()
                      elif en.tipo==3:
                          Painehit.play()
                    
        for bule in enembal_lista:
            bule.derecha(pantalla)
            if bule.rect.x < 0:
                enembal_lista.remove(bule)
                activos_sp_lista.remove(bule)
            bulenimp = pygame.sprite.spritecollide(jugador,enembal_lista,False)
            for bl in bulenimp:
                    enembal_lista.remove(bl)
                    activos_sp_lista.remove(bl)
                    jugador.vidas-=1
                    Fire.play()
        
        golpazo=pygame.sprite.spritecollide(jugador,enemigos_lista,True)
        for f in golpazo:
            if f.tipo==1:
                dano=random.randint(1,3)
            elif f.tipo==2:
                dano=random.randint(3,5)
            elif f.tipo==3:
                dano=random.randint(5,7)
            enemigos_lista.remove(f)
            activos_sp_lista.remove(f)
            Fire.play()
            posx=random.randint(800,1200)
            posy=random.randint(50,500)
            entipo=random.randint(1,3)
            ene=Enemigo(posx,posy,entipo)
            enemigos_lista.add(ene)
            activos_sp_lista.add(ene)
            jugador.vidas-=dano
            
            
        nivel_actual.update()
        if nivel_actual_no==0:
            if jugador.rect.right >= 450:
                dif=jugador.rect.x - 450
                jugador.rect.x = 450
                nivel_actual.Mover_fondox(-dif)

            if jugador.rect.left <=120:
                dif=120-jugador.rect.x
                jugador.rect.x=120
                nivel_actual.Mover_fondox(dif)
        elif nivel_actual_no==1:
            if jugador.rect.top <= 100:
                dif=jugador.rect.y - 100
                jugador.rect.y = 100
                nivel_actual.Mover_fondoy(-dif)
                for en in enemigos_lista:
                    en.rect.y-=dif
                for bl in balas_lista:
                    bl.rect.y-=dif
                for enbl in enembal_lista:
                    enbl.rect.y-=dif
            
            if jugador.rect.right >= 800:
                jugador.rect.x = jugador.rect.x - 6

            if jugador.rect.left <=0:
                jugador.rect.x= - jugador.rect.x

        if nivel_actual_no==0:
            pos_actual=jugador.rect.x + nivel_actual.mov_fondo
        else:
            pos_actual=jugador.rect.y - nivel_actual.mov_fondo
        nivel_actual.draw(pantalla)
        if pos_actual < nivel_actual.limiteder:
            jugador.rect.x=120
            if nivel_actual_no <nivel_tot-1:
                nivel_actual_no += 1
                nivel_actual=nivel_lista[nivel_actual_no]
                jugador.nivel=nivel_actual
                Nivel.rect1.x = 0
                
                
            else:
                Fon.stop()
                Enemies.stop()
                Intro=True
                FonInt=0
                Fondo=None
                Intmus=pygame.mixer.Sound("sonidos/Intermedio.ogg")
                Intmus.play(-1)
                fuente1 = fuente.render("Enter - continuar", 1, (255,255,255))
                while Intro:
                    for k in pygame.event.get():
                        if k.type == pygame.QUIT:
                            Bcg.stop()
                            Intro=False
                            fin=True
                        if k.type == pygame.KEYDOWN:
                            if k.key == pygame.K_RETURN:
                                if FonInt==0:
                                    FonInt=1
                        if FonInt==0:
                            Fondo="imagenes/Fin1.png"
                        elif FonInt==1:
                            Intro=False
                        Hist=pygame.image.load(Fondo)
                        pantalla.blit(Hist, [0, 0])
                        pantalla.blit(fuente1, (10,500))
                        pygame.display.flip()
                w_temp.write(str(puntos) + "\n")
                w_temp.close()
                Intmus.stop()
                Jefe.main()
                pygame.quit()
        
        for nv in range(jugador.vidas):
            vd=Vidas(nv,pantalla)
        for nb in range (jugador.bullets):
            ps=Poder(nb,pantalla)
        txt_puntos=fuentep.render("Puntaje: "+str(puntos),True,NEGRO)
        pantalla.blit(txt_puntos,[10,10])
        txt_nivel=fuentep.render("Nivel: "+str(nivel_actual_no+1),True,NEGRO)
        pantalla.blit(txt_nivel,[400,10])
        if tipobul==0:
            txt_plasma=fuentep.render("Arma actual: Bazuka Laser",True,NEGRO)
            pantalla.blit(txt_plasma,[10,30])
            txt_info=fuentep.render("Vida",True,NEGRO)
            pantalla.blit(txt_info,[10,50])
            txt_info=fuentep.render("Poder",True,NEGRO)
            pantalla.blit(txt_info,[10,70])
        if tipobul==1:
            txt_plasma=fuentep.render("Arma actual: Rifle de Plasma",True,NEGRO)
            pantalla.blit(txt_plasma,[10,30])
            txt_info=fuentep.render("Vida",True,NEGRO)
            pantalla.blit(txt_info,[10,50])
            txt_info=fuentep.render("Poder",True,NEGRO)
            pantalla.blit(txt_info,[10,70])
    
        
        activos_sp_lista.draw(pantalla)
        reloj.tick(60)
        pygame.display.flip()
    nivel_actual.draw(pantalla)
    activos_sp_lista.draw(pantalla)
    finjuego=False
    while not finjuego:
        imagen= pygame.image.load('imagenes/GameOver.png')

        pantalla.blit(imagen,(200,200))

        pygame.display.flip()
        for e in pygame.event.get():
              if e.type == pygame.QUIT:
                  finjuego=True
              if e.type == pygame.KEYDOWN:
                  if e.key == pygame.K_RETURN:
                      finjuego=True
              if e.type == pygame.KEYDOWN:
                  if e.key == pygame.K_w:
                      main()                     

if __name__=="__main__":
    main()
        
pygame.quit()
