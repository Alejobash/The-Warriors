#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, random
from pygame.locals import *

NEGRO= [0,0,0]
ROJO=[255,0,0]
BLANCO=[255,255,255]
AZUL=[0,0,255]
CAFE=[102,51,0]
ROSA=[255,0,255]
AMARILLO=[255,255,0]
CELESTE=[0,255,255]
GRIS=[128,128,128]
GRISOSC=[64,64,64]
MORADO=[128,0,128]
NARANJA=[255,128,0]
Alto=600
Ancho=800
reloj = pygame.time.Clock()
Fontrans1=pygame.image.load("imagenes/lav.jpg")
Fontrans=pygame.image.load("imagenes/Bossbackg.png")
Fontrans=pygame.transform.scale(Fontrans,(650,500))

class Jugador(pygame.sprite.Sprite):
    velx=0
    vely=0
    sprite=0

    nivel=None

    def __init__(self, tipo):
        pygame.sprite.Sprite.__init__(self)

        self.isrun=1
        self.tipoj=tipo
        if self.tipoj==0:
            self.imager  = pygame.image.load("imagenes/Cyberdemond1.png")
            self.imager2 = pygame.image.load("imagenes/Cyberdemond2.png")
            self.imager3 = pygame.image.load("imagenes/Cyberdemond3.png")
            self.imager4 = pygame.image.load("imagenes/Cyberdemond4.png")
            self.imagel  = pygame.image.load("imagenes/Cyberdemoni1.png")
            self.imagel2 = pygame.image.load("imagenes/Cyberdemoni2.png")
            self.imagel3 = pygame.image.load("imagenes/Cyberdemoni3.png")
            self.imagel4 = pygame.image.load("imagenes/Cyberdemoni4.png")
            self.imaged  = pygame.image.load("imagenes/Cyberdemon1.png")
            self.imaged2 = pygame.image.load("imagenes/Cyberdemon2.png")
            self.imaged3 = pygame.image.load("imagenes/Cyberdemon3.png")
            self.imaged4 = pygame.image.load("imagenes/Cyberdemon4.png")
            self.imageu  = pygame.image.load("imagenes/Cyberdemonb1.png")
            self.imageu2 = pygame.image.load("imagenes/Cyberdemonb2.png")
            self.imageu3 = pygame.image.load("imagenes/Cyberdemonb3.png")
            self.imageu4 = pygame.image.load("imagenes/Cyberdemonb4.png")
            self.image   = self.imaged
            self.rect=self.image.get_rect()
            self.vel=12
            self.ancho=85
            self.alto=110
        elif self.tipoj==1:
            self.imager=pygame.image.load("imagenes/Marinestd.png")
            self.imager1=pygame.image.load("imagenes/Marinewkd1.png")
            self.imager2=pygame.image.load("imagenes/Marinewkd2.png")
            self.imager3=pygame.image.load("imagenes/Marinewkd3.png")
            self.imager4=pygame.image.load("imagenes/Marinewkd4.png")
            self.imagel=pygame.image.load("imagenes/Marinesti.png")
            self.imagel1=pygame.image.load("imagenes/Marinewki1.png")
            self.imagel2=pygame.image.load("imagenes/Marinewki2.png")
            self.imagel3=pygame.image.load("imagenes/Marinewki3.png")
            self.imagel4=pygame.image.load("imagenes/Marinewki4.png")
            self.imaged=pygame.image.load("imagenes/Marinest.png")
            self.imaged1=pygame.image.load("imagenes/Marinewkf1.png")
            self.imaged2=pygame.image.load("imagenes/Marinewkf2.png")
            self.imaged3=pygame.image.load("imagenes/Marinewkf3.png")
            self.imaged4=pygame.image.load("imagenes/Marinewkf4.png")
            self.imageu=pygame.image.load("imagenes/Marinestb.png")
            self.imageu1=pygame.image.load("imagenes/Marinewkb1.png")
            self.imageu2=pygame.image.load("imagenes/Marinewkb2.png")
            self.imageu3=pygame.image.load("imagenes/Marinewkb3.png")
            self.imageu4=pygame.image.load("imagenes/Marinewkb4.png")
            self.image=self.imagel
            self.rect=self.image.get_rect()
            self.vel=8
            self.ancho=33
            self.alto=48

        self.dir=0
        self.vidas=100
        self.psi=100
        self.walking   = False

    def mover(self, px, py):
                self.rect.move_ip(px, py)
                    

    def refrescar(self, superficie, px, py):
        if self.isrun==1:
            if self.tipoj==0:
                    if self.dir==0:
                        if self.sprite==0:
                            self.image = self.imagel
                            self.sprite=1
                        elif self.sprite==1:
                            self.image = self.imagel2
                            self.sprite=2
                        elif self.sprite==2:
                            self.image = self.imagel3
                            self.sprite=3
                        elif self.sprite==3:
                            self.image = self.imagel4
                            self.sprite=0
                    elif self.dir==1:
                        if self.sprite==0:
                            self.image = self.imager
                            self.sprite=1
                        elif self.sprite==1:
                            self.image = self.imager2
                            self.sprite=2
                        elif self.sprite==2:
                            self.image = self.imager3
                            self.sprite=3
                        elif self.sprite==3:
                            self.image = self.imager4
                            self.sprite=0
                    elif self.dir==2:
                        if self.sprite==0:
                            self.image = self.imageu
                            self.sprite=1
                        elif self.sprite==1:
                            self.image = self.imageu2
                            self.sprite=2
                        elif self.sprite==2:
                            self.image = self.imageu3
                            self.sprite=3
                        elif self.sprite==3:
                            self.image = self.imageu4
                            self.sprite=0
                    elif self.dir==3:
                        if self.sprite==0:
                            self.image = self.imaged
                            self.sprite=1
                        elif self.sprite==1:
                            self.image = self.imaged2
                            self.sprite=2
                        elif self.sprite==2:
                            self.image = self.imaged3
                            self.sprite=3
                        elif self.sprite==3:
                            self.image = self.imaged4
                            self.sprite=0
            else:
                if self.dir==0:
                        if self.sprite==0:
                            self.image = self.imagel1
                            self.sprite=1
                        elif self.sprite==1:
                            self.image = self.imagel2
                            self.sprite=2
                        elif self.sprite==2:
                            self.image = self.imagel3
                            self.sprite=3
                        elif self.sprite==3:
                            self.image = self.imagel4
                            self.sprite=0 
                elif self.dir==1:
                        if self.sprite==0:
                            self.image = self.imager1
                            self.sprite=1
                        elif self.sprite==1:
                            self.image = self.imager2
                            self.sprite=2
                        elif self.sprite==2:
                            self.image = self.imager3
                            self.sprite=3
                        elif self.sprite==3:
                            self.image = self.imager4
                            self.sprite=0
                elif self.dir==2:
                        if self.sprite==0:
                            self.image = self.imageu1
                            self.sprite=1
                        elif self.sprite==1:
                            self.image = self.imageu2
                            self.sprite=2
                        elif self.sprite==2:
                            self.image = self.imageu3
                            self.sprite=3
                        elif self.sprite==3:
                            self.image = self.imageu4
                            self.sprite=0
                elif self.dir==3:
                        if self.sprite==0:
                            self.image = self.imaged1
                            self.sprite=1
                        elif self.sprite==1:
                            self.image = self.imaged2
                            self.sprite=2
                        elif self.sprite==2:
                            self.image = self.imaged3
                            self.sprite=3
                        elif self.sprite==3:
                            self.image = self.imaged4
                            self.sprite=0
            self.mover(px, py)
            superficie.blit(self.image, self.rect)
        elif self.isrun==0:
            if self.dir==0:
                self.image=self.imagel
            elif self.dir==1:
                self.image=self.imager
            elif self.dir==2:
                self.image=self.imageu
            elif self.dir==3:
                self.image=self.imaged
