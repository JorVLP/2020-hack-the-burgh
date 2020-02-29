

def getScreen(x,y,bgWidth, bgHeight, radius):
    possible = [i for i in range(4)]
    
    x = x % (2 * bgWidth) 
    y = y % (2 * bgHeight) 

    if 0 <= x - radius and x + radius <= bgWidth:
        possible.remove(1)
        possible.remove(3)

    if bgWidth <= x - radius and x + radius <= 2 * bgWidth:
        possible.remove(0)
        possible.remove(2)

    if 0 <= y - radius and y + radius <= bgHeight:
        if 2 in possible: possible.remove(2)
        if 3 in possible: possible.remove(3)

    if bgHeight <= y - radius and y + radius <= 2 * bgHeight:
        if 0 in possible: possible.remove(0)
        if 1 in possible: possible.remove(1)

    if 0 in possible:
        possible.remove(0)
        possible.append((0,x,y))
    
    if 1 in possible:
        possible.remove(1)
        possible.append((1,x - bgWidth,y))
    
    if 2 in possible: 
        possible.remove(2)
        possible.append((2,x,y - bgHeight))

    if 3 in possible:
        possible.remove(3)
        possible.append((3,x - bgWidth,y - bgHeight))

