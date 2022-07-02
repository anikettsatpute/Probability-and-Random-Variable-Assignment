import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4,4,30)
simlen = int(1e6)
err = []
randvar = np.loadtxt('Data/gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

	
plt.plot(x.T,err)
plt.scatter(x.T,err,color="red")
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

plt.savefig('./Figures/gau_cdf.pdf')
plt.savefig('./Figures/gau_cdf.eps')