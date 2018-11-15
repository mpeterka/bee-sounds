from scipy import signal
from scipy.io import wavfile
import glob
import numpy as np
import matplotlib

matplotlib.use('agg')
from matplotlib import pyplot as plt


def main():
    files = glob.glob('wav_data/*.wav')
    result = {}
    for filename in files:
        rate, audio = wavfile.read(filename)
        freqs, times, Sx = signal.spectrogram(audio, fs=rate, window='hanning',
                                              nperseg=1024,
                                              detrend=False, scaling='density')
        data_test = Sx
        temp_res = []
        for i in range(data_test.shape[0]):
            s = 20 * np.log10(data_test[i])
            hod = freqs[np.argmax(s)]
            temp_res.append(hod)

        if len(temp_res) > 0:
            avg = np.average(temp_res)
            print(avg)
            result[filename] = avg

    f, ax = plt.subplots(figsize=(9, 6))
    ax.set_ylabel('bzucak')
    ax.set_xlabel('files')
    lists = sorted(result.items())
    x, y = zip(*lists)
    plt.plot(x, y)
    plt.savefig('target/spectroFig.png')


if __name__ == "__main__":
    main()
