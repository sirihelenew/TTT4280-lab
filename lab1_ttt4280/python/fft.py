import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import windows

# Parametere for sinussignalet
frekvens = 100  # Frekvens på 100 Hz
amplitude = 1   # Amplitude på 1
varighet = 1    # Varighet på 1 sekund

# Parametere for simulering av ADC
samplingsfrekvens = 1000  # Samplingsfrekvens på 1000 Hz
adc_bits = 8              # Oppløsning på 8 bit
adc_max_verdi = 2**adc_bits - 1  # Maksverdi for ADC-en

# Generer tidsaksen
t = np.linspace(0, varighet, int(samplingsfrekvens * varighet), endpoint=False)

# Generer sinussignalet
signal = amplitude * np.sin(2 * np.pi * frekvens * t)

# Simuler ADC ved å kvantisere signalet
kvant_signal = (signal + 1) * (adc_max_verdi / 2)  # Flytt signal til positivt område og skaler
kvant_signal = np.round(kvant_signal)              # Kvantiser til nærmeste heltall
kvant_signal = kvant_signal / (adc_max_verdi / 2) - 1  # Skaler tilbake til originalt område

# Utfør FFT
fft_resultat = fft(kvant_signal)
fft_frekvanser = np.fft.fftfreq(len(kvant_signal), d=1/samplingsfrekvens)

# Begrens til positivt frekvensområde
fft_resultat = fft_resultat[:len(fft_resultat)//2]
fft_frekvanser = fft_frekvanser[:len(fft_frekvanser)//2]

# Plot resultatet
plt.figure(figsize=(12, 6))
plt.plot(fft_frekvanser, np.abs(fft_resultat))
plt.title("Frekvensspektrum av Sinussignal")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
