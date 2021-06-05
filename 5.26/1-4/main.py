import thinkdsp
import matplotlib.pyplot as plt
from winsound import PlaySound
import time

def play(file, flags):
    print('Now play '+file)
    PlaySound(file, flags)
    print('end')

def strech(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor

plt.rcParams['font.sans-serif'] = ['KaiTi']# 指定默认字体
plt.rcParams['axes.unicode_minus'] = False# 解决保存图像是负号'-'显示为方块的问题

wave = thinkdsp.read_wave('170255__dublie__trumpet.wav')# 导入音频
wave.normalize()
play("170255__dublie__trumpet.wav", flags=8)

plt.subplot(221)
plt.title("原音频")
plt.xlim(0, 20)
wave.plot()
time.sleep(1)

strech(wave, 0.5)
plt.subplot(222)
plt.title("2倍速音频")
plt.xlim(0, 20)
wave.plot()
wave.write("base_2.wav")
play("base_2.wav", flags=8)
time.sleep(1)

strech(wave, 2)
wave.write("base.wav")
play("base.wav", flags=8)
plt.subplot(223)
plt.title("复原音频")
plt.xlim(0, 20)
wave.plot()
time.sleep(1)

strech(wave, 2)
wave.write("base_part.wav")
play("base_part.wav", flags=18)
plt.subplot(224)
plt.title("0.5倍速音频")
plt.xlim(0, 20)
wave.plot()
time.sleep(1)
plt.show()