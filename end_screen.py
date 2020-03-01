import pygame
import os


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
penguin_img = pygame.image.load("./images/penguinEnd.png")

# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.SysFont(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText


def endScreen():
    global pause, score
    pause = 0
    screen.fill(white)

    menu=True
    selected="start"
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_SPACE:
                    if selected=="start":
                        # LINK TO MAIN
                        print("Start")
                    if selected=="quit":
                        pygame.quit()
                        quit()
 
        # Main Menu UI
        screen.fill(white)
        title=text_format("GAME", font, 150, red)
        title2=text_format("OVER", font, 150, red)
        screen.blit(penguin_img, (0,0))
        if selected=="start":
            text_start = text_format("START", font, 75, red)
        else:
            text_start = text_format("START", font, 75, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, red)
        else:
            text_quit = text_format("QUIT", font, 75, black)
 
        title_rect=title.get_rect()
        title2_rect=title2.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(title2, (screen_width/2 - (title_rect[2]/2), 180))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), screen_height // 2 + 120))
        screen.blit(text_file1, (220, screen_height // 2 + 170))
        screen.blit(text_file2, (280, screen_height // 2 + 190))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), screen_height // 2 + 250))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Malfunctioning Penguin - Music-Generated Gliding Game")

endScreen()