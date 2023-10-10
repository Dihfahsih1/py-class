from scipy import stats
import numpy as np

from scipy import linalg

A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
x = linalg.solve(A, b)
print(x)
