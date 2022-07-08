import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

def tri_pdf(i):
    if(i<0):
        return 0
    elif(i<1):
        return i
    elif(i<2):
        return 2-i
    else:
        return 0
    

maxrange=100
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)
simlen = int(1e6)
err = []
simu = []
h = 2*maxlim/(maxrange-1)

randvar = np.loadtxt('Data/4_1.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	simu.append(test)

x_2 = np.linspace(-maxlim,maxlim,maxrange)

def pdf(i):
    return tri_pdf(i)

vec_pdf = np.vectorize(pdf,otypes=[np.float64])


plt.plot(x_2.T,vec_pdf(x_2),color="blue",label="Theaurotical")
plt.scatter(x[0:(maxrange-1)].T,simu,color="red",label="Simulation")
plt.grid()
plt.xlabel('$x_i$')
plt.ylabel('$p_T(x_i)$')
plt.legend(["Numerical"])

plt.savefig('./Figures/4_5_pdf.pdf')
plt.savefig('./Figures/4_5_pdf.eps')