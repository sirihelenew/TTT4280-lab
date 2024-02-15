import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import windows

def raspi_import(path, channels=5):
    """
    Import data produced using adc_sampler.c.

    Returns sample period and a (`samples`, `channels`) `float64` array of
    sampled data from all channels.

    Example (requires a recording named `foo.bin`):
    ```
    >>> from raspi_import import raspi_import
    >>> sample_period, data = raspi_import('foo.bin')
    >>> print(data.shape)
    (31250, 5)
    >>> print(sample_period)
    32.0

    ```
    """

    with open(path, 'r') as fid:
        sample_period = np.fromfile(fid, count=1, dtype=float)[0]
        data = np.fromfile(fid, dtype='uint16').astype('float64')
        # The "dangling" `.astype('float64')` casts data to double precision
        # Stops noisy autocorrelation due to overflow
        data = data.reshape((-1, channels))

    # sample period is given in microseconds, so this changes units to seconds
    sample_period *= 1e-6
    return sample_period, data


# Import data from bin file
if __name__ == "__main__":
    sample_period, data = raspi_import(sys.argv[1] or 'foo.bin')
    """plt.figure(figsize=(10, 6))
    plt.plot(np.arange(data.shape[0])*sample_period, data)
    plt.xlabel('Tid (s)')
    plt.ylabel('Tall fra ADC-en')
    plt.legend()
    plt.show()"""

    sample_period, data = raspi_import(sys.argv[1] or 'foo.bin')

    channel_data = data[:,0]

# Apply a window function (e.g., Hanning window)
    #window = windows.hann(len(channel_data))
    #windowed_data = channel_data * window

# FFT
    fft_data = fft(channel_data)

# Frekvensakse
    n = len(channel_data)
    frequencies = fftfreq(n, d=sample_period)

# Amplitude
    magnitude = np.abs(fft_data) / n

    sx = np.square(magnitude)

    magnitude_db = 20 * np.log10(magnitude)
    magnitude_db_normalisert = magnitude_db - np.max(magnitude_db)

# Plot frequency spectrum
    plt.figure(figsize=(10, 6))
    plt.plot(frequencies[:n//2], magnitude_db_normalisert[:n//2])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.xlim(0,200)
    #plt.ylim(0,400)
    plt.title('Frequency Spectrum of the Sine Wave')
    plt.show()

    # Plot each channel individually
    plt.figure(figsize=(10, 6))
    #for i in range(data.shape[1]):
    plt.plot(np.arange(data.shape[0])*sample_period, data[:, 1])

    plt.xlabel('Time (s)')
    plt.ylabel('ADC Value')
    plt.title('Sine Wave Measured by ADC, channel 2')
    plt.legend()
    plt.show()
