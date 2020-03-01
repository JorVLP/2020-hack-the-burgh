import pygame
from pygame.locals import Color,Rect
import os
from player import Player
from game import Game
import game_utils
import end_screen
import win_screen
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
pygame.mixer.music.play()


while run:
    delta_time = clock.get_time()/1000
    frame_time = pygame.time.get_ticks()

    if current_screen == "game_screen":
        game_score = game.tick()
        if game_score > 0:
            print("HHHHHHH")
            pygame.mixer.music.stop()
            current_screen = "game_over"
        elif game_score == -1:
            pygame.mixer.music.stop()
            effect = pygame.mixer.Sound("./sounds/applause.wav")
            effect.play()
            win_screen.winScreen()
                
    if current_screen == "game_over":
        effect = pygame.mixer.Sound("./sounds/splash_2.wav")
        effect.play()
        restart = end_screen.endScreen(game_score)
        if restart:
            current_screen = "game_screen"
            game = Game(win)
            pygame.mixer.music.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    clock.tick(60)
