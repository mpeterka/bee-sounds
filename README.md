# bee-sounds

Analýza zvuků ve včelím úlu.

# Technické záležitosti:
Testováno na Python 3.7.1, Win.

Upgrade PIP

    python -m pip install --upgrade pip
    
SciPy (pronounced “Sigh Pie”) is a Python-based ecosystem of open-source software for mathematics, science, and engineering.

    python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

# Soubory

* [wav_data/*.wav](wav_data) nahrávky z úlu od Lukáše Širhala
* [fft.py](fft.py): Vykreslí graf frekvencí a jejich sílu - Fourierova transformace
* [spectro.py](spectro.py): Spektrograf (od Lukáše Širhala)
* [fft-bzz-all.py](fft-bz-all.py): Projde všechny audio a v zajímavém pásmu (450 - 550 kHz) a najde nejvyšší amplitudu. 
To vypíše na výstup a do grafu.
Mělo by odpovídat aktivitě včelstev.
  * Zde by se mělo pokračovat.*