class Vidas():

    def __init__(self,nvidas, pantalla, px):
        self.alto=3
        self.ancho=30
        self.sep=0
        self.vidas=nvidas
        self.Verde=2.55
        self.Rojo=255-(nvidas*self.Verde)
        self.color=[self.Rojo,self.Verde*nvidas,0]
        self.pos_x=px
        self.pos_yini=400
        self.pos_y=self.pos_yini-(nvidas*(self.alto+self.sep))
        pygame.draw.rect(pantalla,self.color,[self.pos_x,self.pos_y, self.ancho,self.alto])

class Psi():

    def __init__(self,npsi, pantalla):
        self.alto=3
        self.ancho=30
        self.sep=0
        self.vidas=npsi
        self.Azul=2.55
        self.Rojo=255-(npsi*self.Azul)
        self.color=[self.Rojo,0,self.Azul*npsi]
        self.pos_x=50
        self.pos_yini=400
        self.pos_y=self.pos_yini-(npsi*(self.alto+self.sep))
        pygame.draw.rect(pantalla,self.color,[self.pos_x,self.pos_y, self.ancho,self.alto])


class Plataforma(pygame.sprite.Sprite):

    def __init__(self,ancho,alto):
        self.Anc=ancho
        self.Alt=alto
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([self.Anc,self.Alt])
        self.rect=self.image.get_rect()

