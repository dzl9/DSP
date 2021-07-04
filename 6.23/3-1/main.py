from thinkdsp import decorate
from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
from thinkdsp import SinSignal
import numpy as np
import matplotlib.pyplot as plt
from winsound import PlaySound
import time

def play(file, flags):
    print('Now play '+file)
    PlaySound(file, flags)
    print('end')

signal = SinSignal(freq=440)
duration = signal.period * 30.25
wave = signal.make_wave(duration)
spectrum = wave.make_spectrum()
#plt.subplot(121)
spectrum.plot(high=880)
decorate(xlabel='Frequency (Hz)')

for window_func in [np.bartlett, np.blackman, np.hamming, np.hanning]:
    wave = signal.make_wave(duration)
    wave.ys *= window_func(len(wave.ys))
    wave.write("test.wav")
    play("test.wav", flags=18)
    time.sleep(1)
    spectrum = wave.make_spectrum()
    spectrum.plot(high=880, label=window_func.__name__)

decorate(xlabel='Frequency (Hz)')

plt.show()
