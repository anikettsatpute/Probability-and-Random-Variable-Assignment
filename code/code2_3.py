import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt


maxrange=50
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)
simlen = int(1e6)
err = []
pdf = []
h = 2*maxlim/(maxrange-1);

randvar = np.loadtxt('gau.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test)

def gauss_pdf(x):
	return 1/mp.sqrt(2*np.pi)*np.exp(-x**2/2.0)
	
vec_gauss_pdf = scipy.vectorize(gauss_pdf)

plt.plot(x[0:(maxrange-1)].T,pdf,'o')
plt.plot(x,vec_gauss_pdf(x))
plt.grid()
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])

plt.savefig('gauss_pdf.pdf')
plt.savefig('gauss_pdf.eps')
