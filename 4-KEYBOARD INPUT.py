import math 
import random  #used fpor randomly placing enemy ships  
import pygame 
from pygame import mixer
from pygame.locals import *


# Initializing pyagme 
pygame.init()

# create the screen 
screen = pygame.display.set_mode((800,600)) 

# importing the background images 
background = pygame.image.load("C:\\Users\\HP\\CODE\\VS-CODE\\PYTHON\\GAMES\\images\\SPACE INVADERS\\background.png")

# importing sounds 
mixer.music.load('C:\\Users\\HP\\CODE\\VS-CODE\\PYTHON\\GAMES\\images\\SPACE INVADERS\\background.wav') # for importing sounds 
# mixer.music.play(-1)

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
    screen.blit(playerImg, (x,y))
    

    
def show_score(x,y):
    score = font.render("Score :" +str(score_value),True,(225,225,225))
    screen.blit(score,(x,y))
    
# Game loop
running = True
while running:
    # RGB = Red,Green,Blue
    screen.fill((0,0,0))
    
    # Background image 
    screen.blit(background,(0,0))
    
    # handle keyboard input 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke(input given ) is pressed checki whether its right or left 
        if event.type == pygame.KEYDOWN:
            # left key
            if event.key == pygame.K_LEFT:
                playerX_change = -5
                
            # right key
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            # shoot 
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("C:\\Users\\HP\\CODE\\VS-CODE\\PYTHON\\GAMES\\images\\SPACE INVADERS\\laser.wav")
                    bulletSound.play() 
                    # Get current coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)  
        
        # stop movement if key is released
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0     # to stop movement  when no inputs 
    
    # update player positions 
    playerX+= playerX_change
    
    # limit movement 
    if playerX <=0:
        playerX=0
        # limiting the movement of the spaceship acc to the screen
    elif playerX >=736:
        playerX =736      
    
    # draw player    
    player(playerX,playerY)
    
    # show font 
    show_score(textX,testY)
    
    # update screen 
    pygame.display.update()