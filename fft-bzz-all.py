import glob

import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile

# Pro vsechny soubory
files = glob.glob('wav_data/*.wav')
result = {}  # soubor := jak moc bzuci
for filename in files:
    rate, audio = wavfile.read(filename)

    # Vypise max. amplitudu v nejakem rozpeti frekvence pro dany soubor
    spectre = np.fft.fft(audio)
    freq = np.fft.fftfreq(audio.size, 1 / rate)

    maxAmp = 0
    for i in range(freq.size):
        f = freq[i]
        if 550 > f > 450: # jen zajimave frekvence bzuceno | TODO: mozna by se tu dalo vymyslet neco lepsiho (gauss?), nebo vybrat vice zajimavych frekvenci
            hodnotaComplex = spectre[i]
            hodnota = np.abs(hodnotaComplex)  # absolutní hodnota komplexního čísla
            if hodnota > maxAmp:
                maxAmp = hodnota # nová nejvyšší hodnota
    result[filename] = maxAmp
    # Vypis na vystup - asi je mozno i do souboru nebo do Elastic
    print("{} \t {}".format(filename, maxAmp))

f, ax = plt.subplots(figsize=(9, 6))
ax.set_ylabel('Jak moc bzučí')
ax.set_xlabel('Soubory v čase')
# TODO: vykuchat ze souboru datum a cas - na X ose ted neni nic videt
lists = sorted(result.items())  # sorted by key, return a list of tuples
x, y = zip(*lists)  # unpack a list of pairs into two tuples
plt.plot(x, y)
plt.show()
