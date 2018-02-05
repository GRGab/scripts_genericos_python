#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:05:02 2017

@author: gabo
"""
import numpy as np
import matplotlib.pyplot as plt

def Vcentr(r, L=0.5, m1=1):
    return L**2/(2 * m1 * r**2)

def V(r, m2=2, l=0.5):
    return  m2 * 9.8 * (r-l)


rs = np.linspace(0,2,1000)

fig, ax = plt.subplots()
#ax.cla()

ax.plot(rs, V(rs), '--k', label='$V(r)$')
ax.plot(rs, Vcentr(rs), '-.k', ms=1, label='$V_{cen}(r) = \dfrac{L^2}{2 m_1 r^2}$')
ax.plot(rs, V(rs) + Vcentr(rs), '-', color='dodgerblue', linewidth=3, label='$V_{ef}(r) = V(r) + V_{cen}(r)$')


### Graficar los ejes
ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')

### Eliminar ticks
plt.xticks([])
plt.yticks([])

ax.set_xlim(-0.02, 1)
ax.set_ylim(-12,50)

ax.legend()
plt.tight_layout

plt.plot()