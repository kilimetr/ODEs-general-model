# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
import os

os.chdir("/Users/kilimetr/Desktop/python/Clauss_process")

from model import mixer1, mixer2

Ca0 = 0
T0  = 350

Caf = 1
Tf  = 300

t    = np.linspace(0, 10, 100)
yini = [Ca0, T0]
args = (Caf, Tf)
pars = (Caf, Tf)

y  = odeint(mixer1, yini, t, args)
yy = odeint(lambda x, tt: mixer2(x, tt, pars), yini, t)

# print(len(y[:,0]))
# print(len(y[0,:]))
# print(y.shape)

plt.figure("Concentration and Temperature")

plt.subplot(2, 2, 1)
plt.plot(t, y[:,0], "r-", linewidth = 3)
plt.title("Concentration Progress")
plt.xlabel("Time [s]")
plt.ylabel("Concentration [mol/dm3]")
plt.legend(["Concentration"], loc = "best")

plt.subplot(2, 2, 2)
plt.plot(t, y[:,1], "b-.")
plt.title("Temperature Progress")
plt.xlabel("Time [s]")
plt.ylabel("Temperature [K]")
plt.legend(["Temperature"], loc = "best")

plt.subplot(2, 2, 3)
plt.plot(t, yy[:,0], "r-", linewidth = 3)
plt.title("Concentration Progress")
plt.xlabel("Time [s]")
plt.ylabel("Concentration [mol/dm3]")
plt.legend(["Concentration"], loc = "best")

plt.subplot(2, 2, 4)
plt.plot(t, yy[:,1], "b-.")
plt.title("Temperature Progress")
plt.xlabel("Time [s]")
plt.ylabel("Temperature [K]")
plt.legend(["Temperature"], loc = "best")

plt.show()