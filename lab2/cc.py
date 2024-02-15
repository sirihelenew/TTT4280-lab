import numpy as np
import matplotlib.pyplot as plt

# Velger samplingsfrekvens fs = 1000 Hz
# Lager tidsvektor fra 0 til 1 sekund med 1000 prøver per sekund
fs = 1000
t = np.arange(-0.5, 0.5, 1/fs)

# Lager to sinussignaler med samme frekvens
# signal2 er forsinket med 0.01 sekunder
signal1 = np.sinc(2 * np.pi * 5 * t)
signal2 = np.sinc(2 * np.pi * 5 * (t - (1/4)))


plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal1, label='Signal 1', color='deeppink')
plt.plot(t, signal2, label='Signal 2', color='dodgerblue')
plt.title('Signalene')
plt.xlabel('Tid (s)')
plt.ylabel('Amplitude')
plt.legend()

# Krysskorrelasjon
cross_correlation = np.correlate(signal1, signal2, mode='full')

# Maksimalverdien til krysskorrelasjonen
max_cc = np.argmax(np.abs(cross_correlation))

# Tidsforsinkelse
tidsforsinkelse = max_cc - (len(signal1) - 1)

# Tidsforsinkelse i sekunder
delay_seconds = tidsforsinkelse / fs

lags = np.arange(-len(signal1) + 1, len(signal1))
lag = np.argmax(lags)
delay = lags[lag]/fs

print(f"Effektiv forsinkelse: {delay_seconds} sekunder")

# Plot 
plt.subplot(2, 1, 2)
#plt.plot((np.arange(len(cross_correlation)) - len(signal1) + 1) / fs, cross_correlation, color='deeppink')
plt.plot(lags, cross_correlation, color='deeppink')
#plt.axvline(x=delay_seconds, color='aqua', linestyle='--')
#plt.axvline(x=delay, color='darkorange', linestyle='--')
#plt.text(delay_seconds, 0, f'  {delay_seconds:.2f} s', verticalalignment='bottom')
#plt.text(lags, 0, f'  {lags:.2f} s', verticalalignment='bottom')
#plt.xlim(-200, 200)
plt.title('Krysskorrelasjon mellom signalene')
plt.xlabel('Forsinkelse')
plt.ylabel('Krysskorrelasjon')

plt.tight_layout()
plt.show()