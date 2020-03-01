import pygame
import game_utils
from pygame.locals import Color,Rect
import os
from player import Player
import random



class Game():

    def __init__(self, window):
        self.win = window
        self.orig_bg = pygame.image.load(os.path.join('images', 'background.png')).convert()
        self.bg_width = self.orig_bg.get_width()
        self.bg_height = self.orig_bg.get_height()
        self.backgrounds = [self.orig_bg.copy() for i in range(4)]
        self.bg_ystart = 0
        self.bg_yend = self.bg_height
        self.bg_xstart = 0
        self.bg_xend = self.bg_width
        self.penguin = Player(window)
        self.game_over = False
        self.direction = 1
        self.y_speed = 4
        self.x_speed = 4
        self.screen_x = self.bg_width//2
        self.screen_y = 0
        self.last_dir_flip = 0
        self.game_start_time = pygame.time.get_ticks()
        self.score = 0
        self.flag = 0
        self.increment = 0
        self.last_decoration = 7000
        filenames = ["seal.png", "narwhal.png", "waterbottle.png", "garbage.png","sealRight.png"]
        self.seals = [pygame.image.load(os.path.join('images', name)) for name in filenames] 
        pygame.draw.rect(self.backgrounds[0],Color(255,255,255),Rect(0,0,2048,2048))
        pygame.draw.rect(self.backgrounds[1],Color(255,255,255),Rect(0,0,2048,2048))
        pygame.draw.rect(self.backgrounds[0],Color(0,0,0),Rect(0,0,2048,5))
        pygame.draw.rect(self.backgrounds[1],Color(0,0,0),Rect(0,0,2048,5))


    def tick(self):
        frame_time = pygame.time.get_ticks()

        self.screen_y += self.y_speed
        self.screen_x += self.x_speed * self.direction

        self.bg_ystart += self.y_speed
        self.bg_yend += self.y_speed
        if self.bg_ystart > self.bg_height:
            self.bg_ystart = self.bg_ystart - 2*self.bg_height
            self.backgrounds[0] = self.orig_bg.copy()
            self.backgrounds[1] = self.orig_bg.copy()
        if self.bg_yend > self.bg_height:
            self.bg_yend = self.bg_yend - 2*self.bg_height
            self.backgrounds[2] = self.orig_bg.copy()
            self.backgrounds[3] = self.orig_bg.copy()

        self.bg_xstart += self.x_speed * self.direction
        self.bg_xend += self.x_speed * self.direction
        if self.bg_xstart > self.bg_width:
            self.bg_xstart = self.bg_xstart - 2*self.bg_height
        if self.bg_xstart < self.bg_width * -1:
            self.bg_xstart = self.bg_xstart + 2*self.bg_height
        if self.bg_xend > self.bg_width:
            self.bg_xend = self.bg_xend - 2*self.bg_height
        if self.bg_xend < self.bg_width * -1:
            self.bg_xend = self.bg_xend + 2*self.bg_height

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if frame_time - self.last_dir_flip > 200:
                self.direction *= -1
                self.penguin.change_direction()
                self.last_dir_flip = frame_time

        if keys[pygame.K_DOWN]:
            self.game_over = True

        # draw background
        game_time = pygame.time.get_ticks() - self.game_start_time
        (path_x, path_radius) = game_utils.plot_path(game_time)
        if self.flag == 1:
            self.increment += 10
            path_radius += self.increment
        plot_list = game_utils.get_screen(path_x + 512, -self.screen_y, self.bg_width, self.bg_height, path_radius)
        for (i, x, y) in plot_list:
            pygame.draw.circle(self.backgrounds[i], Color(255, 255, 255), (x, y), path_radius)
        if len(plot_list) == 1 and frame_time - self.last_decoration > 4000:
            print("hiiii")
            self.last_decoration = frame_time
            x_offset = (500 if random.randint(0,1) == 1 else -500) + random.randint(-100,100)

            seal_plot_list = game_utils.get_screen(path_x + 512 + x_offset, -self.screen_y, self.bg_width, self.bg_height, 500)
            seal = self.seals[random.randint(0,len(self.seals)-1)]
            for (i, x, y) in seal_plot_list:
                self.backgrounds[i].blit(  seal ,( x,y))

        # draw window
        self.backgrounds = self.backgrounds
        self.win.blit(self.backgrounds[0], (self.bg_xstart,  self.bg_ystart))
        self.win.blit(self.backgrounds[1], (self.bg_xend,    self.bg_ystart))
        self.win.blit(self.backgrounds[2], (self.bg_xstart,  self.bg_yend))
        self.win.blit(self.backgrounds[3], (self.bg_xend,    self.bg_yend))
        self.draw_text(str(self.score), 25, self.win.get_width()-50, 10)
        self.score = (pygame.time.get_ticks() - self.game_start_time)//1000
        
        game_over = self.is_game_over(self.win.get_at(self.penguin.center)) # must be before penguin draw
        self.penguin.draw(self.win)
        pygame.display.update()
        return game_over

    def is_game_over(self,c):
        if c != Color(255,255,255,255) and  c != Color(0,0,0,255):
            return self.score
        elif(self.flag == 1 and self.increment > 1800):
            return -1
        elif(game_utils.total_length < self.score+3):
            self.flag = 1
        return False


    def draw_text(self,text, size, x, y):
        WHITE = (255, 255, 255)
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.win.blit(text_surface, text_rect)



if __name__ == '__main__':
    clock = pygame.time.Clock()
    pygame.init()
    W, H = 1024, 800
    win = pygame.display.set_mode((W,H))
    pygame.display.set_caption('Malfunctioning self.penguin')
    game = Game(win)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
        game.tick()
        clock.tick(60)
