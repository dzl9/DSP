from thinkdsp import decorate
from thinkdsp import TriangleSignal
import numpy as np
import matplotlib.pyplot as plt

triangle = TriangleSignal().make_wave(duration=0.01)#对一个频率为440HZ的三角波，进行一个采样频率为40000HZ长度为0.5s的采样

triangle.make_audio()
plt.subplot(121)
triangle.plot()
plt.xlim(0, 0.01)
decorate(xlabel='Time (s)')

plt.subplot(122)
triangle.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
spectrum = triangle.make_spectrum()
spectrum.hs[0]
print("spectrum.hs[0]",spectrum.hs[0])

spectrum.hs[0] = 100            #如果我们把零频率分量加上去，它的效果是给波加上一个垂直偏移量。
plt.subplot(121)
triangle.plot(color='gray')
spectrum.make_wave().plot()
decorate(xlabel='Time (s)')

plt.show()
