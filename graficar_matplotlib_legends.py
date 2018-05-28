# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:41:21 2018

@author: Gabo
"""

import numpy as np
import matplotlib.pyplot as plt
import os

#%%

## Importar datos ##
# Funciones útiles:
# np.loadtxt, np.load, np.genfromtxt, csv.reader (leer: https://docs.python.org/2/library/csv.html)

os.chdir(r'un\path\cualquiera')

#%%

####

xs = np.linspace(0, 4, 10000)
ys1 = np.sin(xs) + 0.2 * np.random.normal(size=10000)
ys2 = ys1**2


graficos_path    =  'Graficos'
titulo           = 'Título'
magnitud_x       = 'Magnitud (unidades)'
magnitud_y       = 'Magnitud (unidades)'

####

plt.style.use('seaborn')

#Estilos disponibles:
['bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot',
 'grayscale', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette',
 'seaborn-dark', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted',
 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster',
 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid',
 'seaborn', 'Solarize_Light2', '_classic_test']

fig, ax = plt.subplots()

ax.plot(xs, ys1, '.', label='Unos datos')
ax.plot(xs, ys2, '.', label='Otros datos')
ax.set_title(titulo_hist, fontsize=16)
ax.set_xlabel(magnitud_x, fontsize=14)
ax.set_ylabel(magnitud_y, fontsize=14)
ax.legend()
fig.tight_layout()

# Guardar imagen
#plt.savefig(os.path.join(graficos_path, titulo_hist) + '.png')
plt.show()
