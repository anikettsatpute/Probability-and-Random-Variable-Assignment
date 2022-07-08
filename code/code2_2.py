from cmath import exp
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import math as math
import scipy

def q_fun(i):
	mp.dps=7
	return mp.erfc(i/math.sqrt(2))/2


x = np.linspace(-4,4,50)
simlen = int(1e6)
err = []
randvar = np.loadtxt('../Data/gau.dat',dtype='double')
for i in range(0,50):
	err_ind = np.nonzero(randvar < x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

x_2 =np.linspace(-4,4,50)

def cdf(i): 
	return 1-q_fun(i)

vec_cdf = np.vectorize(cdf,otypes=[np.float64])

plt.plot(x_2.T,vec_cdf(x),color="blue",label="Theoretical")
plt.scatter(x.T,err,color="red",label="Simulated")
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend()

plt.savefig('../Figures/gau_cdf.pdf')
plt.savefig('../Figures/gau_cdf.eps')