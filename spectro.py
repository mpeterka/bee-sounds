import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal
from scipy.io import wavfile

matplotlib.use('agg')

rate, audio = wavfile.read('wav_data/18-08-07_09_10_12.wav')

freqs, times, Sx = signal.spectrogram(audio,
                                      fs=rate,
                                      window='hanning',
                                      nperseg=512,
                                      noverlap=None,
                                      detrend=False,
                                      scaling='spectrum')

f, ax = plt.subplots(figsize=(9, 6))
ax.pcolormesh(times, freqs, np.log10(Sx), cmap='viridis')
ax.set_ylabel('Frequency [kHz]')
ax.set_xlabel('Time [s]')
plt.savefig('target/spectro.png')
