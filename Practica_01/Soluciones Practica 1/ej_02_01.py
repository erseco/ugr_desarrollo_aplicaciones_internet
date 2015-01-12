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

# Puede que te haga falta instalar el paquete python-tk:
# sudo apt-get install python-tk

# Para poder vr el resultado gráfico, si trabajas sobre una máuina virtual
# no olvides hacer un X11 forwarding (parámetro -X)

import time
from funcionesJuegoVida import *

board = cargaFichero('juegoVida.txt')
    
printBoard(board);
pintaTableroGrafico(board);

while True:
  time.sleep(0.3)
  
  iteracion(board);
  
  printBoard(board);
  pintaTableroGrafico(board);
      