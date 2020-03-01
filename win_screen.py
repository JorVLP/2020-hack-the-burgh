import pygame
import os
import time


# Game Initialization
pygame.init()
pygame.mixer.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width = 1024
screen_height = 800
screen=pygame.display.set_mode((screen_width, screen_height))

# Colors
white=(255, 255, 255)
black=(33,54,72)
gray=(50, 50, 50)
red=(234,65,123)
green=(0, 255, 0)
blue=(122,246,246)
yellow=(255, 255, 0)
bright_red = (255,0,0)
bright_green = (0,255,0)

# Game Fonts
font = 'Retro'

# Game image
penguin_img = pygame.image.load("./images/endOfSong.png")

# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.SysFont(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText

def winScreen(score=15):
    pause = 0
    screen.fill(white)

    winner = False

    menu=True
    selected="start"
    y_offset = 0
    menu_startup_time = pygame.time.get_ticks()
    menu_delay_passed = False
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="quit"
                if event.key==pygame.K_DOWN:
                    selected=""
                if event.key==pygame.K_SPACE:
                    if selected=="quit":
                        pygame.quit()
                        quit()
        
        # Main Menu UI
        if (winner==False):
            screen.fill(white)
            screen.blit(penguin_img, (0,0))
        else:
            screen.fill(white)
            screen.blit(penguin_img, (0,0))
        
        if selected=="quit":
            text_quit=text_format("QUIT", font, 50, red)
        else:
            text_quit = text_format("QUIT", font, 50, black)

        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(text_quit, (20, 20))

        pygame.display.update()

    score = 0
    clock.tick(FPS)
    pygame.display.set_caption("Malfunctioning Penguin - Music-Generated Gliding Game")

if __name__ == '__main__':
    winScreen()