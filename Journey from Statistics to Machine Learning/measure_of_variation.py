import numpy as np
from statistics import variance, stdev


game_points = np.array([35, 56, 43, 59, 63, 79, 35, 41, 64, 43, 93, 60, 77, 24, 82])

# Calculate Variance
dt_var = variance(game_points)
print('Sample variance :', round(dt_var, 2))

# Calculate Standard Deviation
dt_std = stdev(game_points)
print('Sample standard Deviation :', round(dt_std, 2))

# Calculate Range
dt_rng = np.max(game_points, axis=0) - np.min(game_points, axis=0)
print('Range : ', dt_rng)

# Calculate percentiles
print('Quantiles:')
for val in [20, 80, 100]:
    dt_quantiles = np.percentile(game_points, val)
    print(str(val) + "%", dt_quantiles)

# Calculate IQR
q75, q25 = np.percentile(game_points, [75, 25])
print("Inter quartile range:", q75-q25)
