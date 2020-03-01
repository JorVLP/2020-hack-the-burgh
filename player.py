import pygame
import os

class Player(object):

    def __init__(self, win):
        self.face_left = pygame.image.load(os.path.join('images', 'penguinLeft.png'))
        self.face_right = pygame.image.load(os.path.join('images', 'penguinRight.png'))
        self.PENG_WIDTH = self.face_left.get_width()
        self.PENG_HEIGHT = self.face_left.get_height()
        self.x = (win.get_width()-self.PENG_WIDTH)/2
        self.y = win.get_height()-self.PENG_HEIGHT-30
        self.width = self.face_left.get_width()
        self.height = self.face_left.get_height()
        self.go_left = True
        self.center = (win.get_width()//2,win.get_height()-30-(self.PENG_HEIGHT//2))

    def change_direction(self):
        self.go_left = not self.go_left

    def draw(self, win):
        if self.go_left:
            win.blit(self.face_left, (self.x, self.y))
        else:
            win.blit(self.face_right, (self.x, self.y))

        #pygame.draw.rect(win, (255,0,0),self.hitbox, 2)