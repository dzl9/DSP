from thinkdsp import decorate
from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
from thinkdsp import SinSignal
import numpy as np
import matplotlib.pyplot as plt
from winsound import PlaySound
import thinkdsp
import time

def play(file, flags):
    print('Now play '+file)
    PlaySound(file, flags)
    print('end')

from thinkdsp import Chirp
from thinkdsp import normalize, unbias

PI2 = 2 * np.pi

class TromboneGliss(Chirp):
    """Represents a trombone-like signal with varying frequency."""
    
    def evaluate(self, ts):
        """Evaluates the signal at the given times.

        ts: float array of times
        
        returns: float wave array
        """
        l1, l2 = 1.0 / self.start, 1.0 / self.end
        lengths = np.linspace(l1, l2, len(ts))
        freqs = 1 / lengths
        
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        ys = self.amp * np.cos(phases)
        return ys

low = 262
high = 349
signal = TromboneGliss(high, low)
wave1 = signal.make_wave(duration=1)
wave1.apodize()
wave1.make_audio()

signal = TromboneGliss(low, high)
wave2 = signal.make_wave(duration=1)
wave2.apodize()
wave2.make_audio()

wave = wave1 | wave2
wave.make_audio()

sp = wave.make_spectrogram(1024)
sp.plot(high=1000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')



plt.show()
