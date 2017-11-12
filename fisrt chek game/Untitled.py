# Code designed and written by: Rania ElSharafa
# Andrew ID: relshara
# File Created: November 7, 5:00pm
# Modification History:
# Start          End
# 7/11  5:00pm   7/11  10:00pm
# 8/11  6:00pm   8/11  11:00pm
# 10/11 8:00pm   10/11 10:00pm
# 11/11 5:00pm   11/11 01:00pm
# 12/11 10:30am  12/11 12:30pm

#importing libraries 
import pygame
import os
import random

from pygame.locals import *

#initiating pygame window
pygame.init()
height = 800
width = 600
clock_speed = 150
#setting size for the window
window = pygame.display.set_mode((width, height))
#setting caption
pygame.display.set_caption('Mr. Potato')
#loading gameplay background
background=pygame.image.load("background.jpg").convert()
#loading menu backgrounds
interface=pygame.image.load("interface2.jpg").convert()
instructions=pygame.image.load("instructions.jpg").convert()
#loading characters for each level
#character1=pygame.image.load("char1.png").convert()
character2=pygame.image.load("char2.png").convert()
character3=pygame.image.load("char3.png").convert()
character4=pygame.image.load("char4.png").convert()
character5=pygame.image.load("char5.png").convert()
character6=pygame.image.load("char6.png").convert()
character7=pygame.image.load("char7.png").convert()
character8=pygame.image.load("char8.png").convert()
#loading the falling objects
monster=pygame.image.load("monster.png").convert()

#loading and playing background music
music=pygame.mixer.Sound("music.wav")
music.play(-1)
music.set_volume(0.5)

game = 1
#function to move the character moving horozintaly 
def movePotatoH(potato,direction):
    #initilize the tuples and dictionaries to the key values for the size and the postion
    (sw,sh) = potato['size']
    (px,py) = potato['pos']
    speed = potato['speed']
    velocity = speed*direction
    #cheaking id the player has pressed either left or right keyboard buttons and if so it will
    #move according to the x and y direction that we have caculated
    if direction == -1:
        if px >= 15:
            potato['pos'] = (px + velocity,py)
    elif direction == 1:
        if px <= width-sw-15:
            potato['pos'] = (px + velocity,py)
    
#function to move the character moving vertically
def movePotatoV(potato,direction):
    (sw,sh) = potato['size']
    (px,py) = potato['pos']
    speed = potato['speed']
    velocity = speed*direction
    if direction == -1:
        if py >= 15:
            potato['pos'] = (px, py + velocity)
    elif direction == 1:
        if py <= height-sh-15:
            potato['pos'] = (px, py + velocity)
while game == 1:
    #assignig empty dictionary
    objects= {}
    #pytting dictionaries inside another dixrionaries that will help us later while calling the keys
    #and values
    objects['potato']={}
    #setting the postion the the character
    objects['potato']['pos'] = (275,700)
    #setting the size of the chrachter
    objects['potato']['size']= (50,80)
    #setting the speed of the chrachter
    objects['potato']['speed']= 7
    #letting the charchter to be falling down and bring them to the top of the back ground
    objects['potato']['img']=pygame.transform.scale(pygame.image.load("char1.png").convert_alpha(),objects['potato']['size'])
    #assging varibles
    monstersOutOfRange=[]
    monsterCount = 0
    monsterID = 0
    #function to set the time of proccesing the game
    clock=pygame.time.Clock()
    menu=1
    #making while loop for the the main munue to be open first
    while menu==1:
        main_menu = 1
        instructions_menu = 0
        while main_menu == 1:
            #function to set the buttons in the mune
            for event in pygame.event.get():
                #if statment to check if the user want to quit the game then we assign varibles
                #that will help us in other tasks
                if event.type is QUIT:
                    game = 0
                    gameplay = 0
                    menu = 0
                #cheking if the user has presses with the mouse a specific button 
                elif event.type == MOUSEBUTTONDOWN:
                    #function to get the postion the mouse
                    mousePosition = pygame.mouse.get_pos()
                    (mx,my) = mousePosition
                    #cheking if a specific button either (start button or main menue button)
                    if 180 < mx < 395 and 205 < my < 267:
                        gameplay= 1
                        menu = 0
                        main_menu=0
                    if 177 < mx < 396 and 315 < my < 379:
                        main_menu = 0
                        instructions_menu = 1
            #function to blit the interface
            window.blit(interface,(0,0))
            #function to flip 
            pygame.display.flip()
        #while loop for the instruction window
        while instructions_menu == 1:
            for event in pygame.event.get():
                if event.type is QUIT:
                    #assigning varibles
                    game = 0
                    gameplay = 0
                    menu = 0
                 #chaking if we moves the mouse button   
                elif event.type == MOUSEBUTTONDOWN:
                    mousePosition = pygame.mouse.get_pos()
                    (mx,my) = mousePosition
                    #if statemt to cheak if we pressed specific x and y coordinates and if so
                    #it will assign varibles that will help us later in other tasks
                    if 420 < mx < 574 and 733 < my < 786:
                        gameplay= 1
                        menu = 0
                        instructions_menu=0
                    if 16 < mx < 170 and 733 < my < 786:
                        main_menu = 1
                        instructions_menu = 0
            window.blit(instructions,(0,0))
            pygame.display.flip()

        
    while gameplay==1:
        clock.tick(clock_speed)
        for event in pygame.event.get():
            if event.type is QUIT:
                game = 0
                gameplay = 0
        #cheaking which key is pressed if it is down up or right or left
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            movePotatoH(objects['potato'],-1)
            
        if keys[pygame.K_RIGHT]:
            movePotatoH(objects['potato'],1)
        if keys[pygame.K_UP]:
            movePotatoV(objects['potato'],-1)
            
        if keys[pygame.K_DOWN]:
            movePotatoV(objects['potato'],1)
        #moster falling from the top
        if monsterCount <= 4:
            monsterID += 1
            #using random so the monters can fall down from random places
            RandomizedXPos = random.randrange(10,550)
            #using dictionaries and adding dictuires to dictionares so we can get the valuse and the keys
            #this will make it easier to do other tasks
            objects['monster'+str(monsterID)] = {}
            objects['monster'+str(monsterID)]['pos'] = [RandomizedXPos, -40]
            objects['monster'+str(monsterID)]['size']= (40,40)
            objects['monster'+str(monsterID)]['speed']= 4
            #letting the monster bring it infront the back ground and intert it
            objects['monster'+str(monsterID)]['img']=pygame.transform.scale(pygame.image.load("monster.png").convert_alpha(),objects['monster'+str(monsterID)]['size'])
        monsterCount = 0
        window.blit(background,(0,0))
        #letting the charachters togather in the screen the falling monsters and ms.potato
        for char in objects:
            #cheaking if monters is in the dictionary and if so it will fall down  accrding to the speed and size
            #that we have assin
            if char[0:7] == "monster":
                if not objects[char]['pos'][1] > height:
                    monstersOutOfRange += [char]
                    objects[char]['pos'] = (objects[char]['pos'][0],objects[char]['pos'][1]+objects[char]['speed'])
                    window.blit(objects[char]['img'], objects[char]['pos'])
                    monsterCount+= 1
            elif char=='potato':
                window.blit(objects[char]['img'], objects[char]['pos'])


        #diaplying the charchter and back ground
        pygame.display.flip()
    



#function to quit pygame 
pygame.quit()
