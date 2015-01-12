#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#
# DAI - Desarrollo de Aplicaciones para Internet
#
# 2014 Ernesto Serrano <erseco@correo.ugr.es>
#
#-----------------------------------------------

Realice un programa que cree un fichero de imagen que contenga una representacion del 
Conjunto de Mandelbrot (http://es.wikipedia.org/ wiki/Conjunto_de_Mandelbrot) entre unas 
coordenadas (x1, y1) y (x2, y2) que se le preguntaran al inicio del programa al usuario.

'''
 
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
