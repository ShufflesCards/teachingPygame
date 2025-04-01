# Benjamin Kellman
# 3/18/25

import pygame

class Box(pygame.sprite.Sprite):
    time = 0

    # describe self as the object, the instance of the class
    def __init__ (self, x, y, img, dx=0, dy=0, imageScalel=1): #time in seconds
        super().__init__() # Box is a child class calling its parent pygame.sprite.Sprite

        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        # x pos, y pos, x velocity, y velocity
        self.imageScale = 0.05
        self.imageWidth = (pygame.image.load(img).get_width())*self.imageScale
        self.imageHeight = (pygame.image.load(img).get_height())*self.imageScale
        self.image = pygame.transform.scale_by(pygame.image.load(img), self.imageScale)#.convert_alpha()
        self.rect = self.image.get_rect(center = (200, 200))

        self.visualHitbox = pygame.Surface([self.imageWidth, self.imageHeight])


    def __str__(self):
        return f"({self.x}, {self.y})   <{self.dx}, {self.dy}> at {self.time} units of time"
    def increaseSpeedX(self, dx): # do not use negative numbers
        if self.dx>0:
            self.dx+=dx
        else:
            self.dx-=dx
    def increaseSpeedY(self, dy): # do not use negative numbers
        if self.dx<0:
            self.dy-=dy
        else:
            self.dy+=dy

    def increaseTime(self, dt=1):
        self.time+=dt
        self.update(dt)

    def update(self, dt=1):
        self.x+=dt*self.dx
        self.y+=dt*self.dy

    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y)) # blit using the rect
        screen.blit(self.visualHitbox, (self.x, self.y))


    


        
clock = pygame.time.Clock()
background_colour = (234, 212, 252) 
screen = pygame.display.set_mode((1200, 800)) 
pygame.display.set_caption('Window Caption') 
screen.fill(background_colour) 
pygame.display.flip() 
thing = Box(50, 50, 'theBox.png', 2, 2, 0.05)
thing.increaseTime(4)
print(thing)


while True: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
        
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
    screen.fill(background_colour) 
    thing.draw(screen)
    thing.increaseTime()
    if thing.x >1200 or thing.x <0:
        if thing.dx>5 or thing.dx<-5:
            thing.dx = -thing.dx//1.2
        else:
            thing.dx =-thing.dx
    if thing.y >800 or thing.y < 0:
        if thing.dy>5 or thing.dy<-5:
            thing.dy = -thing.dy//1.2
        else:
            thing.dy= -thing.dy

    
    pygame.display.flip()
    clock.tick(60)

