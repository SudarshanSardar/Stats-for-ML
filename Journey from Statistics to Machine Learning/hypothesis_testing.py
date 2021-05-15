from scipy import stats
import numpy as np


x_bar = 990
mu0 = 1000
s = 12.5
n = 30

# Test Statistic
t_sample = (x_bar-mu0)/(s/np.sqrt(float(n)))
print("Test Statistic:", round(t_sample, 2))

# Critical value from t-table
alpha = 0.05
t_alpha = stats.t.ppf(alpha, n-1)
print("Critical value from t-table:", round(t_alpha, 3))

# Lower tail p-value from t-table
p_val = stats.t.sf(np.abs(t_sample), n-1)
print("Lower tail p-value from t-table", p_val)
