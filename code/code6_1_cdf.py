from cmath import exp
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import math as math
import scipy

def v_cdf(i):
    if (i < 0): return 0
    else: return 1 - np.exp(-i/2)


x = np.linspace(0,10,100)
simlen = int(1e6)
err = []
randvar = np.loadtxt('../Data/6_1_2.dat',dtype='double')
for i in range(0,100):
	err_ind = np.nonzero(randvar < x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

x_2 =np.linspace(0,10,100)

vec_cdf = np.vectorize(v_cdf,otypes=[np.float64])

plt.plot(x_2.T,vec_cdf(x),color="blue",label="Theoretical")
plt.scatter(x.T,err,color="red",label="Simulated")
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_V(x)$')
plt.legend()

plt.savefig('../Figures/6_1_cdf.pdf')
plt.savefig('../Figures/6_1_cdf.eps')