class Ondapsi (pygame.sprite.Sprite):

        def __init__(self, posx, posy,tipo, direc, dan):
                pygame.sprite.Sprite.__init__(self)
                self.sprite    = 0
                self.tipo      = tipo
                self.direccion = direc
                self.danopsi   = dan
                self.image = pygame.image.load("imagenes/BFGshot1.png")
                self.rect  = self.image.get_rect()
                if self.tipo == 0:
                    self.vel   =  5
                    if self.direccion == 1 or self.direccion == 0:
                        self.rect.x = posx
                        self.rect.y = posy+10
                    if self.direccion == 2 or self.direccion == 3:
                        self.rect.x = posx
                        self.rect.y = posy
                if self.tipo ==1:
                    self.vel   =  10
                    self.image = pygame.image.load("imagenes/Plasma.png")
                    self.rect  = self.image.get_rect()
                    if self.direccion == 1:
                        self.rect.x = posx+10
                        self.rect.y = posy+14
                    if self.direccion == 0:
                        self.rect.x = posx-10
                        self.rect.y = posy+14
                    if self.direccion ==2 or self.direccion ==3:
                        self.rect.x = posx
                        self.rect.y = posy
                if self.tipo ==2:
                    self.vel   =  15
                    if self.direccion ==1:
                        self.image = pygame.image.load("imagenes/rbullet.png")
                        self.rect  = self.image.get_rect()
                        self.rect.x = posx
                        self.rect.y = posy
                    if self.direccion ==0:
                        self.image = pygame.image.load("imagenes/lbullet.png")
                        self.rect  = self.image.get_rect()
                        self.rect.x = posx
                        self.rect.y = posy
                    if self.direccion ==2:
                        self.image = pygame.image.load("imagenes/ubullet.png")
                        self.rect  = self.image.get_rect()
                        self.rect.x = posx
                        self.rect.y = posy
                    if self.direccion ==3:
                        self.image = pygame.image.load("imagenes/dbullet.png")
                        self.rect  = self.image.get_rect()
                        self.rect.x = posx
                        self.rect.y = posy

        def derecha(self, superficie):
            if self.tipo ==0:
                if self.sprite==0:
                    self.image = pygame.image.load("imagenes/BFGshot1.png")
                    self.sprite=1
                elif self.sprite==1:
                    self.image = pygame.image.load("imagenes/BFGshot2.png")
                    self.sprite=0
            if self.tipo ==1:
                if self.sprite==0:
                    self.image = pygame.image.load("imagenes/plasma.png")
                    self.sprite=1
                elif self.sprite==1:
                    self.image = pygame.image.load("imagenes/plasma2.png")
                    self.sprite=0
            self.rect.x = self.rect.x + self.vel
            superficie.blit(self.image, self.rect)
        def izquierda(self, superficie):
            if self.tipo ==0:
                if self.sprite==0:
                    self.image = pygame.image.load("imagenes/BFGshot1.png")
                    self.sprite=1
                elif self.sprite==1:
                    self.image = pygame.image.load("imagenes/BFGshot2.png")
                    self.sprite=0
            if self.tipo ==1:
                if self.sprite==0:
                    self.image = pygame.image.load("imagenes/plasma.png")
                    self.sprite=1
                elif self.sprite==1:
                    self.image = pygame.image.load("imagenes/plasma2.png")
                    self.sprite=0
            self.rect.x = self.rect.x - self.vel
            superficie.blit(self.image, self.rect)
        def arriba(self, superficie):
            if self.tipo ==0:
                if self.sprite==0:
                    self.image = pygame.image.load("imagenes/BFGshot1.png")
                    self.sprite=1
                elif self.sprite==1:
                    self.image = pygame.image.load("imagenes/BFGshot2.png")
                    self.sprite=0
            if self.tipo ==1:
                if self.sprite==0:
                    self.image = pygame.image.load("imagenes/plasma.png")
                    self.sprite=1
                elif self.sprite==1:
                    self.image = pygame.image.load("imagenes/plasma2.png")
                    self.sprite=0
            self.rect.y = self.rect.y - self.vel
            superficie.blit(self.image, self.rect)
        def abajo(self, superficie):
            if self.tipo ==0:
                if self.sprite==0:
                    self.image = pygame.image.load("imagenes/BFGshot1.png")
                    self.sprite=1
                elif self.sprite==1:
                    self.image = pygame.image.load("imagenes/BFGshot2.png")
                    self.sprite=0
            if self.tipo ==1:
                if self.sprite==0:
                    self.image = pygame.image.load("imagenes/plasma.png")
                    self.sprite=1
                elif self.sprite==1:
                    self.image = pygame.image.load("imagenes/plasma2.png")
                    self.sprite=0
            self.rect.y = self.rect.y + self.vel
            superficie.blit(self.image, self.rect)

