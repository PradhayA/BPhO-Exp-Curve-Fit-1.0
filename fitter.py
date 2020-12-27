# This is the algorithm used for curve fitting for the BPHO Experimental project

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Dataset as obtained from the experiment
x = [0.723938224, 0.965250965, 1.206563707, 1.447876448, 1.689189189, 1.930501931, 2.171814672]
y = [2.758, 2.443, 2.142333333, 1.911, 1.817666667, 1.688333333, 1.616]


# Curve fit equation for the power law a/(x^b)
def func(x, a, b):
    global r
    global s
    r = a
    s = b
    return a / (x ** b)


# start values, not really necessary here but good to know the concept
p0 = [2, 0.5]
# the actual curve fitting, returns the parameters in popt and the covariance matrix in pcov
popt, pcov = curve_fit(func, np.asarray(x), np.asarray(y), p0)
# Curve equation
equation = 'y = %.5f  / (x^(%.5f))' % (r, s)
print(equation)

# plot the function to see, if the fit is any good
# first the raw data
plt.scatter(x, y, color="blue", label="raw data")
# then the fitted curve
x_fit = np.linspace(0.9 * min(x), 1.1 * max(x), 1000)
y_fit = func(x_fit, *popt)

plt.plot(x_fit, y_fit, color="red", label="fitted data")
plt.xlabel("Depth(cm)")
# Calculate Standard Deviation of Data for a and b values
error = np.sqrt(np.diag(pcov))
print(error)
plt.ylabel("Period(s)")
plt.title("Period vs Depth")
plt.grid()
plt.legend()
plt.show()

print("a: ", error[0])
print("b: ", error[1])
print("Percentage error for a: ", (((error[0]) / r) * 100), "%")
print("Percentage error for b: ", (((error[1]) / s) * 100), "%")
