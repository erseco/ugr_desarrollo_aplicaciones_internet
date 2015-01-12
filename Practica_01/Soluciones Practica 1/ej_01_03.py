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


print "Bienvenido al programa de la criba de Eratóstenes."

limite = input("Introduce hasta que número quieres calcular los primos: ")

l = range(limite)


for i in range(2, limite):
  if l[i] != -1:   # Si no esta marcado es primo
    print i
    
  for h in range(i, limite, i):
    l[h] = -1 # Marcamos los múltiplos de i
    
print "Ahi lo llevas :-P"


