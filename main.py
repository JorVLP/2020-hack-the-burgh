import pygame
from pygame.locals import Color,Rect
import os
from player import Player
from game import Game
import game_utils

pygame.init()

W, H = 1024, 800
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Malfunctioning Penguin')

def endScreen():
    global pause
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
        game_over = largeFont.render('Game Over',1,(0,0,0))
        plushie = largeFont.render('Where\'s my plushie..? :( ',1,(0,0,0))

        crying = pygame.image.load(os.path.join('images', 'cryingPinguin.png'))
        win.blit(crying, (W/2.5, H/2))
        win.blit(game_over, (W/2 - game_over.get_width()/2,150))
        win.blit(plushie, (W/2 - plushie.get_width()/2, 240))
        pygame.display.update()

clock = pygame.time.Clock() 
run = True
current_screen = "game_screen"
game = Game(win)

while run:
    delta_time = clock.get_time()/1000
    frame_time = pygame.time.get_ticks()

    if current_screen == "game_screen":
        if game.tick():
            endScreen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    clock.tick(60)
