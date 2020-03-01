import pygame
import python_util
import random

factor = 1
randomness = 0
path_x, path_radius = (0,50)
path_function, total_length = (0,0)

def set_func(music):
    global path_function, total_length
    path_function, total_length = python_util.getFun(music)

def plot_path(time):
    global path_x, path_radius, path_function, total_length, factor,randomness
    # print((path_function(time/1000)*10000))
    grad = 0 if time == 0 else (path_function(time/1000) - path_function((time - 1)/1000))*100000000
    if grad >= 7 or grad <= -7:
        factor *= 0.999
    if grad <= 0.05 and grad >= -0.05:
        factor *= 1.001
    randomness = max(-100, min(100, (randomness + random.randint(-2,2))))
    return (int(path_function(time/1000)*100000*factor) + randomness, 200)
    

    
    #int(python_util.getWidth(time, path_radius, total_length)))

    # keys = pygame.key.get_pressed()

    # if keys[pygame.K_DOWN]:
    #     path_radius -= 1
    
    # if keys[pygame.K_UP]:
    #     path_radius += 1

    # if keys[pygame.K_LEFT]:
    #     path_x -= 2

    # if keys[pygame.K_RIGHT]:
    #     path_x += 2

    # return (path_x,path_radius)


def get_screen(x,y,bgWidth, bgHeight, radius):
    possible = [i for i in range(4)]
    
    x = x % (2 * bgWidth) 
    y = y % (2 * bgHeight) 

    if x - radius >= 0 and x + radius <= bgWidth:
        possible.remove(1)
        possible.remove(3)

    if bgWidth <= x - radius and x + radius <= 2 * bgWidth:
        possible.remove(0)
        possible.remove(2)

    if y - radius >= 0 and y + radius <= bgHeight:
        if 2 in possible: possible.remove(2)
        if 3 in possible: possible.remove(3)

    if bgHeight <= y - radius and y + radius <= 2 * bgHeight:
        if 0 in possible: possible.remove(0)
        if 1 in possible: possible.remove(1)

    if 0 in possible:
        possible.remove(0)
        possible.append((0,
            x if x <= bgWidth + radius else x - 2 * bgWidth,
            y if y <= bgHeight + radius else y - 2 * bgHeight))
    
    if 1 in possible:
        possible.remove(1)
        possible.append((1,
            x + bgWidth if x <= radius else x - bgWidth,
            y if y <= bgHeight + radius else y - 2 * bgHeight))
    
    if 2 in possible: 
        possible.remove(2)
        possible.append((2,
            x if x <= bgWidth + radius else x - 2 * bgWidth,
            y + bgHeight if y <= radius else y - bgHeight))

    if 3 in possible:
        possible.remove(3)
        possible.append((3,
            x + bgWidth if x <= radius else x - bgWidth,
            y + bgHeight if y <= radius else y - bgHeight))

    return possible
    
