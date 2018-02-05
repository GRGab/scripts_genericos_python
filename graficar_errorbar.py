#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:13:08 2017

@author: gabo
"""

import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline
# %%

# Datos teóricos de relleno
xs = np.linspace(0, 10, 100)
ysteo = np.sin(xs)

# Datos experimentales de relleno
ysexp = ysteo + np.random.normal(loc=0, scale=0.1, size=100)
xerrs = np.ones(100) * 1
yerrs = np.ones(100) * 0.1


# %%
# La verdad de la milanesa:

fig, ax = plt.subplots()
ax.plot(xs, ysteo, 'x', color='gray', label='Modelo teórico')
ax.errorbar(xs, ysexp, yerr=yerrs, xerr=xerrs, fmt='.k',
            capsize=0, elinewidth=0.3, label='Medición experimental')
# capsize=0 hace que no aparezcan las barritas en los bordes que no te gustan
# elinewidth controla qué tan finitas son las barras de error
ax.set_xlabel('Esto es el eje x (unidades)')
ax.set_ylabel('Esto es el eje y (unidades)')
ax.legend()  # Muestra los labels de los puntos dibujados
