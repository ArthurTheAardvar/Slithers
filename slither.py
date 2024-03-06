#slither game
#written by Martin Rivera Amparan
import pygame #imports
import math #needed for square root function
import random

pygame.init() #initializes Pygame
pygame.display.set_caption("Slither") #sets the window title
screen = pygame.display.set_mode((600,600)) #creates game screen
clock = pygame.time.Clock() #starts game clock

#game variables
doExit = False

#player variables
xpos = 200
ypos = 200
vx = 1
vy = 1

r = random.randrange(0, 255)
g = random.randrange(0, 255)
b = random.randrange(0, 255)

#+++++++++++++++++++++++++++++++++++++++
class pellet:
    def __init__(self, xpos, ypos, red, green, blue, radius):
        self.xpos = xpos
        self.ypos = ypos
        self.red = red
        self.green = green
        self.blue = blue
        self.radius = radius

    def collide(self,x,y):
        if math.sqrt((x-self.xpos)*(x-self.xpos)+(y-self.ypos)*(y-self.ypos)) < self.radius + 6:
            self.xpos = random.randrange(0, 600)
            self.ypos = random.randrange(0, 600)
            self.red = random.randrange(0, 255)
            self.green = random.randrange(0, 255)
            self.blue = random.randrange(0, 255)
            self.radius = random.randrange(0, 30)
            return True

    def draw(self):
        pygame.draw.circle(screen, (self.red, self.green, self.blue), (self.xpos, self.ypos), self.radius)

pelletBag = list() #creates a list data structure

class tailSeg:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos

    def update(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos

    def draw(self):
        r = random.randrange(0, 255)
        g = random.randrange(0, 255)
        b = random.randrange(0, 255)
        pygame.draw.circle(screen, (r, g, b), (self.xpos, self.ypos), 12)


tail = list()
oldX = 200
oldY = 200
counter = 0
#pushes 10 pellets into list
for i in range(10):
    pelletBag.append(pellet(random.randrange(0,600), random.randrange(0,600), random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255), random.randrange(0,30)))
#gameloop---------------------------------------------------------
while not doExit:

#event/input section---------------------
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True

        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos

            if mousePos[0] > xpos:
                vx = 1

            elif mousePos[0] < xpos:
                vx = -1
        

            if mousePos[1] > ypos:
                vy = 1

            elif mousePos[1] < ypos:
                vy = -1
      
        
            
#physics section-------------------------
    counter += 2 #update counter
    if counter == 20: #creates a delay so the segments follow behind
        counter = 0 #resets counter every 20 ticks
        oldX = xpos #holds onto old player position from 20 ticks ago
        oldY = ypos

        if(len(tail) > 2): #dont push numbers if there are no nodes yet
            for i in range(len(tail)): #loop for each slot in list
                #start in last position, push the *second to last* into it, repeat till at beginning
                tail[len(tail)-i-1].xpos = tail[len(tail)-i-2].xpos
                tail[len(tail)-i-1].ypos = tail[len(tail)-i-2].ypos
        if(len(tail) > 0): #if you have atleast one segment, push old head position into that
            tail[0].update(oldX, oldY) #push head position into first position of list

        #check for collision with pellets
        for i in range(10):
            if pelletBag[i].collide(xpos, ypos) == True:
                tail.append(tailSeg(oldX, oldY))

      
    

    #update circle position
    xpos += vx
    ypos += vy
#render section------------------------------------
    screen.fill((0,0,0))
    for i in range(10):
        pelletBag[i].draw()

    for i in range(len(tail)):
        tail[i].draw()

    pygame.draw.circle(screen, (r, g, b), (xpos, ypos), 12)
    pygame.display.flip()

#end game loop######################################
pygame.quit()