from cmath import exp
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import math as math
import scipy

def tri(i):
	if(i<0):
		return 0
	elif(i<1):
		return (i*i)/2
	elif(i<2):
		return (-i*i)/2 + 2*i -1
	else:
		return 1


x = np.linspace(-4,4,50)
simlen = int(1e6)
err = []
randvar = np.loadtxt('Data/4_1.dat',dtype='double')
for i in range(0,50):
	err_ind = np.nonzero(randvar < x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

x_2 =np.linspace(-4,4,50)

def cdf(i):
	return tri(i)
vec_cdf = np.vectorize(cdf,otypes=[np.float64])

plt.plot(x_2.T,vec_cdf(x_2),color="blue",label="Simulated")
plt.scatter(x.T,err,color="red",label="Theoretical")
plt.grid()
plt.xlabel('$T$')
plt.ylabel('$F_T(x)$')
plt.legend()

plt.savefig('./Figures/4_5_cdf.pdf')
plt.savefig('./Figures/4_5_cdf.eps')