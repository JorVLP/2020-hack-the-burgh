import librosa as lb
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as sp
from scipy import optimize


sample_rate = 100
plt.figure(figsize=(20, 2))

filename = '/Users/gabi/Documents/penguin/joakim_karud-rock_angel.wav'
data, sample_rate = librosa.load(filename, sr=sample_rate, mono=True, offset=0.0, res_type='kaiser_best')

data = np.array([i for i in data if i >= 0])
time = len(data)
# plt.plot([i for i in range(time)], data)

time = len(data) // 100
data = np.take(data, [i for i in range(time * 100)])

data = np.reshape(data, (time, 100))
data = [np.mean(row) for row in data]
time = [i for i in range(time)]

f = sp.CubicSpline(time, data)
# plt.plot(time, sp.CubicSpline(time, data))
t = np.arange(0.0,100.0,0.1)
plt.plot(t, f(t))
plt.show()
