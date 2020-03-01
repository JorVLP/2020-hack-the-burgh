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
penguin_img = pygame.image.load("./images/penguinEnd.png")

# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.SysFont(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText

def endScreen(score=0):
    pause = 0
    screen.fill(white)

    menu=True
    selected="start"
    y_offset = 0
    menu_startup_time = pygame.time.get_ticks()
    menu_delay_passed = False
    while menu:
        if not menu_delay_passed:
            if pygame.time.get_ticks() - menu_startup_time > 200:
                menu_delay_passed = True
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        selected="start"
                    elif event.key==pygame.K_RIGHT:
                        selected="quit"
                    if event.key==pygame.K_SPACE:
                        if selected=="start":
                            return (True)
                        if selected=="quit":
                            pygame.quit()
                            quit()
        filename = "highscore"
        score_file = open(filename,"rt")
        best_score_ever = int(score_file.read())

        if(score > best_score_ever):
            best_score_ever = score
            old_best_score = score_file.read()
            old_best_score = old_best_score.replace(old_best_score, str(score))
            score_file.close()

            score_file = open(filename, "wt")
            score_file.write(old_best_score)
            score_file.close()

        # Main Menu UI
        highest_score_text = text_format(("Highest Score: "+ str(best_score_ever)), font, 60, red)
        score_text = text_format(("Your Score: " + str(score)), font, 60, red)
        
        screen.fill(white)
        title=text_format("GAME OVER", font, 150, red)
        title2=text_format("OVER", font, 150, red)

        screen.blit(penguin_img, (0,0))

        tear = pygame.image.load(os.path.join('images', 'tear.png'))
        x_tear = 280
        y_tear = 500
        screen.blit(tear, (x_tear, y_tear+y_offset))
        y_offset += 2
        if y_offset >= 300:
            y_offset = 0
        
        if selected=="start":
            text_start = text_format("RESTART", font, 75, red)
        else:
            text_start = text_format("RESTART", font, 75, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, red)
        else:
            text_quit = text_format("QUIT", font, 75, black)
 
        title_rect=title.get_rect()
        #title2_rect=title2.get_rect()

        highest_rect=highest_score_text.get_rect()
        score_rect=score_text.get_rect()

        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 50))
        screen.blit(highest_score_text, ((highest_rect[2]/6)-40, 200))
        screen.blit(score_text, (screen_width - (score_rect[2]) - 20, 200))

        screen.blit(text_start, (100, screen_height // 2 + 270))
        screen.blit(text_quit, (790, screen_height // 2 + 270))

        pygame.display.update()
    score = 0
    clock.tick(FPS)
    pygame.display.set_caption("Malfunctioning Penguin - Music-Generated Gliding Game")

if __name__ == '__main__':
    endScreen()