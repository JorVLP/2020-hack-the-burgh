import pygame
import os

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