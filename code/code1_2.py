import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(-4,4,30)
simlen = int(1e6)
err = []
randvar = np.loadtxt('Data/uni.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

plt.plot(x.T,err)
plt.scatter(x.T,err,color="red")
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_U(x)$')

plt.savefig('./Figures/uni_cdf.pdf')
plt.savefig('./Figures/uni_cdf.eps')