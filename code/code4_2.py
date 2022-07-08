import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(-4,4,100)
simlen = int(1e6)
err = []
randvar = np.loadtxt('Data/4_1.dat',dtype='double')
for i in range(0,100):
	err_ind = np.nonzero(randvar < x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

plt.scatter(x.T,err,color="red")
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_T(x)$')

plt.savefig('./Figures/4_2_CDF.pdf')
plt.savefig('./Figures/4_2_CDF.eps')