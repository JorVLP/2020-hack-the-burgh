import pygame
from pygame.locals import *
import os
import random

pygame.init()

W, H = 500, 800
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Malfunctioning Penguin')

orig_bg = pygame.image.load(os.path.join('images', 'background.png')).convert()
bg = orig_bg.copy()
bg_ystart = 0
bg_yend = bg.get_height()
bg_xstart = 0
bg_xend = bg.get_width()

clock = pygame.time.Clock()
WHITE = (255, 255, 255)
font_name = pygame.font.match_font('arial')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)



class Player(object):
    face_left = pygame.image.load(os.path.join('images', 'penguinLeft.png'))
    face_right = pygame.image.load(os.path.join('images', 'penguinRight.png'))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.go_left = True
    
    def change_direction(self):
        self.go_left = not self.go_left

    def draw(self, win):
        if self.go_left:
            win.blit(self.face_left, (self.x, self.y))
        else:
            win.blit(self.face_right, (self.x, self.y))

        #pygame.draw.rect(win, (255,0,0),self.hitbox, 2)

def endScreen():
    global pause, score, obstacles
    pause = 0
    obstacles = []

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        win.blit(bg, (0,0))
        largeFont = pygame.font.SysFont('comicsans', 80)
        lastScore = largeFont.render('Best Score: ' + str(updateFile()),1,(255,255,255))
        currentScore = largeFont.render('Score: '+ str(score),1,(255,255,255))
        win.blit(lastScore, (W/2 - lastScore.get_width()/2,150))
        win.blit(currentScore, (W/2 - currentScore.get_width()/2, 240))
        pygame.display.update()
    score = 0

def redrawWindow():

    win.blit(bg, (bg_xstart,bg_ystart))
    win.blit(bg, (bg_xend,bg_yend))
    win.blit(bg, (bg_xstart,bg_yend))
    win.blit(bg, (bg_xend,bg_ystart))
    
    penguin.draw(win)
    for obstacle in obstacles:
        obstacle.draw(win)

    pygame.draw.rect(win,Color(0,255,0),Rect(0,bg_ystart,100,10))
    pygame.draw.rect(win,Color(255,0,0),Rect(50,bg_yend,100,10))
    largeFont = pygame.font.SysFont('comicsans', 30)
    text = largeFont.render('Score: ' + str(score), 1, (255,255,255))


    win.blit(text, (700, 10))
    pygame.display.update()


pygame.time.set_timer(USEREVENT+1, 500)
pygame.time.set_timer(USEREVENT+2, 3000)

score = 0

run = True
PENG_WIDTH = 123
PENG_HEIGHT = 110
penguin = Player((win.get_width()-PENG_WIDTH)/2, win.get_height()-PENG_HEIGHT-30, 50, 50)

obstacles = []
pause = 0
fallSpeed = 0

direction = 1
last_dir_flip = 0

while run:
    delta_time = clock.get_time()/1000
    frame_time = pygame.time.get_ticks()

    #draw_text(win, frame_time/1000, 18, 300, 10)

    if pause > 0:
        pause += 1
        if pause > fallSpeed * 2:
            endScreen()


    # scrolling of the background
    bg_ystart += 2
    bg_yend += 2
    if bg_ystart > bg.get_height():
        bg_ystart = bg_ystart - 2*bg.get_height()
    if bg_yend > bg.get_height():
        bg_yend = bg_yend - 2*bg.get_height()

    bg_xstart += 2 * direction
    bg_xend += 2 * direction
    if bg_xstart > bg.get_width():
        bg_xstart = bg_xstart - 2*bg.get_height()
    if bg_xstart < bg.get_width() * -1:
        bg_xstart = bg_xstart + 2*bg.get_height()
    if bg_xend > bg.get_width():
        bg_xend = bg_xend - 2*bg.get_height()
    if bg_xend < bg.get_width() * -1:
        bg_xend = bg_xend + 2*bg.get_height()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

        if event.type == USEREVENT+1:
            pass


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if frame_time - last_dir_flip > 200:
            direction *= -1
            penguin.change_direction()
            last_dir_flip = frame_time

    if keys[pygame.K_DOWN]:
        pass

    clock.tick(60)
    redrawWindow()
