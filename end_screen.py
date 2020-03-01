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
penguin_high_img = pygame.image.load("./images/penguinKindaHappy.png")

# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.SysFont(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText

def endScreen(score=15):
    pause = 0
    screen.fill(white)

    winner = False

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
        
        # high scores
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

            winner = True


        # Main Menu UI

        highest_score_text = text_format(("Highest Score: "+ str(best_score_ever)), font, 60, black)
        score_text = text_format(("Your Score: " + str(score)), font, 60, black)

        new_highest_score_text = text_format(("NEW HIGH SCORE!!!"), font, 100, red)
        DA_new_highest_score_text = text_format(str(best_score_ever), font, 150, red)

        
        title=text_format("It's getting hotter and hotter in here...", font, 70, red)
        title2=text_format("Please save my home!", font, 100, red)

        if (winner==False):
            screen.fill(white)
            screen.blit(penguin_img, (0,0))

            tear = pygame.image.load(os.path.join('images', 'tear.png'))
            x_tear = 280
            y_tear = 500
            screen.blit(tear, (x_tear, y_tear+y_offset))
            y_offset += 2
            if y_offset >= 300:
                y_offset = 0
        else:
            screen.fill(white)
            screen.blit(penguin_high_img, (0,0))
        
        if selected=="start":
            text_start = text_format("RESTART", font, 75, red)
        else:
            text_start = text_format("RESTART", font, 75, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, red)
        else:
            text_quit = text_format("QUIT", font, 75, black)
 
        title_rect = title.get_rect()
        title2_rect = title2.get_rect()

        highest_rect = highest_score_text.get_rect()
        score_rect = score_text.get_rect()

        new_highest_rect = new_highest_score_text.get_rect()
        DA_new_highest_rect = highest_score_text.get_rect()

        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()
 
        # Main Menu Text

        if(winner==False):
            screen.blit(title, (screen_width/2 - (title_rect[2]/2), 120))
            screen.blit(title2, (screen_width/2 - (title_rect[2]/2) + 70, 180))
            screen.blit(highest_score_text, ((highest_rect[2]/6)-40, 720))
            screen.blit(score_text, (screen_width - (score_rect[2]) - 20, 720))
        else:
            screen.blit(new_highest_score_text, ((new_highest_rect[2]/4), 200))
            screen.blit(DA_new_highest_score_text, (screen_width/2 -60, 50))

        screen.blit(text_start, (100, 30))
        screen.blit(text_quit, (790, 30))

        pygame.display.update()
    score = 0
    clock.tick(FPS)
    pygame.display.set_caption("Malfunctioning Penguin - Music-Generated Gliding Game")

if __name__ == '__main__':
    endScreen()