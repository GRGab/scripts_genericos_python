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

os.chdir(r'C:\Users\Gabo\Dropbox\Facultad\Labo 5\Conteo de fotones')

#%%
### El snippet propiamente dicho

####
valores_a_binear = np.random.normal(size=10000)
num_bines        = 100

graficos_path    =  ''
titulo_hist      = 'Título del histograma'
magnitud_x       = 'Distancia (m)'

ancho_bines      = 0.05 # Modificar o se va ver horrible
####


fig, ax = plt.subplots()
conteos, bordes_bines = np.histogram(valores_a_binear, bins=num_bines)
# Opcional: especificar número o posición de bines
# Opcional: normalizar con density=True
error = np.sqrt(conteos)
# Opcional: normalizar el error si se normalizan los conteos:
#error = np.sqrt(conteos)/np.sqrt(len(valores_a_binear))
ax.bar(bordes_bines[:-1], conteos, align='edge', color='dodgerblue',
       yerr=error, capsize=3, width=ancho_bines)
ax.set_title(titulo_hist, fontsize=16)
ax.set_xlabel(magnitud_x, fontsize=14)
fig.tight_layout()

# Guardar imagen
#plt.savefig(os.path.join(graficos_path, titulo_hist) + '.png')
plt.show()