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
    
    # data = [vector[num] for vector in data]
    return data[:, num], t, sample_period



ifq, t, sample_period = data('samples/v2-2.bin', 2)
ifi, t, sample_period = data('samples/v2-2.bin', 1)

# ifq = signal.detrend(ifq[80000:82000]) * 8.0566e-4
# ifi = signal.detrend(ifi[80000:82000]) * 8.0566e-4
# t = t[80000:82000]
ifq = signal.detrend(ifq[3000:]) * 8.0566e-4
ifi = signal.detrend(ifi[3000:]) * 8.0566e-4
t = t[3000:] 

print(ifq.shape)

x = ifi+ 1j*ifq

def fft(signal1):
    N= 2**18
    N_FFT = np.fft.fftfreq(N)
    FFT1 = np.fft.fft(x, N)

    plt.plot(N_FFT*1/sample_period, abs(FFT1))
    


f_D1 = []
f_D2 = []
f_D3 = []

def v_r(vec):
    f_0 = 24.13*10**9
    c = 3*10**8
    hastigheter = []
    for i in range (0,len(vec)):
        fart = (vec[i]*c)/(2*f_0)
        hastigheter.append(fart)
    
    return hastigheter

avr1 = np.average(v_r(f_D1))
std1 = np.std(v_r(f_D1))

avr2 = np.average(v_r(f_D2))
std2 = np.std(v_r(f_D2))

avr3 = np.average(v_r(f_D3))
std3 = np.std(v_r(f_D3))

print("avr1 = ", avr1, "\n", "std1 = ", std1)
print("avr2 = ", avr2, "\n", "std1 = ", std2)
print("avr3 = ", avr3, "\n", "std1 = ", std3)

støy = fft.tolist()

for i in range(2914-20, 2914+20):
    støy.pop(i)

std_støy = abs(np.std(støy))
max_signal = abs(np.max(fft))

SNR = max_signal/std_støy


print("SNR: ", SNR)
#plt.plot(t, ifq)
#plt.plot(t, ifi)

fft(x)
#plt.ylim(0,800000)
plt.xlim(-300,300)
plt.legend()
plt.show()