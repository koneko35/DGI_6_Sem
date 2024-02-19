from sympy import *
import numpy as np

x = Symbol("x")
k = Symbol("k")

y = 1 - np.exp(-k*x)

yprime = y.diff(x)
print(yprime)