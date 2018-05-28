# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:27:50 2018

@author: Gabo

Colormaps:

Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r,
CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys,
Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r,
Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r,
PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy,
RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1,
Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Vega10, Vega10_r,
Vega20, Vega20_r, Vega20b, Vega20b_r, Vega20c, Vega20c_r, Wistia, Wistia_r,
YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot,
afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr,
bwr_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix,
cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r,
gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r,
gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2,
gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno,
inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r,
ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow,
rainbow_r, seismic, seismic_r, spectral, spectral_r, spring, spring_r,
summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c,
tab20c_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.axes_grid1 import make_axes_locatable

#%%
# un ejemplo de heatmap
path_input = r'C:\Users\Gabo\Dropbox\Facultad\Labo 5\Fluidos\Clase 4'
path_inicial = os.getcwd()
os.chdir(path_input)
x, y, _, _, vort = np.loadtxt('med_laser_3_CLAHE5_highpass20_130_80_30_solo50_calib.txt',
                              skiprows=3, delimiter=',').T
os.chdir(path_inicial)

x = np.unique(x)
y = np.unique(y)
vort_grid = np.reshape(vort, (len(y), len(x)), order='F')
una_matriz = vort_grid
#%%

bitmap = una_matriz
xmin, xmax, ymin, ymax = 0, 1, 0, 1
interpolation = 'None'
cmap = 'coolwarm'

fig, ax = plt.subplots()
heatmap = ax.imshow(bitmap, origin='upper',
                    extent=(xmin, xmax, ymin, ymax),
                    interpolation=interpolation,
                    cmap=cmap)

divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.05)
cax.set_xlabel('[u.a.]')
ax.set_xticks(ax.get_xticks()[:-1]) #si el último xtick se solapa con el xlabel
fig.colorbar(heatmap, cax=cax, orientation='vertical')
fig.tight_layout()