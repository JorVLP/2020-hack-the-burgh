import pygame
from pygame.locals import Color,Rect
import os
from player import Player
from game import Game
import game_utils
import end_screen

pygame.init()

W, H = 1024, 800
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Malfunctioning Penguin')

clock = pygame.time.Clock() 
run = True
current_screen = "game_screen"
game = Game(win)

while run:
    delta_time = clock.get_time()/1000
    frame_time = pygame.time.get_ticks()

    if current_screen == "game_screen":
        if game.tick():
            end_screen.endScreen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    clock.tick(60)
