# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:29:31 2019

@author: WS1
"""

import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 0.5, 0.1
s = np.random.normal(mu, sigma, 100)

# Create the bins and histogram
count, bins, ignored = plt.hist(s, 20, normed=True)

# Plot the distribution curve
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ),       linewidth=3, color='y')
plt.show()