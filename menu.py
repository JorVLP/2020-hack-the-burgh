from pygame.locals import *
import pygame
import time
import random
import os
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import game_utils

# The root window is created
root = tk.Tk()
root.withdraw()

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
bright_red = (255,0,0)
bright_green = (0,255,0)

# Game Fonts
font = 'Retro'


# Game image
background_img = pygame.image.load("./images/icy_background.png")
penguin_img = pygame.image.load(os.path.join('images', 'penguinTitle.png'))

# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.SysFont(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText

#Main Menu
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
                if event.key==pygame.K_SPACE:
                    if selected=="start":
                        global audio_file_name
                        audio_file_name = filedialog.askopenfilename(filetypes=(("Audio Files", ".wav .ogg .mp3"),   ("All Files", "*.*")))
                        pygame.display.update()
                        game_utils.set_func(audio_file_name)
                        root.withdraw()
                        root.destroy()
                        return audio_file_name
                    if selected=="quit":
                        pygame.quit()
                        quit()
 
        # Main Menu UI
        #screen.fill(white)
        screen.blit(background_img, (0,0))
        title=text_format("Malfunctioning Penguin", font, 90, blue)
        screen.blit(penguin_img, (262, 100))
        if selected=="start":
            text_start = text_format("START", font, 75, red)
            text_file1 = text_format("(This game is procedurally generated from an audio file,", font, 30, red)
            text_file2 = text_format("so upload your favourite tune and glide away!)", font, 30, red)
        else:
            text_start = text_format("START", font, 75, black)
            text_file1 = text_format("(This game is procedurally generated from an audio file,", font, 30, black)
            text_file2 = text_format("so upload your favourite tune and glide away!)", font, 30, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, red)
        else:
            text_quit = text_format("QUIT", font, 75, black)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        file1_rect=text_file1.get_rect()
        file2_rect=text_file2.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), screen_height // 2 + 120))
        screen.blit(text_file1, (220, screen_height // 2 + 170))
        screen.blit(text_file2, (280, screen_height // 2 + 190))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), screen_height // 2 + 250))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Malfunctioning Penguin - Music-Generated Gliding Game")

if __name__ == '__main__':
    pygame.mixer.music.load('sounds/PFUDOR.mp3')
    pygame.mixer.music.play(-1)
    main_menu()

