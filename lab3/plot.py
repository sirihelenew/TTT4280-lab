import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#hente fra fil
<<<<<<< HEAD
with open('output\opptak7.txt', 'r') as f:
    r = []
    g = []
    b = []
=======
# with open('outputny/eggan28.txt', 'r') as f:
#     r = []
#     g = []
#     b = []
>>>>>>> e2d43d560053139d7708973a0c8e4700c7878165
    
#     lines = f.readlines()
#     for i in range(3, len(lines)):
#         line = lines[i].split(' ')
#         r.append(float((line[0]).strip()))
#         g.append(float((line[1]).strip()))
#         b.append(float((line[2]).strip()))

# g = signal.detrend(g)
# t = np.arange(0,10, 10/len(g))

# g_hann = np.hanning(len(g))*g

# n_pad = 2**15
# g_pad = np.pad(g_hann, (0, n_pad - len(g)), 'constant')
    
<<<<<<< HEAD
autocorr = np.abs(np.correlate(b_pad, b_pad, mode='full'))
lags = np.arange(-n_pad + 1, n_pad,1) 
=======
# autocorr = np.correlate(g_pad, g_pad, mode='full')  
# lags = np.arange(-n_pad + 1, n_pad,1) 
>>>>>>> e2d43d560053139d7708973a0c8e4700c7878165

# fft = np.fft.fft(g_pad, n_pad)
# freq = np.fft.fftfreq(n_pad)
    
<<<<<<< HEAD
#plt.plot(t, b)
#plt.plot(freq*30*60, np.abs(fft))
plt.plot(lags, np.abs(autocorr))
#plt.xlim(-1000,1000)
plt.show()
=======
# #plt.plot(t, b)
# #plt.plot(freq*30*60, np.abs(fft))
# #plt.plot(lags, autocorr)
# #plt.xlim(-1000,1000)
# #plt.show()
>>>>>>> e2d43d560053139d7708973a0c8e4700c7878165

# for i in range(-5, 5):
#     autocorr[n_pad + i] = 0
    
# index = np.argmax(autocorr)
# puls = 30*60/lags[index]

<<<<<<< HEAD
puls_fft = 30*60*freq[np.argmax(fft)]
print("Puls med autokorrelasjon: ", -1*puls)
print("Puls med FFT: ", -1*puls_fft)
=======
# puls_fft = 30*60*freq[np.argmax(fft)]
# print("Puls med autokorrelasjon: ", abs(puls))
# print("Puls med FFT: ", abs(puls_fft))
# # print(lags[index])
# # print(freq[np.argmax(fft)])

def process_files(file_paths):
    puls_array = []
    puls_fft_array = []
    
    for file_path in file_paths:
        with open(file_path, 'r') as f:
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

            for i in range(-5, 5):
                autocorr[n_pad + i] = 0

            index = np.argmax(autocorr)
            puls = 30*60/lags[index]

            puls_fft = 30*60*freq[np.argmax(fft)]
            
            puls_array.append(abs(puls))
            puls_fft_array.append(abs(puls_fft))
    
    return puls_array, puls_fft_array

process_files('data/data.txt')
>>>>>>> e2d43d560053139d7708973a0c8e4700c7878165
