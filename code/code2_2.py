import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4,4,30)
simlen = int(1e6)
err = []
randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

	
plt.plot(x.T,err)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_U(x)$')

plt.savefig('./gau_cdf.pdf')
plt.savefig('./gau_cdf.eps')