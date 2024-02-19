import scipy.io
import matplotlib.pyplot as plt
import numpy as np

mat = scipy.io.loadmat('matlab.mat')
x = mat['skiraw'][:,0].real


# plt.plot(xdata,ydata, linewidth=2, color='b')
# plt.show()
# print(x)
l = 1

w = l*np.exp(-l*x)
p = np.cumsum(w*x)
m = np.cumsum(w*x*x)
d = np.cumsum(w*(x-m)**2*x)


# 1 гистограмма
# patches = plt.hist(x, bins=20)
# print(p,' ',m,' ',d)
plt.plot(x,w)
plt.show()

