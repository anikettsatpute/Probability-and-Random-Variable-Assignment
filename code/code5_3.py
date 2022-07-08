import numpy as np
import matplotlib.pyplot as plt

Y = np.loadtxt('../Data/5_2.dat',dtype='double')

X = np.linspace(0,1000000,1000000)

plt.scatter(X,Y,label="Simulated")

plt.grid()
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.legend()

plt.savefig('../Figures/5_3_YvsX.png')
#plt.savefig('./Figures/5_3_YvsX.eps')