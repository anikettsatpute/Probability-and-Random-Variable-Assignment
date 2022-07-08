
import numpy as np
import mpmath as mp
from matplotlib import pyplot as plt
import scipy

bv = np.loadtxt('../Data/5_1.dat', dtype='double')
nv = np.loadtxt('../Data/gau.dat', dtype='double')

def P_e(a):
    y = a*bv + nv
    count1 = np.count_nonzero(bv > 0)
    count2 = np.count_nonzero(bv < 0)
    e0 = np.count_nonzero((y < 0) & (bv > 0)) 
    e1 = np.count_nonzero((y > 0) & (bv < 0))
    return 0.5*(e0/count1 + e1/count2)

vec_P_e = scipy.vectorize(P_e, otypes=['double'])

def q_fun(x):
    return (0.5)*mp.erfc(x/np.sqrt(2))

qfunc_vec = scipy.vectorize(q_fun, otypes=['double'])

x = np.linspace(0,10,11)
a = np.linspace(0,10,11)
plt.plot(a, vec_P_e(a),label="Simulation",color="red")
plt.scatter(x, qfunc_vec(x),label="Theauretical",color="blue")
plt.grid()
plt.xlabel('$A$ (dB)')
plt.ylabel('$P_e(A)$')
plt.legend()
plt.savefig('../Figures/5_7.png')