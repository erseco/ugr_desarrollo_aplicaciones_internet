#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#
# DAI - Desarrollo de Aplicaciones para Internet
#
# 2014 Ernesto Serrano <erseco@correo.ugr.es>
#
#-----------------------------------------------

Implemente el Juego de la Vida (http://es.wikipedia.org/wiki/Juego_ de_la_vida). 
La salida de cada iteracion debe guardarse en ficheros de texto con nombre consecutivo. 
Opcionalmente, se puede usar la biblioteca graphics.py para mostrar la evolucion del juego como imagenes 
en vez de ficheros de texto. N
ota: Si ejecutas los ejercicios en una maquina virtual sin escritorio deberas hacer un X11 fordwarding 
(parametro -X en el comando ssh) para poder visualizar ventanas con graphics.py. 
En Ubuntu Server es posible que necesite instalar el paquete python-tk.

'''
 
from time import sleep
 
import numpy as np

import matplotlib
matplotlib.use('TKAgg')

import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import animation
 
def vecindario(b):
    """Array de células vivas en el vecindario."""
    vecindario = (
        np.roll(np.roll(b, 1, 1), 1, 0) +  # Abajo-derecha
        np.roll(b, 1, 0) +  # Abajo
        np.roll(np.roll(b, -1, 1), 1, 0) +  # Abajo-izquierda
        np.roll(b, -1, 1) +  # Izquierda
        np.roll(np.roll(b, -1, 1), -1, 0) +  # Arriba-izquierda
        np.roll(b, -1, 0) +  # Arriba
        np.roll(np.roll(b, 1, 1), -1, 0) +  # Arriba-derecha
        np.roll(b, 1, 1)  # Derecha
    )
    return vecindario
 
 
def paso(b):
    """Paso en el juego de la vida de Conway."""
    v = vecindario(b)
    buffer_b = b.copy()  # Hacemos una copia de la matriz
    for i in range(buffer_b.shape[0]):
        for j in range(buffer_b.shape[1]):
            if v[i, j] == 3 or (v[i, j] == 2 and buffer_b[i, j]):
                buffer_b[i, j] = 1
            else:
                buffer_b[i, j] = 0
    return buffer_b
 
 
# Parámetros del problema
GENERACIONES = 50
N = 8
M = 8
 
# Construimos el tablero
tablero = np.zeros((N, M), dtype=int)
 
# Añadimos una nave
tablero[1, 1:4] = 1
tablero[2, 1] = 1
tablero[3, 2] = 1
 
# Creamos la figura
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111)
ax.axis('off')
b = tablero
imagen = ax.imshow(b, interpolation="none", cmap=cm.gray_r)
 
 
def animate(i):
    global b
    b = paso(b)
    imagen.set_data(b)
 
 
anim = animation.FuncAnimation(fig, animate, frames=GENERACIONES, blit=True)
anim.save('juego_vida.mp4', fps=10)
