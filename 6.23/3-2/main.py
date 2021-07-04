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

from thinkdsp import Chirp
from thinkdsp import normalize, unbias

PI2 = 2 * np.pi

class SawtoothChirp(Chirp):
    """Represents a sawtooth signal with varying frequency."""

    def evaluate(self, ts):
        """Helper function that evaluates the signal.

        ts: float array of times
        """
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        cycles = phases / PI2
        frac, _ = np.modf(cycles)
        ys =  normalize(unbias(frac), self.amp)
        return ys

signal = SawtoothChirp(start=220, end=880)
wave = signal.make_wave(duration=1, framerate=4000)
#wave.apodize()
#wave.make_audio()

sp = wave.make_spectrogram(256)
sp.plot()
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')

plt.show()
