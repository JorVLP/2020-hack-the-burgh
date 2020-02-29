import pygame

path_x, path_radius = (0,50)

def plot_path(time):
    global path_x, path_radius

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        path_radius -= 1
    
    if keys[pygame.K_UP]:
        path_radius += 1

    if keys[pygame.K_LEFT]:
        path_x -= 2

    if keys[pygame.K_RIGHT]:
        path_x += 2

    return (path_x,path_radius)


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

if __name__ == '__main__':
    bg = 100
    test1 = get_screen(10,30,bg,bg,20)
    output1 = [(0,10,30),(1,bg+10,30)]
    if len(test1) != len(output1):
        print("wrong length")
    for t in test1:
        if t not in output1:
            print(f"wrong output1: {t}")

    test2 = get_screen(bg-10,30,bg,bg,20)
    output2 = [(0,bg-10,30),(1,-10,30)]
    if len(test2) != len(output2):
        print("wrong length")
    for t in test2:
        if t not in output2:
            print(f"wrong output2: {t}")

    test3 = get_screen(bg+10,30,bg,bg,20)
    output3 = [(0,bg+10,30),(1,10,30)]
    if len(test3) != len(output3):
        print("wrong length")
    for t in test3:
        if t not in output3:
            print(f"wrong output3: {t}")

    test5 = get_screen(2*bg-10,30,bg,bg,20)
    output5 = [(0,-10,30),(1,bg-10,30)]
    if len(test5) != len(output5):
        print("wrong length")
    for t in test5:
        if t not in output5:
            print(f"wrong output5: {t}")

    test4 = get_screen(50,50,bg,bg,20)
    output4 = [(0,50,50)]
    if len(test4) != len(output4):
        print("wrong length")
    for t in test4:
        if t not in output4:
            print(f"wrong output4: {t}")
    
