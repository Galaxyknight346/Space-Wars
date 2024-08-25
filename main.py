from tkinter.tix import MAX
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import pygame
import os
pygame.font.init()
pygame.mixer.init()
import sys
import random
import time
from PIL import ImageTk, Image

resolutionA, resloutionB = 1920, 1080

#Start Menu(Created on tkinter)

import tkinter as tk



root = tk.Tk()
root.title("Space Wars")
w = (resolutionA)/1.9 #1,129.4
h = (resloutionB)/1.7 #635.3
root.resizable(False, False)



ws = root.winfo_screenwidth() 
hs = root.winfo_screenheight() 


x = (ws/2) - (w/2)
y = (hs/2) - (h/2)



root.geometry('%dx%d+%d+%d' % (w, h, x, y))



titleFont = Font(family = "Raleway", size = 42, weight = "bold", underline = 0, overstrike = 0)

title_label = tk.Label(root, text = "Space Wars", font = titleFont, padx = 240)

title_img = ImageTk.PhotoImage(Image.open("/Users/shrishvishnu/Desktop/Computer Science/SpaceWars/Assets/title_img.png"))
title_img_label = tk.Label(root, image=title_img, padx = 3)
title_img_label.grid(row=0, column = 3)

yellow_label = tk.Label(root, text = "Player 1 Name: ", padx = 30)
yellow_label.grid(row=1, column=0)

entry_yellow = tk.Entry(root)
entry_yellow.grid(row = 2, column=0, padx = 8)

yellow_ship_label1 = tk.Label(root, text = "Player 1 Ship Info: ")
yellow_ship_label1.grid(row = 3, column = 0)

yellow_ship_label2 = tk.Label(root, text = "Ship Name: Yellow 3x01")
yellow_ship_label2.grid(row = 4, column = 0)

yellow_ship_label_image = ImageTk.PhotoImage(Image.open("/Users/shrishvishnu/Desktop/Computer Science/SpaceWars/Assets/yellow_label_spaceship.png"))
yellow_ship_label3 = tk.Label(root, image = yellow_ship_label_image)
yellow_ship_label3.grid(row=5, column = 0)

yellow_label4 = tk.Label(root, text = "Spaceship Health: 20")
yellow_label4.grid(row=6, column=0)



red_label = tk.Label(root, text = "Player 2 Name: ")
red_label.grid(row = 1, column = 5)

entry_red = tk.Entry(root)
entry_red.grid(row = 2, column = 5)

red_ship_label1 = tk.Label(root, text = "Player 2 Ship Info: ")
red_ship_label1.grid(row=3, column = 5)

red_ship_label2 = tk.Label(root, text = "Ship Name: Red 45po2")
red_ship_label2.grid(row=4, column = 5)

red_ship_label_image = ImageTk.PhotoImage(Image.open("/Users/shrishvishnu/Desktop/Computer Science/SpaceWars/Assets/red_label_spaceship.png"))
red_ship_label3 = tk.Label(root, image=red_ship_label_image)
red_ship_label3.grid(row=5, column = 5)

red_ship_label4 = tk.Label(root, text = "Spaceship Health: 20")
red_ship_label4.grid(row=6, column = 5)

instructions1 = "Welcome to Space Wars! Enter each players name, and press the play button.\nPlayer 1 will have the yellow spaceship, and Player 2 will have the red one.\nPlayer 1: Use WASD to move, and 'C' to shoot.\nPlayer 2: Use the Arrow Keys to move, and 'K' to shoot.\nThe game will reset once a ship reaches 0 health.\nGood luck and have fun!"
instructions_label = tk.Label(root, text = instructions1)
instructions_label.grid(row=3, column = 3)



def makeNames():
    global yellow_player
    global red_player
    yellow_player = entry_yellow.get()
    red_player = entry_red.get()

    root.quit()


start = tk.Button(root, text = "Play!", command=makeNames)
start.grid(row=6, column = 3)





root.mainloop()

root.quit()



#Window Variables
WIDTH, HEIGHT = (resolutionA)/1.5, (resloutionB)/1.5
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Wars")
icon = pygame.image.load(r'/Users/shrishvishnu/Desktop/Computer Science/SpaceWars/Assets/rocket-icon.png')
pygame.display.set_icon(icon)
CYAN = (200, 255, 255)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('/Users/shrishvishnu/Desktop/Computer Science/SpaceWars/Assets', 'spacewarsbg4.jpg')), (WIDTH, HEIGHT))

#Collision Events
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
ABILITY_HIT = pygame.USEREVENT + 3

