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

import copy
from graphics import *

win = None


# Pinta el tablero usando graphics.py
def pintaTableroGrafico(board):
  global win
  
  radioCirculos = 5
  
  if win is None:  # Si la ventana (global) no ha sido creada, la creamos
    win = GraphWin('Juego de la Vida', radioCirculos * len(board) * 2, radioCirculos * len(board[0]) * 2, autoflush=False)
  
  for y in range(1, len(board[0]) - 1):
    for x in range(1, len(board) - 1):
      c = Circle(Point(radioCirculos + x * radioCirculos * 2, radioCirculos + y * radioCirculos * 2), radioCirculos)

      if (board[x][y] == 0):
        c.setFill("white")
      else:
        c.setFill("black")
     
      c.draw(win)
    
  win.update()  # Actualizamos la ventana


# Imprime el tablero
def printBoard(board):
  for y in range(len(board[0])):

    r = ""
    for x in range(len(board)):
      if (board[x][y] == 0):
        r += " "
      else:
        r += "*"
      
    print(r)
    
# Carga el tablero de disco (lo hace 2 mas grande en cada dimension para no tener que hacer calculos especiales en los bordes
def cargaFichero(nombreFichero):
    fich = open(nombreFichero,'r')
    lines = fich.readlines()
    fich.close()

    height = len(lines) + 2
    width = len(lines[0].strip()) + 2

    board = [[0 for x in xrange(height)] for x in xrange(width)]

    for y in range(len(lines)):
      for x in range(len(lines[0].strip())):
        if (lines[y][x] == '0'):
          board[x + 1][y + 1] = 0
        else:
          board[x + 1][y + 1] = 1
    
    return board
  
  
# Ejecuta una iteracion del juevo del a vida 
def iteracion(board):
# Una copia del array para no comernos el coco
  newBoard = copy.deepcopy(board)
  
# Hacemos los calculos desde la fila y columna 1 hasta la tamaño -1 para evitar problemas en los bordes. Previamente el tablero lo hemos hecho mas grande al cargarlo
  for x in range(1, len(board) - 1):
    for y in range(1, len(board[0]) - 1):
      celulasVivasAlrededor = board[x-1][y-1] + board[x][y-1] + board[x+1][y-1] + board[x-1][y] + board[x+1][y] + board[x-1][y+1] + board[x][y+1] + board[x+1][y+1];
      
      # Si celula muerta y tres vecinas, nace
      if (board[x][y] == 0):
        if (celulasVivasAlrededor == 3):
          newBoard[x][y] = 1 # Nace
        else:
          newBoard[x][y] = 0 # Permanece muerta
      
      # Si viva y 2 o 3 vecinas, continua viva, si no, muere
      if (board[x][y] == 1):
        if ((celulasVivasAlrededor == 2) or (celulasVivasAlrededor == 3)):
          newBoard[x][y] = 1 # Se mantiene viva
        else:
          newBoard[x][y] = 0 # Muere
          
# lo copiamos en el tablero original
  for x in range(1, len(board) - 1):
    for y in range(1, len(board[0]) - 1):
      board[x][y] = newBoard[x][y]
