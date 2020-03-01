import pygame
from pygame.locals import Color,Rect
import os
from player import Player
from game import Game
import game_utils
import end_screen
import menu

pygame.init()
#pygame.mixer.init()

highest_score = 0

W, H = 1024, 800
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Malfunctioning Penguin')

clock = pygame.time.Clock()

music_filename = menu.main_menu()
run = True
current_screen = "game_screen"
game = Game(win)

print(music_filename)
pygame.mixer.music.load(music_filename)
pygame.mixer.music.play(-1)


while run:
    delta_time = clock.get_time()/1000
    frame_time = pygame.time.get_ticks()

    if current_screen == "game_screen":
        game_score = game.tick()
        if game_score:
            current_screen = "game_over"
                
    if current_screen == "game_over":
        restart = end_screen.endScreen(game_score)
        if restart:
            current_screen = "game_screen"
            game = Game(win)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    clock.tick(60)
