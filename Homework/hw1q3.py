"""hw1w3.py -- Homework 1, Question 3

Patrick Fasano
ECT* TALENT School 2017
"""

import numpy as np
import matplotlib.pyplot as plt

data = {}
with open("rms13.dat") as fp:
    for line in fp:
        # skip comment lines
        if line[0] == '!':
            continue

        # split line into pieces, and parse into data dict
        tokens = line.split()
        (z, n, a, rms, error, *_) = tokens
        z = int(z)
        n = int(n)
        a = int(a)
        rms = float(rms)
        error = float(error)
        data[(z, n)] = (rms, error)

radii_differences = []
for (nuclide, value) in data.items():
    (z, n) = nuclide
    try:
        radius0 = value[0]
        radius1 = data[(z,n-1)][0]
        difference = radius0 - radius1
        radii_differences.append([n, difference])
    except:
        continue

plot_data = np.array(radii_differences)
plt.plot(plot_data[:,0], plot_data[:,1], '.')
plt.show()
