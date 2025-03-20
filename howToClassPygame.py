# Benjamin Kellman
# 3/18/25

import pygame

class Box(pygame.sprite.Sprite):
    time = 0
    # describe self as the object, the instance of the class
    def __init__ (self, x, y, img, dx=0, dy=0): #time in seconds
        super().__init__() # Box is a child class calling its parent pygame.sprite.Sprite

        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        # x pos, y pos, x velocity, y velocity
        self.image = pygame.transform.scale_by(pygame.image.load(img), 0.05)#.convert_alpha()
        self.rect = self.image.get_rect(center = (200, 200))

    def __str__(self):
        return f"({self.x}, {self.y})   <{self.dx}, {self.dy}> at {self.time} seconds"
    
    def increaseTime(self, dt):
        self.time+=dt
        self.update(dt)

    def update(self, dt=1):
        self.x+=dt*self.dx
        self.y+=dt*self.dy
    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y)) # blit using the rect

clock = pygame.time.Clock()
background_colour = (234, 212, 252) 
screen = pygame.display.set_mode((1200, 800)) 
pygame.display.set_caption('Window Caption') 
screen.fill(background_colour) 
pygame.display.flip() 
thing = Box(50, 50, 'theBox.png', 2, 4)
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
    thing.update()
    if clock.get_time()%10==0:

        print(thing)
    pygame.display.flip()
    clock.tick(60)

