import pygame
from pygame.locals import *
import time
import random
import os

# Game Initialization
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width = 1024
screen_height = 800
screen=pygame.display.set_mode((screen_width, screen_height))

# Colors
white=(255, 255, 255)
black=(33,54,72)
gray=(50, 50, 50)
red=(234,65,123)
green=(0, 255, 0)
blue=(122,246,246)
yellow=(255, 255, 0)
 

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.SysFont(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText


# Game Fonts
font = 'Retro'


# Game image
penguin_img = pygame.transform.scale(pygame.image.load("./images/penguinTitle.png"), (460,460))


# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Main Menu
def main_menu():
 
    menu=True
    selected="start"
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        print("Start")
                    if selected=="quit":
                        pygame.quit()
                        quit()
 
        # Main Menu UI
        screen.fill(white)
        title=text_format("Malfunctioning Penguin", font, 90, blue)
        screen.blit(penguin_img, (262, 120))
        if selected=="start":
            text_start=text_format("START", font, 75, red)
        else:
            text_start = text_format("START", font, 75, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, black)
        else:
            text_quit = text_format("QUIT", font, 75, black)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), screen_height // 2 + 150))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), screen_height // 2 + 250))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")

        while True:
            for event in pygame.event.get():
                if(start_rect.collidepoint(pygame.mouse.get_pos())):
                    pygame.quit()
                    quit()
                if(event.type == pygame.MOUSEBUTTONDOWN and event.start_rect== 1):
                    pygame.quit()
                    quit()
                elif(event.type == pygame.MOUSEBUTTONDOWN and event.quit_rect==1):
                    pygame.quit()
                    quit()
                elif(event.type == pygame.QUIT):
                    pygame.quit()
                    quit()

main_menu()
