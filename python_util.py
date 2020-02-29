import librosa as lb
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as sp
from scipy import optimize
import random as rn 
import math

def getMusic():
    sample_rate = 100

    filename = '/Users/gabi/Documents/penguin/joakim_karud-rock_angel.wav'
    data, sample_rate = librosa.load(filename, sr=sample_rate, mono=True, offset=0.0, res_type='kaiser_best')

    data = np.array([i for i in data if i >= 0])
    time = len(data) // 100
    data = np.take(data, [i for i in range(time * 100)])

    data = np.reshape(data, (time, 100))
    data = [np.mean(row) for row in data]
    time = [i for i in range(time)]

    f = sp.CubicSpline(time, data)

def getWidth(time, lastWidth, totalLength):
    maxWidth = 50 - math.ceil((time / totalLength) * 40)
    minWidth = maxWidth // 2
    newWidth = lastWidth + rn.randint(-1,1)
    return min(maxWidth, max(minWidth, newWidth))

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
        possible.remove(2)
        possible.remove(3)

    if bgHeight <= y - radius and y + radius <= 2 * bgHeight:
        possible.remove(0)
        possible.remove(1)

    for square in possible:
        if square == 0: 
            possible.remove(0)
            possible.append((0,x,y))
        
        if square == 1: 
            possible.remove(1)
            possible.append((1,(x - bgWidth) % (2 * bgWidth),y))
        
        if square == 2: 
            possible.remove(2)
            possible.append((2,x,(y - bgHeight) % (2 * bgHeight)))

        if square == 3: 
            possible.remove(3)
            possible.append((3,(x - bgWidth) % (2 * bgWidth),(y - bgHeight) % (2 * bgHeight)))


