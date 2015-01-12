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
    

# Importamos las funciones
from ordenacion import *
import time

lista1 = generaListaAleatoria()
lista2 = list(lista1)
lista3 = list(lista1)
lista4 = list(lista1)


#print lista1

start = time.clock()
burbuja(lista1)
end = time.clock()

#print lista1

print "El método de burbuja ha tardado %f segundos" %(end - start)

start = time.clock()
burbujaMejorada(lista2)
end = time.clock()

# print lista2

print "El método de burbuja mejorada ha tardado %f segundos" %(end - start)

start = time.clock()
reemplazo(lista3)
end = time.clock()

#print lista3

print "El método de reemplazo ha tardado %f segundos" %(end - start)

start = time.clock()
mergeSort(lista4)
end = time.clock()

#print lista4

print "El método de mergeSort ha tardado %f segundos" %(end - start)