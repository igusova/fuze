%matplotlib inline
import matplotlib.pyplot as plt
import math
import numpy as np
def func(x):
    f = math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)
    return f
func(1)
w = np.array([[1,1],[1,15]])
y = np.array([3.25,0.63])
np.linalg.solve(w,y)
x = np.arange(0, 5)
y = 3.43-0.187*x
plt.plot(x, y)
plt.show()
