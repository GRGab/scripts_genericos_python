# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 20:30:11 2018

@author: Gabo
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(1000)
y, bin_edges = np.histogram(x, bins=10)
bin_centers = 0.5*(bin_edges[1:] + bin_edges[:-1])

plt.errorbar(
    bin_centers,
    y,
    yerr = y**0.5,
    marker = '.',
    drawstyle = 'steps-mid'
)
plt.show()