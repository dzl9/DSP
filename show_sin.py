#调用库
import matplotlib.pyplot as plt
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)
y = np.sin(x)#生成x关于sin所对应的值y
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#在画布的第一行第一列显示图像
plt.subplot(1,2,1)
plt.title(r'$f(x)=sin(x)$') #显示标题f(x)=sin(x)
plt.plot(x, y)#以(x,y)为坐标绘制y=sin(x)
#plt.show()

x1 = [t*0.375*np.pi for t in x]#生成相当于与x的3/8πx的点
y1 = np.sin(x1)#生成x1关于sin所对应的值y
#在画布的第一行第二列显示图像
plt.subplot(1,2,2)
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #显示标题f(x)=sin(3/8πx)
plt.plot(x, y1)#以(x,y1)为坐标绘制y=sin(3/8πx)
plt.show()#显示
