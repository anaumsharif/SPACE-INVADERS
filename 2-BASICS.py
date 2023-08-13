import pygame 
from pygame import mixer
import math 
import random  #used fpor randomly placing enemy ships  



# Initializing pyagme 
pygame.init()

# create the screen 
screen = pygame.display.set_mode((800,600)) 

# importing the background images 
background = pygame.image.load("C:\\Users\\HP\\CODE\\VS-CODE\\PYTHON\\GAMES\\images\\SPACE INVADERS\\background.png")

# importing sounds 
mixer.music.load('C:\\Users\\HP\\CODE\\VS-CODE\\PYTHON\\GAMES\\images\\SPACE INVADERS\\background.wav') # for importing sounds 
mixer.music.play(-1)

# caption and icons 
pygame.display.set_caption("SPACE INVADER")
icon = pygame.image.load("C:\\Users\\HP\\CODE\\VS-CODE\\PYTHON\\GAMES\\images\\SPACE INVADERS\\ufo.png")
pygame.display.set_icon(icon)
testX=10
testY=10

# Player
playerImg = pygame.image.load("C:\\Users\\HP\\CODE\\VS-CODE\\PYTHON\\GAMES\\images\\SPACE INVADERS\\player.png")
playerX = 370
playerY = 480
playerX_change = 0

def player(X,Y):
    screen.blit(playerImg,(X,Y))

def show_score(X,Y):
    score = font.render("Score:",+str(score_value),True,(225,225,225))
    score.blit(score,(X,Y))
# Game loop
running = True
while running:
    # RGB = Red,Green,Blue
    screen.fill((0,0,0))
    
    # Background image 
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            running = False
    player(playerX,playerY)
    show_score(testX,testY)
    pygame.display.update()
    
    
