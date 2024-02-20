import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import windows

#--------------------------------------#

def raspi_import(path, channels=5):

    with open(path, 'r') as fid:
        sample_period = np.fromfile(fid, count=1, dtype=float)[0]
        data = np.fromfile(fid, dtype='uint16').astype('float64')
        data = data.reshape((-1, channels))

    sample_period *= 1e-6
    return sample_period, data

if __name__ == "__main__":
    
    sample_period, data = raspi_import(sys.argv[1] or 'foo.bin')

    channel_data = data[:,4] # ADC 5

    #Hanning window
    window = windows.hann(len(channel_data))
    windowed_data = channel_data 

    #Zero-padding
    zero_padding_factor = 2
    
    n_padded = len(windowed_data) * zero_padding_factor
    windowed_data_padded = np.pad(windowed_data, (0, n_padded - len(windowed_data)), 'constant')
    channel_data_padded = np.pad(channel_data, (0, n_padded - len(channel_data)), 'constant')

    fft_data_window = fft(windowed_data_padded)
    fft_data_channel = fft(channel_data_padded)

    #Frekvensakse
    frequencies = fftfreq(n_padded, d=sample_period)

    #Normalisert amplitude window-data
    magnitude_window_data = np.abs(fft_data_window) / n_padded
    magnitude_db_window = 20 * np.log10(magnitude_window_data)
    magnitude_db_normalisert = magnitude_db_window - np.max(magnitude_db_window)

    #Normalisert amplitude channel-data
    magnitude_channel_data = np.abs(fft_data_channel) / n_padded
    psd_channel_data = np.abs(fft_data_channel) ** 2 / n_padded

    #magnitude_db_channel_data = 20 * np.log10(magnitude_channel_data)
    magnitude_db_channel_data = 20 * np.log10(magnitude_channel_data)
    magnitude_db_normalisert_channel_data = magnitude_db_channel_data - np.max(magnitude_db_channel_data)


    #Plot 
    #n_padded//2 for å få med kun den positive delen av frekvensspekteret
    # plt.plot(frequencies[:n_padded//2], magnitude_db_normalisert[:n_padded//2], color='deepskyblue', label='Med Hanning-vindu')
    # plt.plot(frequencies[:n_padded//2], magnitude_db_normalisert_channel_data[:n_padded//2], color='hotpink', label='Uten Hanning-vindu')
    # #plt.figure()
    # #plt.psd(magnitude_db_channel_data, Fs=31250)
    # plt.title('Sammenligning av frekvensspektrum med og uten Hanning-vindu', fontsize=22)
    # plt.xlabel('Frekvens [Hz]', fontsize=18)
    # plt.ylabel('Normalisert amplitude [dB]', fontsize=18)
    # plt.xlim(50,150)
    # plt.ylim(-160,0)
    # plt.legend(loc='upper right', fontsize=14)
    # plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(frequencies[:n_padded//2], magnitude_db_normalisert[:n_padded//2], color='mediumorchid', label='ADC 3')
    plt.xlabel('Frekvens [Hz]', fontsize=18)
    plt.ylabel('Normalisert amplitude [dB]', fontsize=18)
    plt.xlim(50,150)
    plt.ylim(-160,0)
    plt.title('Frekvensspektrum av Sinusbølge, ADC 5, med Zero-padding faktor 2', fontsize=22)
    plt.show()

    
    #magnitude_db_normalisert = magnitude_db - np.max(magnitude_db)

# Plot frequency spectrum
    
