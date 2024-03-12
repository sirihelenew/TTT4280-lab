import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
from scipy.signal import correlate

# Last inn data fra tekstfil
data = np.loadtxt('outputny/vigiropp.txt')

N = 2**7
# Del dataene i tre kolonner for rød, grønn og blå
r = data[:, 0]  # Rød fargekanal
g = data[:, 1]  # Grønn fargekanal
b = data[:, 2]  # Blå fargekanal
sample_period = 10/len(g)  # Tidssteg i sekunder (sek/sample)

x = np.linspace(0,10,len(g))  # Tid i sekunder

g1 = g - np.mean(g) # Fjerner likespenningkomponenten
hanning = np.hanning(len(g)) # Hanning-vindu
g_hann = g1 * hanning 
data_fft = np.fft.fft((g_hann), 1024) # FFT av signalet
freq = np.fft.fftfreq(1024, sample_period) # Frekvensakse #1024 er oppløsning fft
freq_bpm = freq * 60 # Frekvensakse i bpm

#Autokorrelasjonen 
plt.figure()
g_korr = correlate(g1, g1, mode='full')
norm_korr = g_korr / np.max(g_korr)
x_korr = np.arange(-len(g1)+1, len(g1))
plt.plot(x_korr, norm_korr, color='green')
plt.title('Autokorrelasjon av Grønn Kanal')
plt.xlabel('Forsinkelse [samples]')
plt.ylabel('Korrelasjon')

#FFT av signalet
plt.figure()
plt.plot(freq_bpm, np.abs(data_fft), color='green')
#plt.xlim(0, 240)
plt.title('FFT av Grønn Kanal')
plt.xlabel('BPM')
plt.ylabel('Amplitude')

# Plot hver fargekanal
plt.figure()
plt.plot(x, r, label='Rød Kanal', color='red')
plt.plot(x, g, label='Grønn Kanal', color='green')
plt.plot(x, b, label='Blå Kanal', color='blue')
plt.xlabel('Tid [s]')
plt.ylabel('Verdi')
plt.title('Plot av Fargekanaler')
plt.legend()

plt.show()
