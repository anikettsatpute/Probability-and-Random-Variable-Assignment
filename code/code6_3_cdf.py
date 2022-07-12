import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

def cdf_the_gen(x):
    if(x>0):
        return 1-mp.exp(-x**2/2)
    else:
        return 0

y=np.loadtxt('../Data/6_3.dat',dtype="double")
x=np.linspace(-1,8,50)
cdf_sim=[]

for i in range(0,50):
    cdf_sim.append(np.size(np.nonzero(y<x[i]))/1000000)

cdf_the=np.vectorize(cdf_the_gen,otypes=[np.float64])

plt.plot(x,cdf_the(x),color="blue",label="Theoretical")
plt.xlabel('$x$')
plt.ylabel('$F_A(x)$')
plt.legend(["Numerical","Theory"])
plt.scatter(x,cdf_sim,color="red",label="Simulated")
plt.legend()
plt.grid()
plt.savefig('../Figures/6_3_cdf.png')