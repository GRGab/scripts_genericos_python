# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 21:27:33 2018

@author: Gabo
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

data = np.random.normal(size=10000)

# plt.hist gives you the entries, edges 
# and drawables we do not need the drawables:
entries, edges, _ = plt.hist(data, bins=25, range=[-5, 5])

# calculate bin centers
bin_centers = 0.5 * (edges[:-1] + edges[1:])

# draw errobars, use the sqrt error. You can use what you want there
# poissonian 1 sigma intervals would make more sense
plt.errorbar(bin_centers, entries, yerr=np.sqrt(entries), fmt='b.')

plt.show()