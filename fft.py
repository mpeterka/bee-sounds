import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile

matplotlib.use('agg')

rate, audio = wavfile.read('wav_data/18-08-07_09_10_12.wav')

# Vykresli graf frekvenci
f, ax = plt.subplots(figsize=(9, 6))
ax.set_ylabel('Amplituda')
ax.set_xlabel('Frekvence [kHs]')
spectre = np.fft.fft(audio)
freq = np.fft.fftfreq(audio.size, 1 / rate)
mask = freq > 450 # kHz
plt.plot(freq[mask], np.abs(spectre[mask]))
plt.savefig('target/fft.png')
