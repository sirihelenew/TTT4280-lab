import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import windows

def raspi_import(path, channels=5):

    with open(path, 'r') as fid:
        sample_period = np.fromfile(fid, count=1, dtype=float)[0]
        data = np.fromfile(fid, dtype='uint16').astype('float64')
        data = data.reshape((-1, channels))

    sample_period *= 1e-6
    return sample_period, data


# Import data from bin file
if __name__ == "__main__":
    sample_period, data = raspi_import(sys.argv[1] or 'foo.bin')

    channel_data = data[:,4]

    zero_padding_factor = 5
    
    n_padded = len(channel_data) * zero_padding_factor

    data_padded = np.pad(channel_data, (0, n_padded - len(channel_data)), 'constant')

# Perform FFT
    fft_data_padded = fft(channel_data)

# Frequency axis
    n = len(channel_data)
    frequencies = fftfreq(n, d=sample_period)
    #freq2 = np.right_shift(frequencies, n//2)


    

# Magnitude of FFT (normalized)
    magnitude = np.abs(fft_data_padded) 
    psd = np.abs(fft_data_padded) ** 2 

    #sx = np.square(magnitude)

    #magnitude_db = 20 * np.log10(magnitude)
    magnitude_db = 20 * np.log10(psd)
    magnitude_db_normalisert = magnitude_db - np.max(magnitude_db)

    # plt.figure()
    # #plt.psd(freq2, magnitude_db, Fs=31250)
    # plt.title('Frekvensspektrum av Sinusbølge, ADC 2')
    # plt.xlabel('Frekvens [Hz]')
    # plt.ylabel('Normalisert amplitude [dB]')
    # #plt.xlim(0,200)
    # #plt.ylim(-100,0)
    # plt.legend()
    # plt.show()

# Plot frequency spectrum
    plt.figure(figsize=(10, 6))
    plt.plot(frequencies[:n//2], magnitude_db_normalisert[:n//2], color='mediumorchid')
    plt.xlabel('Frekvens [Hz]')
    plt.ylabel('Normalisert amplitude [dB]')
    #plt.xlim(0,200)
    #plt.ylim(0,400)
    plt.title('Frekvensspektrum av Sinusbølge, ADC 5')
    plt.show()

    # Plot each channel individually
    #plt.figure(figsize=(10, 6))
    #for i in range(data.shape[1]):
    #plt.plot(np.arange(data.shape[0])*sample_period, data[:,0]*2/2500, label='ADC 1', color='mediumorchid')
    #plt.plot(np.arange(data.shape[0])*sample_period+0.001, data[:,1]*2/2500, label='ADC 2')
    #plt.plot(np.arange(data.shape[0])*sample_period+0.002, data[:,2]*2/2500, label='ADC 3')
    #plt.plot(np.arange(data.shape[0])*sample_period+0.003, data[:,3]*2/2500, label='ADC 4')
    #plt.plot(np.arange(data.shape[0])*sample_period+0.004, data[:,4]*2/2500, label='ADC 5')
    # plt.xlabel('Tid [s]')
    # plt.ylabel('Spenning [V]')
    # plt.title('Samplet sinussignal med f=100 Hz, samplingfrekvens fs=31250 Hz')
    # #plt.legend()
    # plt.show()