#Ability Variables(FYI: Abilities will be added once I figure out more aobut pygame)
ABILITY_HEIGHT = 60
ABILITY_WIDTH = 60
ABILITY_IMAGE = pygame.image.load(os.path.join('/Users/shrishvishnu/Desktop/Computer Science/SpaceWars/Assets', 'heal.png'))
ABILITY_IMAGE = pygame.transform.scale(ABILITY_IMAGE, (60, 60))
ABILITY_RECT = ABILITY_IMAGE.get_rect()

#Spaceship Control Variables
FPS = 60
spaceH, spaceW = 11,8
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = spaceH*15, spaceW*15
VEL = 15



#Bullet Variables
BULLET_VEL = 25
MAX_BULLETS = 3
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
RED_BULLET_IMAGE = pygame.image.load(os.path.join('/Users/shrishvishnu/Desktop/Computer Science/SpaceWars/Assets', 'red_bullet.jpg'))
RED_BULLET_IMAGE = pygame.transform.scale(RED_BULLET_IMAGE, (10, 20))
YELLOW_BULLET_IMAGE = pygame.image.load(os.path.join('/Users/shrishvishnu/Desktop/Computer Science/SpaceWars/Assets', 'yellow_bullet.png'))
YELLOW_BULLET_IMAGE = pygame.transform.scale(YELLOW_BULLET_IMAGE, (10, 20))




#Border Variables
BORDER = pygame.Rect((WIDTH//2)-(5/2), 0, 8, HEIGHT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BORDER_COLOR = CYAN

#Sound Variables
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('/Users/shrishvishnu/Desktop/Computer Science/SpaceWars/Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('/Users/shrishvishnu/Desktop/Computer Science/SpaceWars/Assets', 'Gun+Silencer.mp3'))

#Text Variables
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)



#Spaceship Variables
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('/Users/shrishvishnu/Desktop/Computer Science/SpaceWars/Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate((pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))), 90)
YELLOW_RECT = YELLOW_SPACESHIP.get_rect()
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('/Users/shrishvishnu/Desktop/Computer Science/SpaceWars/Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate((pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))), 270)
RED_RECT = RED_SPACESHIP.get_rect()
ycoords = ()

#def handle_abilities(ability, ability_s, yellow, red):
    #if(ability_s):
        #WIN.blit(ABILITY_IMAGE, (ability.x, ability.y))
        #pygame.display.update()
    #if(pygame.Rect.colliderect(ability, yellow)):
        #pygame.event.post(pygame.event.Event(ABILITY_HIT))
    #pygame.display.update()

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, ticks, ability, ability_s):
    WIN.blit(SPACE, (0,0))
    pygame.draw.rect(WIN, BORDER_COLOR, BORDER)

    red_health_text = HEALTH_FONT.render(red_player + "'s Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(yellow_player + "'s Health: "+ str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    
    #handle_abilities(ability, ability_s, yellow, red)
    
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
        #Left
        if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
            yellow.x -= VEL
        #Right
        if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
            yellow.x += VEL
        #Up
        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
            yellow.y -= VEL
        #Down
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 20:
            yellow.y += VEL

def red_handle_movement(keys_pressed, red):
        #Left
        if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
            red.x -= VEL
        #Right
        if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:
            red.x += VEL
        #Up
        if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
            red.y -= VEL
        #Down
        if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 20:
            red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)



def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    pygame.init()
    pygame.time.delay(500)
    red = pygame.Rect(950, 450, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 150, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    ability = pygame.Rect(100, 100, 60, 60)
    ability_s= True

    yellow_bullets = []
    red_bullets = []

    red_health = 20
    yellow_health = 20
    healths = [red_health, yellow_health]

    #Abilitiy 1 Function 
    def increase_health():
        yellow_health+= 2
        red_health += 2
    
    abilities = [increase_health]

    def choose_ability(yellow_health, red_health):
        r = random.randint(1, 3)
        if(r == 1):
            yellow_health += 2
            red_health += 2
        elif(r == 2):
            pass
        else:
            pass


            

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        ticks = pygame.time.get_ticks()  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 30, 15)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()


                if event.key == pygame.K_k and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 30, 15)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()
                    
                
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
            
            if event.type == ABILITY_HIT:
                choose_ability(yellow_health, red_health)

        winner_text = ""
        
        if(ticks % 300 == 0):
           ability_s = True

        if red_health==0:
            time.sleep(0.3)
            pygame.display.update()
            winner_text = yellow_player + " Wins!"

        
        if yellow_health == 0:
            time.sleep(0.3)
            pygame.display.update()
            winner_text = red_player + " Wins!"
        
        if winner_text != "":
            draw_winner(winner_text)
            break


        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        


        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, ticks, ability, ability_s)




    main()


if __name__ == "__main__":
    main()