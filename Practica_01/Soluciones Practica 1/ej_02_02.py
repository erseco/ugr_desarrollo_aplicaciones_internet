#!/usr/bin/python
# -*- coding: utf-8 -*-

# Practicas de Desarrollo de Aplicaciones para Internet (DAI)
# Copyright (C) 2013 - Zerjillo (zerjioi@ugr.es)
#    
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#   
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#   
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time
from graphics import *

# Función que pinta en una ventana y salva en formato PPM el fractal de Mandelbrot. Nota: iteraciones tiene que ser menor que 1000
def pintaMandelbrot(x1, y1, x2, y2, ancho, iteraciones, nombreFicheroPPM):
  xa = x1
  xb = x2
  ya = y1
  yb = y2
  maxIt = iteraciones
  # image size
  imgx = ancho
  imgy = int(abs (y2 - y1) * ancho / abs(x2 - x1));
  
  win = GraphWin('Mandelbrot', imgx, imgy, autoflush=False)     # Creamos la ventana (desactivamos autoflush para que se redibuje cuando nosotros digamos, no con cada pixel pintado)
  im = Image(Point(0,0), imgx, imgy)           # Creamos una imagen (para poder guardarla luego)
  
  for y in range(imgy):
    zy = y * (yb - ya) / (imgy - 1)  + ya
    
    for x in range(imgx):
      zx = x * (xb - xa) / (imgx - 1)  + xa
      z = zx + zy * 1j
      c = z
      
      for i in range(maxIt):
        if abs(z) > 2.0: break 
        z = z * z + c
        
      i = maxIt - i
      col = color_rgb(i%10*25, i%16*16, i%8*32)
        
      win.plot(x, y, col)   # Pintamos en paralelo en la pantalla y en la imagen
      im.setPixel(x, y, col)
      
    win.update()  #Actualizamos la ventana cada vez que se completa una fila (para hacer mas rapido el calculo, que no se redibuje cada vez que se pinte un pixel)
        
  im.save(nombreFicheroPPM);  # Grabamos en formato PPM
        
        

pintaMandelbrot(-0.7, -0.7, -0.4, -0.4, 400, 255, "fich.ppm");

time.sleep(5)