from glob import glob
from datetime import datetime
from scipy.io import wavfile
import numpy as np

import matplotlib

matplotlib.use('agg')
from matplotlib import pyplot as plt


class BeeWaveProcessor:
    def __init__(self):
        self.FILES = glob('wav_data/*.wav')
        self.CUT_INDEX = 0

    def process(self):
        print("Start bee wav processing")
        for filename in self.FILES:
            self.wave_process(filename)

    def wave_process(self, filename):
        print("Work on {}".format(filename))
        rate, audio = wavfile.read(filename)
        rff_audio = np.fft.rfft(audio)
        rff_abs = abs(rff_audio)
        frequencies = np.fft.rfftfreq(audio.shape[0], 1 / rate)
        rff_abs = rff_abs[:int(frequencies.size / 2)]
        frequencies = frequencies[:int(frequencies.size / 2)]

        self.filter_lower_frequencies(frequencies)
        frequencies = frequencies[self.CUT_INDEX:]
        rff_abs = rff_abs[self.CUT_INDEX:]

        file_time = self.file_time_resolver(filename)
        self.frequency_processor(file_time, frequencies, rff_abs)

        # numerous_frequency = self.get_numerous_frequency(frequencies, rff_abs)
        #
        # print("{} - frequency {} Hz".format(file_time, numerous_frequency))
        # self.make_plot(file_time, frequencies, rff_abs)

    def frequency_processor(self,filename, frequencies, rff_abs):
        to_350_index = 0
        to_600_index = 0
        to_1000_index = 0
        to_2000_index = 0

        for i in range(frequencies.shape[0]):
            if frequencies[i] < 350:
                to_350_index = i
            elif frequencies[i] < 600:
                to_600_index = i
            elif frequencies[i] < 1000:
                to_1000_index = i
            elif frequencies[i] < 2000:
                to_2000_index = i
            else:
                break
        from_180_to_350_frq = frequencies[:to_350_index]
        from_180_to_350_data = rff_abs[:to_350_index]
        from_350_to_600_frq = frequencies[to_350_index:to_600_index]
        from_350_to_600_data = rff_abs[to_350_index:to_600_index]
        from_600_to_1000_frq = frequencies[to_600_index:to_1000_index]
        from_600_to_1000_data = rff_abs[to_600_index:to_1000_index]
        from_1000_to_2000_frq = frequencies[to_1000_index:to_2000_index]
        from_1000_to_2000_data = rff_abs[to_1000_index:to_2000_index]

        hz_180_to_350 = from_180_to_350_frq[np.argmax(from_180_to_350_data)]
        hz_350_to_6 = from_350_to_600_frq[np.argmax(from_350_to_600_data)]
        hz_6_to_10 = from_600_to_1000_frq[np.argmax(from_600_to_1000_data)]
        hz_10_to_20 = from_1000_to_2000_frq[np.argmax(from_1000_to_2000_data)]

        print("180 - 350: {} Hz".format(hz_180_to_350))
        print("350 - 600: {} Hz".format(hz_350_to_6))
        print("600 - 1000: {} Hz".format(hz_6_to_10))
        print("1000 - 2000: {} Hz".format(hz_10_to_20))
        print("-------------next-------------")

        f, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=(24.8, 12.4), sharex=False, sharey=False)
        ax1.plot(from_180_to_350_frq, from_180_to_350_data)
        ax1.grid(True)

        ax2.plot(from_350_to_600_frq, from_350_to_600_data)
        ax2.grid(True)

        ax3.plot(from_600_to_1000_frq, from_600_to_1000_data)
        ax3.grid(True)

        ax4.plot(from_1000_to_2000_frq, from_1000_to_2000_data)
        ax4.grid(True)

        plt.savefig('target/bee_wave/{}.png'.format(filename))
        plt.clf()
        plt.close(f)

    def get_numerous_frequency(self, frequencies, rff_abs):
        return frequencies[np.argmax(rff_abs)]

    def filter_lower_frequencies(self, frequencies):
        for i in range(frequencies.shape[0]):
            if frequencies[i] < 180:
                self.CUT_INDEX = i
            else:
                break

    def file_time_resolver(self, filename):
        f1 = filename[9:]
        return f1[0:17]

    def file_time_to_UTC_time(self, file_time):
        d_object = datetime.strptime(file_time, '%y-%m-%d_%H_%M_%S')
        return d_object.strftime('%Y-%m-%dT%H:%M:%S-0000')


    def make_plot(self, filename, frequencies, rff_abs):
        fig, ax = plt.subplots(figsize=(24.8, 12.4))
        # plt.xlim([10, samplerate / 2])
        plt.xscale('log')
        plt.grid(True)
        plt.xlabel('Frequency (Hz)')
        plt.plot(frequencies, rff_abs)
        plt.savefig('target/bee_wave/{}.png'.format(filename))
        plt.clf()
        plt.close(fig)


if __name__ == '__main__':
    processor = BeeWaveProcessor()
    processor.process()
