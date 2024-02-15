import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Parameters
fs = 500  # Sampling frequency
t = np.arange(0, 2, 1/fs)  # Time vector of 2 seconds
f = 5  # Frequency of the sine wave

# Actual Signal (continuous sine wave)
actual_signal = np.sin(2 * np.pi * f * t)

# Measured Signal (time-limited sine wave)
n = len(t)
window = np.zeros(n)
window[:n//2] = 1  # Consider only the first half of the signal
measured_signal = actual_signal * window

# FFT of the actual signal
fft_actual = fft(actual_signal)
fft_actual_magnitude = np.abs(fft_actual)

# FFT of the measured signal
fft_measured = fft(measured_signal)
fft_measured_magnitude = np.abs(fft_measured)

# Frequency vector for plotting
freq = np.linspace(0, fs, n)

# Plotting
fig, axs = plt.subplots(3, 1, figsize=(10, 8))

# Actual Signal
axs[0].plot(t, actual_signal, 'b')
axs[0].set_title('Actual Signal')
axs[0].set_xlim(0, 2)
axs[0].set_ylim(-1.5, 1.5)

# Measured Signal
axs[1].plot(t, measured_signal, 'r')
axs[1].set_title('Measured Signal (time-limited)')
axs[1].set_xlim(0, 2)
axs[1].set_ylim(-1.5, 1.5)

# FFT Signal
axs[2].plot(t, fft_measured_magnitude, 'r')
axs[2].plot(t, fft_actual_magnitude, 'b--', alpha=0.5)  # Overlay with actual signal FFT
#axs[2].plot(t, fft_measured_magnitude, 'r')
#axs[2].plot(t, fft_actual_magnitude, 'b--', alpha=0.5)
axs[2].set_title('Signal as seen by FFT')
#axs[2].set_xlim(0, 2)
axs[2].set_xlim(0, 10)  # Limiting the x-axis to show the peak clearly
axs[2].set_ylim(0, 500)

# Show the plots
plt.tight_layout()
plt.show()
