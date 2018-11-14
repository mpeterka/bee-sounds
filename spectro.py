from scipy import signal
from scipy.io import wavfile
import numpy as np
import matplotlib

# from scipy.io import wavfile

matplotlib.use('agg')
from matplotlib import pyplot as plt

M = 1000
rate, audio = wavfile.read('wav_data/18-08-07_09_10_12.wav')

freqs, times, Sx = signal.spectrogram(audio, fs=rate, window='hanning',
                                      nperseg=1024, noverlap=M - 100,
                                      detrend=False, scaling='density')

f, ax = plt.subplots(figsize=(9, 6))
print(np.abs(np.log10(Sx)))
ax.pcolormesh(times, freqs, np.log10(Sx), cmap='viridis')
ax.set_ylabel('Frequency [kHz]')
ax.set_xlabel('Time [s]')
plt.savefig('target/spectro.png')