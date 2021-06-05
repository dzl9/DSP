import os
import matplotlib.pyplot as plt
from thinkdsp import read_wave
from winsound import PlaySound
import time
def play(file, flags):
    print('Now play '+file)
    PlaySound(file, flags)
    print('end')

plt.rcParams['font.sans-serif'] = ['KaiTi']# 指定默认字体
plt.rcParams['axes.unicode_minus'] = False# 解决保存图像是负号'-'显示为方块的问题

wave = read_wave("170255__dublie__trumpet.wav")     #读取音频信号
wave.normalize()                                    #归一化
wave.make_audio()                                   
plt.subplot(3,3,1)
plt.title("原音频")
wave.plot()

segment = wave.segment(start=1.1, duration=0.3)     #复制wave中的一段，起始时间为1.1，长度为0.3
segment.make_audio()
plt.subplot(3,3,2)
plt.title("截取的1.1--1.4s音频")
segment.plot()

plt.subplot(3,3,3)
plt.title("截取的1.1--1.105s音频")
segment.segment(start=1.1, duration=0.005).plot()   #复制segment中的一段，起始时间为1.1，长度为0.005

spectrum = segment.make_spectrum()                  #把上面复制的一段从1.1--1.14的波形转换为频谱
plt.subplot(3,3,4)
plt.title("截取的1.1--1.4音频频谱(频率范围0-7000HZ)")
spectrum.plot(high=7000)                            #频率范围为0--7000HZ

spectrum = segment.make_spectrum()
plt.subplot(3,3,5)
plt.title("截取的1.1--1.4音频频谱(频率范围0-1000HZ)")
spectrum.plot(high=1000)                            #频率范围为0--1000HZ

a=spectrum.peaks()[:30]                             #峰显示频谱的最高点及其频率，按降序排列30个点
print (a)

#低通
def filter_wave(wave, start, duration, cutoff):
    segment = wave.segment(start, duration)
    spectrum = segment.make_spectrum()

    spectrum.plot(high=5000, color='0.7')       #以灰色的图像显示1.1-1.4s的频谱
    spectrum.low_pass(cutoff)                   #低通
    wave_lp = spectrum.make_wave()
    wave_lp.write(filename='wave_lp.wav')
    spectrum.plot(high=5000, color='#045a8d')   #低通处理后的图像用蓝色显示
    xlabel='Frequency (Hz)'
    play('wave_lp.wav', flags=1)
    time.sleep(1)                               # 等待1s运行下一条语句

#低通显示赋值
plt.subplot(3,3,7)
filter_wave(wave, 1.1, 0.3, 1000)


#高通
def filter_wave_hight(wave, start, duration, cutoff):
    segment = wave.segment(start, duration)
    spectrum = segment.make_spectrum()

    spectrum.plot(high=5000, color='0.7')       #以灰色的图像显示1.1-1.4s的频谱
    spectrum.high_pass(cutoff)                   #高通
    wave_hp = spectrum.make_wave()
    wave_hp.write(filename='wave_hp.wav')
    spectrum.plot(high=5000, color='#045a8d')   #高通处理后的图像用蓝色显示
    xlabel='Frequency (Hz)'
    play('wave_hp.wav', flags=1)
    time.sleep(1)                               # 等待1s运行下一条语句
#高通显示赋值
plt.subplot(3,3,8)
filter_wave_hight(wave, 1.1, 0.3, 1500)

#带阻
def filter_wave_hight(wave, start, duration, cutoff_l,cutoff_h):
    segment = wave.segment(start, duration)
    spectrum = segment.make_spectrum()

    spectrum.plot(high=5000, color='0.7')       #以灰色的图像显示1.1-1.4s的频谱
    spectrum.band_stop(cutoff_l ,cutoff_h)      #带通
    wave_base_stop = spectrum.make_wave()
    wave_base_stop.write(filename='wave_base_stop.wav')
    spectrum.plot(high=5000, color='#045a8d')   #带阻处理后的图像用蓝色显示
    xlabel='Frequency (Hz)'
    play('wave_base_stop.wav', flags=1)
    time.sleep(1)                               # 等待1s运行下一条语句
#带阻显示赋值
plt.subplot(3,3,9)
filter_wave_hight(wave, 1.1, 0.3, 1000,2000)



plt.show()
