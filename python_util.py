import librosa as lb
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as sp
from scipy import optimize
import random as rn 
import math

def getFun(music):
    #sample_rate = 100

    #music = './sounds/kevin.mp3'
    data, sample_rate = librosa.load(music, sr=100, mono=True, offset=0.0, res_type='kaiser_best')
    print(data)
    data = np.array([i for i in data if i >= 0])
    m = np.max(data)
    time = len(data) // 100
    data = np.take(data, [i for i in range(time * 100)])

    data = np.reshape(data, (time, 100))
    data = np.array([np.mean(row) for row in data])
    data = data / m
    #time = [i for i in range(time)]

    #f = sp.CubicSpline(time, data)
    time_list = [i for i in range(time)]
    print(len(time_list))
    print(time_list[-1])
    return (sp.CubicSpline(time_list, data), time)

# def getWidth(time, lastWidth, totalLength):
#     maxWidth = 50 - math.ceil((time / totalLength) * 40)
#     minWidth = maxWidth // 2
#     newWidth = lastWidth + rn.randint(-1,1)
#     return min(maxWidth, max(minWidth, newWidth))



if __name__ == '__main__':
    getFun("")
