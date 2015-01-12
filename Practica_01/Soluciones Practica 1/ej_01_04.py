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




# Leemos de fichero
fich = open('ficheroNumeroEntrada.txt','r')
line = fich.readline()
fich.close()

# Casting de cadena a entero
n = int(line)

fib1 = 1
fib2 = 1


# Calculamos
for i in range(n - 2):
  aux = fib2
  fib2 = fib2 + fib1
  fib1 = aux
    
# Grabamos a fichero
fich = open('ficheroNumeroSalida.txt','w')
fich.write('%d' % (fib2)) 
fich.close() 
   
print "El numero %d de la sucesión de Fibonacci es %d. El resultado se ha grabado en el fichero ficheroNumeroSalida.txt" %(n, fib2)
