import numpy as np

def integrand(x):
#  return 1/(x**2 + 1)
  return x

N = 1_000_000 # how many random numbers?
rng = np.random.default_rng() # default random number generator

xmin = 0.0
xmax = 1.0
ymax = 1.0

x = xmin + (xmax-xmin)*rng.random(N)
y = ymax*rng.random(N)

myint = np.count_nonzero(y <= integrand(x))/N
print(f"With {N} rain drops...")
print(f"Integral = {myint:7.5f}")
