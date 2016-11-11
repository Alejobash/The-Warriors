import pygame

class fondo(pygame.sprite.Sprite):
	def __init__(self):
		self.imagen=pygame.image.load("Background23.png").convert_alpha()

		self.rect=self.imagen.get_rect()
	def update(self,pantalla,vx,vy):
		self.rect.move_ip(-vx,-vy)
		pantalla.blit(self.imagen, self.rect)
		

class Player(pygame.sprite.Sprite):
    def __init__(self):
        #creo 4 imagenes
        self.imagen1=pygame.image.load("caminar1.png").convert_alpha()
        self.imagen2=pygame.image.load("caminar3.png").convert_alpha()
        self.imagen3=pygame.image.load("caminar33.png").convert_alpha()
        self.imagen4=pygame.image.load("caminar11.png").convert_alpha() 
         
        # creo la lista de las imaganes
        #el primer indice es la orientacion y el segundo la imagen
        # self.imagenes[self.orientacion][self.imagen_actual]      
        self.imagenes=[[self.imagen1,self.imagen2],[self.imagen3,self.imagen4]]
        
        self.imagen_actual=0
        self.imagen=self.imagenes[self.imagen_actual][0]
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(340,300)
        
        #variable par ver si se esta moviendo
        self.estamoviendo=False
        
        # 0 si va ala derecha 1 si va la izquierda
        self.orientacion=0

    def mover(self,vx,vy):
       self.rect.move_ip(vx,vy)
    
    
       
    #funcion principal de actualizacion   
    def update(self,superficie,vx,vy,t):
        # si no se mueve self.estamoviendo=FALSE
        if (vx,vy)==(0,0): self.estamoviendo=False
        else:self.estamoviendo=True # si se mueve que este en TRUE
        
        # con estas 2 lineas cambio la orientacion
        if vx>0: self.orientacion=0
        elif vx<0: self.orientacion=1
        
        # si el t==1 (auxiliar) y se esta moviendo entonces cambiar la imagen
        if t==1 and self.estamoviendo:
            self.nextimage()
            
        # mover el rectangulo  
        vx=0
        vy=0  
        self.mover(vx, vy)
        
        #self.imagen va ser la imagen que este en la orientacion y en el numero de imagen_actual
        self.imagen=self.imagenes[self.orientacion][self.imagen_actual]
        
        #finalmente pintar en la pantalla
        superficie.blit(self.imagen,self.rect)
        
    #funcion que se encarga de cambiar de imagen    
    def nextimage(self):
        self.imagen_actual+=1
        
        if self.imagen_actual>(len(self.imagenes)-1):# si se fue de rango que lo ponga en 0
            self.imagen_actual=0          
				

def main():
	import pygame
	
	
	pygame.init()
	pantalla=pygame.display.set_mode((800,550))
	salir=False
	reloj1= pygame.time.Clock()
	
	player1=Player()
	fondo1=fondo()
	vx,vy=0,0
	velocidad=10
	leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
	t=0
	
	while salir!=True:#LOOP PRINCIPAL
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				salir=True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					leftsigueapretada=True
					vx=-velocidad
				if event.key == pygame.K_RIGHT:
					rightsigueapretada=True
					vx=velocidad
				if event.key== pygame.K_UP:
					upsigueapretada=True
					vy=-velocidad
				
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					leftsigueapretada=False
					if rightsigueapretada:vx=velocidad
					else:vx=0
				if event.key == pygame.K_RIGHT:
					rightsigueapretada=False
					if leftsigueapretada:vx=-velocidad
					else:vx=0
				if event.key== pygame.K_UP:
					upsigueapretada=False
					if downsigueapretada:vy=velocidad
					else:vy=-0
				if event.key == pygame.K_DOWN:
					downsigueapretada=False
					if upsigueapretada:vy=-velocidad
					else:vy=0                    
		
		reloj1.tick(20)
		t+=1
		if t>1:
			t=0 
		pantalla.fill((200,200,200))
		fondo1.update(pantalla,vx,vy)
		player1.update(pantalla,vx,vy,t)
		pygame.display.update()
		   
	pygame.quit()
	
main()
