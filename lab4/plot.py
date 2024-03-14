import numpy as np
import sys
import scipy.signal as signal
import matplotlib.pyplot as plt


def raspi_import(path, channels=5):
    """
    Import data produced using adc_sampler.c.

    Returns sample period and a (samples, channels) float64 array of
    sampled data from all channels channels.

    Example (requires a recording named foo.bin):
    
    >>> from raspi_import import raspi_import
    >>> sample_period, data = raspi_import('data.bin') 
    >>> print(data.shape)
    (31250, 5)
    >>> print(sample_period)
    3.2e-05

    
    """

    with open(path, 'r') as fid:
        sample_period = np.fromfile(fid, count=1, dtype=float)[0]
        data = np.fromfile(fid, dtype='uint16').astype('float64')
        # The "dangling" .astype('float64') casts data to double precision
        # Stops noisy autocorrelation due to overflow
        data = data.reshape((-1, channels))

    # sample period is given in microseconds, so this changes units to seconds
    sample_period *= 1e-6
    return sample_period, data


# Import data from bin file

def data(fil, num):
   
    sample_period, data = raspi_import(fil)
    t = np.arange(0, len(data)*sample_period, sample_period)
    
    data = [vector[num] for vector in data]
    return data, t, sample_period



ifq, t, sample_period = data('samples/v1-1.bin', 2)
ifi, t, sample_period = data('samples/v1-1.bin', 1)

def fft(signal1, signal2):
    N= 2**14
    N_FFT = np.fft.fftfreq(N)

    FFT1 = np.fft.fft(signal1, N)
    FFT2 = np.fft.fft(signal2, N)

    plt.plot(N_FFT, FFT1)
    plt.plot(N_FFT, FFT2)


#f_D = []

# def v_r(vec):
#     f_0 = 24.13*10**9
#     c = 3*10**8
#     hastigheter = []
#     for i in range (0,len(vec)):
#         fart = (vec[i]*c)/(2*f_0)
#         hastigheter.append(fart)
    
#     return hastigheter

# np.average(v_r(f_D))
# np.std(v_r(f_D))



plt.plot(t, ifq)
plt.plot(t, ifi)

# fft(ifq, ifi)

plt.show()