from pygame.locals import *
import pygame
import time
import random
import os
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

def endScreen():
    global pause, score
    pause = 0

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        win.blit(win, (0,0))
        largeFont = pygame.font.SysFont('comicsans', 80)
        # lastScore = largeFont.render('Best Score: ' + str(updateFile()),1,(255,255,255))
        # currentScore = largeFont.render('Score: '+ str(score),1,(255,255,255))
        game_over = largeFont.render('Game Over',1,(0,0,0))
        plushie = largeFont.render('Where\'s my plushie..? :( ',1,(0,0,0))

        crying = pygame.image.load(os.path.join('images', 'cryingPinguin.png'))
        win.blit(crying, (W/2.5, H/2))
        win.blit(game_over, (W/2 - game_over.get_width()/2,150))
        win.blit(plushie, (W/2 - plushie.get_width()/2, 240))
        pygame.display.update()
        tear = pygame.image.load(os.path.join('images', 'tear.png'))
        x_tear = 512
        y_tear = 400
        for i in range(0, 400):
            if i%4==0:
                win.blit(tear, (x_tear, y_tear+(i/4)))
                pygame.display.update()
    score = 0

endScreen()