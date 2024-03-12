import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

<<<<<<< HEAD
#hente fra fil
with open('opptak4.txt', 'r') as f:
=======
with open('data/eggan1.txt', 'r') as f:
>>>>>>> master
    r = []
    g = []
    b = []
    
    lines = f.readlines()
    for i in range(3, len(lines)):
        line = lines[i].split(' ')
        r.append(float((line[0]).strip()))
        g.append(float((line[1]).strip()))
        b.append(float((line[2]).strip()))

<<<<<<< HEAD
b = signal.detrend(b)
t = np.arange(0,10, 10/len(g))

b_hann = np.hanning(len(b))*b

n_pad = 2**15
b_pad = np.pad(b_hann, (0, n_pad - len(b)), 'constant')
    
autocorr = np.correlate(b_pad, b_pad, mode='full')  
lags = np.arange(-n_pad + 1, n_pad,1) 

fft = np.fft.fft(b_pad, n_pad)
freq = np.fft.fftfreq(n_pad)
    
#plt.plot(t, b)
#plt.plot(freq*30*60, np.abs(fft))
#plt.plot(lags, autocorr)
#plt.xlim(-1000,1000)
#plt.show()
=======
g = signal.detrend(g)
t = np.arange(0,10, 10/len(g))

g_hann = np.hanning(len(g))*g

n_pad = 2**16
g_pad = np.pad(g_hann, (0, n_pad - len(g)), 'constant')
    
autocorr = np.correlate(g_pad, g_pad, mode='full')  
lags = np.arange(-n_pad + 1, n_pad,1) 

fft = np.fft.fft(g_pad, n_pad)
freq = np.fft.fftfreq(n_pad)
    
plt.plot(t, g, color = "green", label = "green")
plt.plot(t, b, color = "blue", label = "blue")
plt.plot(t, r, color = "red", label = "red")
#plt.plot(freq*30*60, np.abs(fft))
#plt.plot(lags, autocorr)
#plt.xlim(0,200)
plt.legend()
plt.show()

støy = fft.tolist()

for i in range(2914-20, 2914+20):
    støy.pop(i)

std_støy = abs(np.std(støy))
max_signal = abs(np.max(fft))

SNR = max_signal/std_støy


print("SNR: ", SNR)


>>>>>>> master

for i in range(-5, 5):
    autocorr[n_pad + i] = 0
    
index = np.argmax(autocorr)
puls = 30*60/lags[index]

puls_fft = 30*60*freq[np.argmax(fft)]
<<<<<<< HEAD
print("Puls med autokorrelasjon: ", -1*puls)
print("Puls med FFT: ", -1*puls_fft)
=======
print("Puls med autokorrelasjon: ", abs(puls))
print("Puls med FFT: ", abs(puls_fft))
>>>>>>> master
