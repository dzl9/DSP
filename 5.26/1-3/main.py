import thinkdsp
import matplotlib.pyplot as plt
from winsound import PlaySound
import time

plt.rcParams['font.sans-serif'] = ['KaiTi']# 指定默认字体
plt.rcParams['axes.unicode_minus'] = False# 解决保存图像是负号'-'显示为方块的问题

def play(file, flags):
    print('Now play '+file)
    PlaySound(file, flags)
    print('end')

sin = thinkdsp.SinSignal(freq=400, amp=1.0)         #生成一个sin信号
cos = thinkdsp.CosSignal(freq=800, amp=0.5)        #生成一个cos信号
cos2= thinkdsp.CosSignal(freq=666, amp=1.0)
sin2= thinkdsp.SinSignal(freq=1234,amp=1.0)
signal = cos+sin                                    #生成一个有sin和cos相加的信号
signal2= signal+cos2+sin2
plt.subplot(2,2,1)
plt.title("复合信号")
signal.plot()
wave = signal.make_wave(duration=1)                 #把生成时间为1s的音频
spectrum = wave.make_spectrum()                     #把上述音频转化为频谱
plt.subplot(2,2,2)
plt.title("复合信号频谱")
spectrum.plot(high=4000)
wave.normalize()
wave.write("sum.wav")                               #保存音频
play("sum.wav", flags=1)
time.sleep(1)

plt.subplot(2,2,3)
plt.title("复合信号2")
signal2.plot()
wave2 = signal2.make_wave(duration=1)                 #把生成时间为1s的音频
spectrum2 = wave2.make_spectrum()                     #把上述音频转化为频谱
plt.subplot(2,2,4)
plt.title("复合信号频谱2")
spectrum2.plot(high=4000)
wave2.normalize()
wave2.write("sum2.wav")                               #保存音频
play("sum2.wav", flags=1)

plt.show()