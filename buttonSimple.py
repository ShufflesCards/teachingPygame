# Benjamin Kellman
# 3/19/25

# you can't really make a button without a class, I will tell Mr. Kux and try to teach how to make a class

import pygame
pygame.init()
clock = pygame.time.Clock()
background_colour = (234, 212, 252) 
screen = pygame.display.set_mode((1200, 800)) 
pygame.display.set_caption('Window Caption') 
screen.fill(background_colour) 
pygame.display.flip() 

class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.alreadyPressed = False
    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
            
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 20)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def process(self):
        mousePos = pygame.mouse.get_pos()
        if (self.isOver(mousePos)):
            self.color = (255, 0, 0)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if not self.alreadyPressed:
                    print("ooga booga")
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        else:
            self.color = (0, 255, 0)
            

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x, y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

def drawWindow():
    screen.fill(background_colour)
    greenButton.draw(screen, (0,0,0))
    greenButton.process()


greenButton = Button((0, 255, 0), 40, 60, 100, 80, "hello")

while True: 
    drawWindow()
    pygame.display.update()
# for loop through the event queue   
    for event in pygame.event.get(): 
        mousePos = pygame.mouse.get_pos()
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()



    pygame.display.flip()
    clock.tick(60)

