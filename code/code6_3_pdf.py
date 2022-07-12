import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt


maxrange=100
x = np.linspace(-4,14,maxrange)
simlen = int(1e6)
err = []
pdf = []

randvar = np.loadtxt('../Data/6_3.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test)

def v_pdf(i):
    if (i >= 0): return i*np.exp(-(i**2)/2)
    else: return 0
	
vec_v_pdf = scipy.vectorize(v_pdf,otypes=[np.float64])

plt.scatter(x[0:(maxrange-1)].T,pdf,color="red")
plt.plot(x,vec_v_pdf(x),color="blue")
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$p_\sqrt{V}(x)$')
plt.legend(["Numerical","Theory"])

plt.savefig('../Figures/6_3_pdf.pdf')
plt.savefig('../Figures/6_3_pdf.eps')