import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

def uni_cdf(i):
	mp.dps=7
	if(i<0):
		return 0
	elif(i<1):
		return i
	else:
		return 1

x = np.linspace(-4,4,50)
simlen = int(1e6)
err = []
randvar = np.loadtxt('../Data/uni.dat',dtype='double')
for i in range(0,50):
	err_ind = np.nonzero(randvar < x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

x_2 =np.linspace(-4,4,50)

def cdf(i):
	return uni_cdf(i)

vec_cdf = np.vectorize(cdf,otypes=[np.float64])

plt.plot(x_2.T,vec_cdf(x),color="blue",label="Theoretical")
plt.scatter(x.T,err,color="red",label="Simulated")
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_U(x)$')
plt.legend()

plt.savefig('../Figures/uni_cdf.pdf')
plt.savefig('../Figures/uni_cdf.eps')