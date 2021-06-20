from thinkdsp import decorate
from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
from thinkdsp import SquareSignal
import numpy as np
import matplotlib.pyplot as plt

square = SquareSignal(1100).make_wave(duration=0.5, framerate=10000)#对一个频率为1100HZ，进行一个采样频率为10000HZ长度为0.5s的采样

square.make_audio()
plt.subplot(121)
square.plot()
plt.xlim(0, 0.01)

plt.subplot(122)
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
plt.show()
