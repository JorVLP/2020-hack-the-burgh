import pygame
import python_util 

path_x, path_radius = (0,50)
pathFunction, totalLength = python_util.getFun("./joakim_karud-rock_angel.wav")

def plot_path(time):
    global path_x, path_radius

    return (pathFunction(time), python_util.getWidth(time, path_radius, totalLength))

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
    
