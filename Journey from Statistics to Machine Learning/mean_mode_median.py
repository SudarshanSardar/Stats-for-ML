import numpy as np
from scipy import stats


data = np.array([4, 5, 1, 2, 7, 2, 6, 9, 3])
print("Data : ", data)

# Mean
mean = np.mean(data)
print("Mean : ", mean)

# Median
median = np.median(data)
print("Median : ", median)

# Mean
mode = stats.mode(data)
print("Mode : ", mode[0][0])
