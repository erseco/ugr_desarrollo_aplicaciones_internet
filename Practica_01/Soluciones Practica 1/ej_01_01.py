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

# Generamos numero aleatorio
numeroAdivinar = random.randint(1, 100)

# Inicialmente el número es desconocido
numero = -1
iteraciones = 0
maxIntentos = 10;

print "Bienvenido al wonderfuloso juego de adivinar un número"


while (numero != numeroAdivinar) and (iteraciones < maxIntentos):
  leido = input("Adivina un número entre 1 y 100 (te quedan %i intentos)... " % (maxIntentos - iteraciones))

  # Casting a entero para poder hacer comparaciones, etc. Peta si el usuario no mete un número, pero no me preocupa
  numero = int(leido)

  if (numero < 1) or (numero > 100):
    print "Tu eres tonto, el número tiene que estar entre 1 y 100."
  elif (numero < numeroAdivinar):
    print "El número buscado es mayor que %i." % (numero)
  elif (numero > numeroAdivinar):
    print "El número buscado el menor que %i." % (numero)
  else:
    print "Felicidades, el número buscado era el %i." % (numeroAdivinar)
    
  iteraciones += 1
    
if (iteraciones == maxIntentos):
  print "Lo siento, no te quedan más intentos. El número buscado era el %i. Y tú eres un poco ceporro por no haberlo adivinado." % (numeroAdivinar)
  
  
   
    
    