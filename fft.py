from scipy import signal
from scipy.io import wavfile

# from scipy.io import wavfile


M = 1000
rate, audio = wavfile.read('wav_data/18-08-07_09_10_12.wav')

freqs, times, Sx = signal.spectrogram(audio, fs=rate, window='hanning',
                                      nperseg=1024, noverlap=M - 100,
                                      detrend=False, scaling='density')

print(freqs)
