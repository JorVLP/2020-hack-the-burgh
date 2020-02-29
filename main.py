import pygame
from pygame.locals import *
import os
import random
from Player import Player
import game_utils

pygame.init()

W, H = 1024, 800
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Malfunctioning Penguin')

orig_bg = pygame.image.load(os.path.join('images', 'background.png')).convert()
bg_width = orig_bg.get_width()
bg_height = orig_bg.get_height()

backgrounds = [orig_bg.copy() for i in range(4)]
bg_ystart = 0
bg_yend = bg_height
bg_xstart = 0
bg_xend = bg_width

clock = pygame.time.Clock()
WHITE = (255, 255, 255)
font_name = pygame.font.match_font('arial')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

    





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
    score = 0

def redrawWindow():

    win.blit(backgrounds[0], (bg_xstart,bg_ystart))
    win.blit(backgrounds[1], (bg_xend,bg_ystart))
    win.blit(backgrounds[2], (bg_xstart,bg_yend))
    win.blit(backgrounds[3], (bg_xend,bg_yend))
    draw_text(win, str(round(frame_time/1000)), 25, W-50, 10)
    
    penguin.draw(win)
    # largeFont = pygame.font.SysFont('comicsans', 30)
    # text = largeFont.render('Score: ' + str(score), 1, (255,255,255))
    # win.blit(text, (700, 10))
    pygame.display.update()


score = 0

run = True
PENG_WIDTH = 123
PENG_HEIGHT = 110
penguin = Player((win.get_width()-PENG_WIDTH)/2, win.get_height()-PENG_HEIGHT-30, 50, 50)


game_over = False

direction = 1
last_dir_flip = 0
pygame.draw.rect(backgrounds[0],Color(255,0,0),Rect(0,0,10,10))
pygame.draw.rect(backgrounds[1],Color(0,255,0),Rect(0,0,10,10))
pygame.draw.rect(backgrounds[2],Color(0,0,255),Rect(0,0,10,10))
pygame.draw.rect(backgrounds[3],Color(0,0,0),Rect(0,0,10,10))



y_speed = 4
x_speed = 6

screen_x = 0
screen_y = 0

path_radius = 50
path_x = bg_width//2

while run:
    delta_time = clock.get_time()/1000
    frame_time = pygame.time.get_ticks()

    screen_y += y_speed
    screen_x += x_speed * direction

    if game_over:
        endScreen()

    # scrolling of the background
    bg_ystart += y_speed
    bg_yend += y_speed
    if bg_ystart > bg_height:
        bg_ystart = bg_ystart - 2*bg_height
        backgrounds[0] = orig_bg.copy()
        backgrounds[1] = orig_bg.copy()
    if bg_yend > bg_height:
        bg_yend = bg_yend - 2*bg_height
        backgrounds[2] = orig_bg.copy()
        backgrounds[3] = orig_bg.copy()

    bg_xstart += x_speed * direction
    bg_xend += x_speed * direction
    if bg_xstart > bg_width:
        bg_xstart = bg_xstart - 2*bg_height
    if bg_xstart < bg_width * -1:
        bg_xstart = bg_xstart + 2*bg_height
    if bg_xend > bg_width:
        bg_xend = bg_xend - 2*bg_height
    if bg_xend < bg_width * -1:
        bg_xend = bg_xend + 2*bg_height

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if frame_time - last_dir_flip > 200:
            direction *= -1
            penguin.change_direction()
            last_dir_flip = frame_time


    (path_x,path_radius) = game_utils.plot_path(frame_time)

    plot_list = game_utils.get_screen(path_x,-screen_y,bg_width,bg_height,path_radius)

    for (i,x,y) in plot_list:
        pygame.draw.circle(backgrounds[i],Color(255,255,255),(x,y),path_radius)


    clock.tick(60)
    redrawWindow()