class Nivel(object):

    plataforma_lista=None
    
    fondo2=Fontrans1
    fondo1=Fontrans
    rect1=fondo1.get_rect()

    def __init__(self,jugador):
        self.plataforma_lista=pygame.sprite.Group()
        self.jugador=jugador

    def update(self):
        self.plataforma_lista.update()

    def draw(self,pantalla):

        pantalla.fill(GRIS)
        pantalla.blit(self.fondo2,(0,0))
        pantalla.blit(self.fondo1,(100,100))
        self.plataforma_lista.draw(pantalla)  

class Nivel_01(Nivel):

    def __init__(self,jugador):

        Nivel.__init__(self,jugador)

        nivel=[[10,600,100,90],[650,10,100,100],[10,600,750,100],[650,10,100,590]]


        for plataforma in nivel:
            bloque =Plataforma(plataforma[0],plataforma[1])
            bloque.rect.x=plataforma[2]
            bloque.rect.y=plataforma[3]
            bloque.jugador =self.jugador
            self.plataforma_lista.add(bloque)

def main():
    pygame.init()
    pygame.mixer.init()
    fuente     = pygame.font.Font("fuentes/zrnic___.ttf", 30)
    fuentep    = pygame.font.Font("fuentes/zrnic___.ttf",15)
    pygame.mixer.Sound("sonidos/Boss.ogg").play(-1)
    Plasma     = pygame.mixer.Sound("sonidos/Plasmarifle.wav")
    Bfg        = pygame.mixer.Sound("sonidos/BFG.wav")
    Marinehit  = pygame.mixer.Sound("sonidos/Crash.wav")
    Cybersight = pygame.mixer.Sound("sonidos/Cybersight.wav").play()
    Cyberfire  = pygame.mixer.Sound("sonidos/Cyberfire.wav")
    Cyberhit   = pygame.mixer.Sound("sonidos/Cyberhit.wav")
    Cyberwalk  = pygame.mixer.Sound("sonidos/Cyberwalk.wav")
    Cyberdeath = pygame.mixer.Sound("sonidos/Cyberdeath.wav")
    Fire       = pygame.mixer.Sound("sonidos/Bomb.wav")
    tamano     = [Ancho,Alto]
    pantalla   = pygame.display.set_mode(tamano)
    pygame.display.set_caption("Doom 2: Ultimo Intento")
    w_score  = open("data/puntaje.txt", "w")
    r_score  = open("data/puntaje.txt", "r")
    r_temp   = open("data/temp.txt","r")
    puntos   = int(r_temp.readline())
    tipopsi  = 1
    posix    = 0
    posiy    = 0
    rpress   = lpress = upress = dpress = spress = False
    distmax  = 0
    dist     = 0
    psidano  = 0
    dano     = 0
    psic     = 0
    balac    = 0
    tanquedis= 0
    tiempdis = 0
    maxdis   = 0

    jugador=Jugador(1)
    jefe=Jugador(0)

    nivel_lista=[]
    nivel_lista.append(Nivel_01(jugador))
    nivel_actual=nivel_lista[0]

    activos_sp_lista=pygame.sprite.Group()
    jefe_lista=pygame.sprite.Group()
    psilanzado=pygame.sprite.Group()
    disparosjefe=pygame.sprite.Group()
    jugador.nivel=nivel_actual
    jugador.isrun=0

    jefe.rect.x=(Ancho-jefe.rect.width)/2
    jefe.rect.y=(Alto-jefe.rect.height)/2
    activos_sp_lista.add(jefe)
    jefe_lista.add(jefe)
    jugador.rect.x=440
    jugador.rect.y=Alto-20-jugador.rect.height
    activos_sp_lista.add(jugador)
    
    Cyberwalk.play(-1)
    fin=False

    while not fin:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                fin=True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    jugador.isrun=1
                    rpress = True
                    jugador.dir=1
                    posix=(jugador.vel)
                if e.key ==pygame.K_LEFT:
                    jugador.isrun=1
                    lpress = True
                    jugador.dir=0
                    posix=-(jugador.vel)
                if e.key ==pygame.K_UP:
                    jugador.isrun=1
                    upress = True
                    jugador.dir=2
                    posiy=-(jugador.vel)
                if e.key ==pygame.K_DOWN:
                    jugador.isrun=1
                    dpress = True
                    jugador.dir=3
                    posiy=jugador.vel
                if e.key ==pygame.K_SPACE:
                    if tipopsi==0:
                        if psic < 1:
                            if jugador.psi>10:
                                Bfg.play()
                                psidano=random.randint(10,15)
                                Ps1 = Ondapsi(jugador.rect.x,jugador.rect.y,tipopsi, jugador.dir, psidano)
                                psilanzado.add(Ps1)
                                activos_sp_lista.add(Ps1)
                                jugador.psi-=10
                                psic+=1
                    if tipopsi==1:
                        if psic < 3:
                            if jugador.psi>2:
                                Plasma.play()
                                psidano=random.randint(2,4) 
                                Ps1 = Ondapsi(jugador.rect.x,jugador.rect.y,tipopsi, jugador.dir, psidano)
                                psilanzado.add(Ps1)
                                activos_sp_lista.add(Ps1)
                                jugador.psi-=2
                                psic+=1
                if e.key ==pygame.K_1:
                    tipopsi=1
                if e.key ==pygame.K_2:
                    tipopsi=0
                elif e.key == pygame.K_RETURN:
                    pygame.mixer.pause()
                    imagen= pygame.image.load('imagenes/pause.png')

                    pantalla.blit(imagen,(75,200))
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
                                  Pausa=False
                                  pygame.mixer.unpause()
                              if k.key == pygame.K_s:
                                  Pausa=False
                                  fin=True

            if e.type == pygame.KEYUP:
                    if e.key == pygame.K_LEFT:
                        lpress=False
                        posix = 0
                        if (not(lpress)and not(rpress)) and (not(upress) and not(dpress)):
                            jugador.isrun=0
                    if e.key == pygame.K_RIGHT:
                        rpress = False
                        posix = 0
                        if not(lpress)and not(rpress) and not(upress) and not(dpress):
                            jugador.isrun=0
                    if e.key == pygame.K_UP:
                        upress = False
                        posiy = 0
                        if not(lpress)and not(rpress) and not(upress) and not(dpress):
                            jugador.isrun=0
                    if e.key == pygame.K_DOWN:
                        dpress = False
                        posiy = 0
                        if not(lpress)and not(rpress) and not(upress) and not(dpress):
                            jugador.isrun=0

        activos_sp_lista.update()

        txt_puntos = fuentep.render("Puntaje: " + str(puntos),True,(255,255,255))
        pantalla.blit(txt_puntos,[10,10])

        bloque_col_list=pygame.sprite.spritecollide(jugador,jugador.nivel.plataforma_lista,False)
        for bloque in bloque_col_list:
            if jugador.rect.x<110:
                jugador.rect.x+=10
            if jugador.rect.x>720:
                jugador.rect.x-=10
            if jugador.rect.y<110:
                jugador.rect.y+=10
            if jugador.rect.y>550:
                jugador.rect.y-=10
        for en in jefe_lista:
            if en.dir==0:
                tanquedis=random.randint(25,50)
                distmax=random.randint(100,600)
                if dist<=distmax:
                    en.refrescar(pantalla,-5,0)
                    dist+=5
                    tiempdis+=1
            elif en.dir==1:
                tanquedis=random.randint(25,50)
                distmax=random.randint(100,600)
                if dist<=distmax:
                    en.refrescar(pantalla,5,0)
                    dist+=5
                    tiempdis+=1
            elif en.dir==2:
                tanquedis=random.randint(25,50)
                distmax=random.randint(100,600)
                if dist<=distmax:
                    en.refrescar(pantalla,0,-5)
                    dist+=5
                    tiempdis+=1
            elif en.dir==3:
                tanquedis=random.randint(25,50)
                distmax=random.randint(100,600)
                if dist<=distmax:
                    en.refrescar(pantalla,0,5)
                    dist+=5
                    tiempdis+=1
            if dist>distmax:
                dist=0
                en.dir=random.randint(0,3)
            if tiempdis>tanquedis and maxdis<5:
                psidano=random.randint(20,25)
                Cyberfire.play()
                if en.dir==0 or en.dir==1:
                    Ps1 = Ondapsi(en.rect.x,en.rect.y+20,2, en.dir, psidano)
                else:
                    Ps1 = Ondapsi(en.rect.x+30,en.rect.y,2, en.dir, psidano)
                disparosjefe.add(Ps1)
                activos_sp_lista.add(Ps1)
                maxdis+=1
                tiempdis=0
                
            if en.rect.x > 670:
              en.rect.x-=10
              en.dir=random.randint(0,3)
              dist=0
              if jugador.psi<100:
                  jugador.psi+=1
            elif en.rect.x < 100:
              en.rect.x+=10
              en.dir=random.randint(0,3)
              dist=0
              if jugador.psi<100:
                  jugador.psi+=1
            elif en.rect.y < 100:
              en.rect.y+=10
              en.dir=random.randint(0,3)
              dist=0
              if jugador.psi<100:
                  jugador.psi+=1
            elif en.rect.y > 490:
              en.rect.y-=10
              en.dir=random.randint(0,3)
              dist=0
              if jugador.psi<100:
                  jugador.psi+=1

        for psd in psilanzado:
            if psd.direccion==1:
                psd.derecha(pantalla)
            if psd.direccion==0:
                psd.izquierda(pantalla)
            if psd.direccion==2:
                psd.arriba(pantalla)
            if psd.direccion==3:
                psd.abajo(pantalla)
            if psd.rect.x > 800 or psd.rect.x <100 or psd.rect.y <100 or psd.rect.y>650:
                psilanzado.remove(psd)
                activos_sp_lista.remove(psd)
                psic-=1
            psimp = pygame.sprite.spritecollide(psd,jefe_lista,False)
            for en in psimp:
                    psilanzado.remove(psd)
                    activos_sp_lista.remove(psd)
                    jefe.vidas-=psd.danopsi
                    en.vidas-=psd.danopsi
                    Cyberhit.play()
                    if en.vidas<=0:
                        Cyberwalk.stop()
                        jefe_lista.remove(en)
                        activos_sp_lista.remove(en)
                    psic-=1
                    puntos +=1000
        for dis in disparosjefe:
            if dis.direccion==1:
                dis.derecha(pantalla)
            if dis.direccion==0:
                dis.izquierda(pantalla)
            if dis.direccion==2:
                dis.arriba(pantalla)
            if dis.direccion==3:
                dis.abajo(pantalla)
            if dis.rect.x > 800 or dis.rect.x <100 or dis.rect.y <100 or dis.rect.y>650:
                disparosjefe.remove(dis)
                activos_sp_lista.remove(dis)
                maxdis-=1
            disimp = pygame.sprite.spritecollide(jugador,disparosjefe,False)
            for di in disimp:
                    Marinehit.play()
                    disparosjefe.remove(di)
                    activos_sp_lista.remove(di)
                    jugador.vidas-=di.danopsi
                    psic-=1
                    puntos +=1000
            
        if jefe.vidas<=0:
            Cyberdeath.play()
            fin=True
            w_score.write(str(puntos) + "\n")
            w_score.close()
            Intro=True
            FonInt=0
            Fondo=None
            fuente1 = fuente.render("Enter - Continuar", 1, (255,255,255))
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
                        Fondo="imagenes/Final.jpg"
                    elif FonInt==1:
                        Intro=False
                    Hist=pygame.image.load(Fondo)
                    pantalla.blit(Hist, [0, 0])
                    pantalla.blit(fuente1, (10,500))
                    pygame.display.flip()

        if jugador.vidas<=0:
            fin=True
            activos_sp_lista.remove(jugador)
            w_score.write(str(puntos) + "\n")
            w_score.close()
        
        golpazo=pygame.sprite.spritecollide(jugador,jefe_lista,False)
        for f in golpazo:
            Fire.play()
            jugador.vidas-=100
            
            
        nivel_actual.update()

        nivel_actual.draw(pantalla)
        activos_sp_lista.draw(pantalla)
        for nv in range(jugador.vidas):
            vd=Vidas(nv,pantalla,5)
        for jv in range(jefe.vidas):
            vd=Vidas(jv,pantalla,755)
        for np in range (jugador.psi):
            ps=Psi(np,pantalla)
        txt_puntos=fuentep.render("Puntaje: "+str(puntos),True,BLANCO)
        pantalla.blit(txt_puntos,[10,10])
        if tipopsi==0:
            txt_psiname=fuentep.render("Arma actual: BFG9000",True,BLANCO)
            pantalla.blit(txt_psiname,[10,30])
            #txt_info=fuentep.render("Danno masivo, Fuego lento, Objetivo multiple",True,NEGRO)
            #pantalla.blit(txt_info,[10,50])
            #txt_info=fuentep.render("Plasma usado: 10",True,NEGRO)
            #pantalla.blit(txt_info,[10,70])
        if tipopsi==1:
            txt_plasma=fuentep.render("Arma actual: Rifle de Plasma",True,BLANCO)
            pantalla.blit(txt_plasma,[10,30])
            #txt_info=fuentep.render("Dano medio, Fuego rapido, Objetivo unico",True,NEGRO)
            #pantalla.blit(txt_info,[10,50])
            #txt_info=fuentep.render("Plasma usado: 2",True,NEGRO)
            #pantalla.blit(txt_info,[10,70])
        jugador.refrescar(pantalla,posix,posiy)
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
