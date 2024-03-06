import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

with open('outputny/eggan28.txt', 'r') as f:
    r = []
    g = []
    b = []
    
    lines = f.readlines()
    for i in range(3, len(lines)):
        line = lines[i].split(' ')
        r.append(float((line[0]).strip()))
        g.append(float((line[1]).strip()))
        b.append(float((line[2]).strip()))

g = signal.detrend(g)
t = np.arange(0,10, 10/len(g))

g_hann = np.hanning(len(g))*g

n_pad = 2**15
g_pad = np.pad(g_hann, (0, n_pad - len(g)), 'constant')
    
autocorr = np.correlate(g_pad, g_pad, mode='full')  
lags = np.arange(-n_pad + 1, n_pad,1) 

fft = np.fft.fft(g_pad, n_pad)
freq = np.fft.fftfreq(n_pad)
    
#plt.plot(t, b)
#plt.plot(freq*30*60, np.abs(fft))
#plt.plot(lags, autocorr)
#plt.xlim(-1000,1000)
#plt.show()

for i in range(-5, 5):
    autocorr[n_pad + i] = 0
    
index = np.argmax(autocorr)
puls = 30*60/lags[index]

puls_fft = 30*60*freq[np.argmax(fft)]
print("Puls med autokorrelasjon: ", -1*puls)
print("Puls med FFT: ", -1*puls_fft)
