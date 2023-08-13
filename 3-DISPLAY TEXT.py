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
# score 
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)   # to lower fonts 
textX = 10
testY = 10

# Player
playerImg = pygame.image.load("C:\\Users\\HP\\CODE\\VS-CODE\\PYTHON\\GAMES\\images\\SPACE INVADERS\\player.png")
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))
    
def show_score(x,y):
    score_value =0
    score = font.render("Score :" +str(score_value),True,(225,225,225))
    screen.blit(score,(x,y))
# Game loop
running = True
while running:
    # RGB = Red,Green,Blue
    screen.fill((0,0,0))
    
    # Background image 
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    player(playerX,playerY)
    show_score(textX,testY)
    # To show random text 
    score = font.render("HELLO WORLD !",True,(225,0,0))
    screen.blit(score,(100,100))
    pygame.display.update()