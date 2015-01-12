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



import random


cadena = ""

tamanio = random.randint(4,8)

for i in range(tamanio):
  if (random.random() > 0.5) :
    cadena += "["
  else:
    cadena += "]"
  
print "La cadena aleatoria es %s" % (cadena)

cuenta = 0;


# Contamos el numero de corchetes abiertos y cerrados. Si en algún momento se han cerrado más que abierto, problema
for i in range(len(cadena)):
  if (cadena[i] == "["):
    cuenta += 1
  else:
    cuenta -= 1

  if (cuenta < 0):
    print "Hay un problema con la cadena en el caracter %d." % (i)
    
    exit()  # Salida guarrilla del programa. No usar en programas de verdad :-)

# Si queda alguno abierto, problema
if (cuenta > 0):
  print "¡Demasiados corchetes abiertos!"
else:
  print "¡La cadena está bien formateada!"
  
  
  