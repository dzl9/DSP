from thinkdsp import decorate
from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
import numpy as np
import matplotlib.pyplot as plt

class SawtoothSignal(Sinusoid):
    """Represents a sawtooth signal."""
    
    def evaluate(self, ts):
        """Evaluates the signal at the given times.

        ts: float array of times
        
        returns: float wave array
        """
        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys

sawtooth = SawtoothSignal().make_wave(duration=0.5, framerate=40000) #对一个锯齿波进行一个长度为0.5s，采样频率为40khz的采样
sawtooth.make_audio()
plt.subplot(221)
sawtooth.plot()
plt.xlim(0, 0.01)
#plt.ylim(-1.5, 1.5)

plt.subplot(222)
sawtooth.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')

plt.subplot(223)
sawtooth.make_spectrum().plot()
plt.xlim(0, 2300)
decorate(xlabel='Frequency (Hz)')

plt.show()
