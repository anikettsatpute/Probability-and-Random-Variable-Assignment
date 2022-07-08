import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import math as math

def log_cdf(i):
	mp.dps=7
	if(i<0):
		return 0
	else:
		return (1-math.exp(-i/2))

x = np.linspace(-4,4,100)
simlen = int(1e6)
err = []
randvar = np.loadtxt('Data/3_1.dat',dtype='double')
for i in range(0,100):
	err_ind = np.nonzero(randvar < x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

x_2 =np.linspace(-4,4,100)

def cdf(i):
	return log_cdf(i)

vec_cdf = np.vectorize(cdf,otypes=[np.float64])


plt.plot(x_2,vec_cdf(x),color="blue",label="Theaurotical")
plt.scatter(x.T,err,color="red",label="Simulated")
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_V(x)$')
plt.legend()

plt.savefig('./Figures/3_1_cdf.pdf')
plt.savefig('./Figures/3_1_cdf.eps')
