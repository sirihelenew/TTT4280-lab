import numpy as np
import sys
import matplotlib.pyplot as plt
import scipy.signal 
import scipy.interpolate

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

def plot_channel_data(sample_period, data, channel=0):
    time_axis = np.arange(data.shape[0]) * sample_period  # Beregn tidsaksen
    plt.figure(figsize=(10, 6))
    plt.plot(time_axis, data[:, channel] - np.mean(data[:, channel]), color='deeppink')  # Trekker fra gjennomsnittet for å sentrere rundt 0
    #plt.plot(np.arange(data.shape[0])*sample_period, data[:,2]*2/2500, label='ADC 1', color='mediumorchid')
    plt.xlabel('Tid (s)')
    plt.ylabel('Amplitude')
    plt.title(f'Signal fra ADC 1')
    plt.ylim(-400,400)
    plt.grid(True)
    plt.show()



def cross_correlation(signal1, signal2, fs):
    crosscorrelation = np.correlate(signal1, signal2, mode='full')
    max_cc = np.argmax(np.abs(crosscorrelation))

    # Tidsforsinkelse
    tidsforsinkelse = max_cc - (len(signal1) - 1)

    # Tidsforsinkelse i sekunder
    delay_seconds = tidsforsinkelse / fs

    lags = np.arange(-len(signal1) + 1, len(signal1),1)
    lags = np.arange(-len(signal1) + 1, len(signal1),1/4)
    lag = np.argmax(abs(crosscorrelation))


    print(f"Effektiv forsinkelse: {delay_seconds} sekunder")
    print(f"Effektiv forsinkelse: {lags[lag]} lags")
   


    # Plot 
    
    plt.plot(lags, crosscorrelation, color='deeppink')
    
    plt.title('Krysskorrelasjon mellom signalene')
    plt.xlabel('Forsinkelse')
    plt.ylabel('Krysskorrelasjon')

    #plt.tight_layout()
    plt.show()

    return lags[lag]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        print("Vennligst oppgi filnavn som argument.")
        sys.exit(1)

    sample_period, data = raspi_import(filepath)
    data = scipy.signal.detrend(data, axis=0)
    #plot_channel_data(sample_period, data, channel=0) #ADC 
    #t = np.arange(0, 1, 1/31250)
    t = np.linspace(0, 1, 31250)
    signal2 = data[:,1]
    signal2_interpolate = scipy.interpolate.interp1d(t, signal2)
    signal2_interpolated = signal2_interpolate(t)

    signal3 = data[:,2]
    signal3_interpolate = scipy.interpolate.interp1d(t, signal3)
    signal3_interpolated = signal3_interpolate(t)

    signal1 = data[:,0]
    signal1_interpolate = scipy.interpolate.interp1d(t, signal1)
    signal1_interpolated = signal1_interpolate(t)
    
    n23 = (cross_correlation(signal2_interpolated, signal3_interpolated, 31250))  
    n13 = (cross_correlation(signal1_interpolated, signal3_interpolated, 31250))
    n12 = (cross_correlation(signal1_interpolated, signal2_interpolated, 31250))
    theta = np.degrees(np.arctan2(np.sqrt(3)*(n23+n13),(n23-n13-2*n12)))
    print(f"n23 = {n23}, n13 = {n13}, n12 = {n12}, theta = {theta}")

    