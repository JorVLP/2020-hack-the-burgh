import pygame
import game_utils



class Game():

    def __init__(self, window):
        self.win = window

    def draw(self):
        (path_x,path_radius) = game_utils.plot_path(frame_time)
        plot_list = game_utils.get_screen(path_x,-screen_y,bg_width,bg_height,path_radius)
        for (i,x,y) in plot_list:
            pygame.draw.circle(backgrounds[i],Color(255,255,255),(x,y),path_radius)
    
    def _draw_path():
        pass

    def _draw_window():
        win.blit(backgrounds[0], (bg_xstart,bg_ystart))
        win.blit(backgrounds[1], (bg_xend,bg_ystart))
        win.blit(backgrounds[2], (bg_xstart,bg_yend))
        win.blit(backgrounds[3], (bg_xend,bg_yend))
        draw_text(win, str(round(frame_time/1000)), 25, W-50, 10)
        
        penguin.draw(win)
        pygame.display.update()



if __name__ == '__main__':
    pygame.init()
    W, H = 1024, 800
    win = pygame.display.set_mode((W,H))
    pygame.display.set_caption('Malfunctioning Penguin')
    game = Game(win)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
    game.draw()
    clock.tick(60)
    redrawWindow()
