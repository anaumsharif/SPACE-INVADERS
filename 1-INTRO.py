import pygame 
from pygame import mixer
import math 
import random  #used fpor randomly placing enemy ships  


# Initializing pyagme 
pygame.init()

# create the screen 
screen = pygame.display.set_mode((800,768)) 

# importing the background images 
background = pygame.image.load("C:\\Users\\HP\\CODE\\VS-CODE\\PYTHON\\GAMES\\images\\SPACE INVADERS\\background.png")
mixer.music.load("C:\\Users\\HP\\CODE\\VS-CODE\\PYTHON\\GAMES\\images\\SPACE INVADERS\\background.wav") # for importing sounds 
mixer.music.play(-1)

enemy = pygame.image.load("C:\\Users\\HP\\CODE\\VS-CODE\\PYTHON\\GAMES\\images\\SPACE INVADERS\\enemy.png")
a =1
# Game loop
running = True
while running:
    # RGB = Red,Green,Blue
    screen.fill((0,0,0))
    
    # Background image 
    screen.blit(background,(0,0))
    
    # enemy image
    screen.blit (enemy,(100,100))
    screen.blit (enemy,(200,200))
    screen.blit (enemy,(400,250))
    screen.blit (enemy,(600,300))
    # to make it iterative or moving around 
    screen.blit (enemy,(a,100))
    a = a+1
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            running = False
    pygame.display.update()
    
    
