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


# Ordenacion burbuja
def burbuja(lista):
  for i in range(len(lista)):
    for h in range(i, len(lista) - 1):
      if (lista[h] > lista[h+1]):
        aux = lista[h]
        lista[h] = lista[h + 1]
        lista[h + 1] = aux


# Ordenacion burbuja con posible salida antes de tiempo
def burbujaMejorada(lista):
  for i in range(len(lista)):
    cambio = False
    for h in range(i, len(lista) - 1):
      if (lista[h] > lista[h+1]):
        aux = lista[h]
        lista[h] = lista[h + 1]
        lista[h + 1] = aux
        cambio = True
        
    if not cambio:
      return

# Ordenacion por reemplazo
def reemplazo(lista):
  for i in range(len(lista) - 1):
    currentPos = i
    
    for h in range(i + 1, len(lista)):
      if (lista[h] < lista[currentPos]):
        currentPos = h
        
    aux = lista[i]
    lista[i] = lista[currentPos]
    lista[currentPos] = aux

def mergeSort(lista):
  listaTrabajo = list(lista)
  
  mergeSort2(lista, 0, len(lista) - 1, listaTrabajo)
  
  
  

def mergeSort2(lista, i1, i2, listaTrabajo):  
  if (i1 == i2):  # Si un solo elemento, volvemos sin mas
    return
  
  medio = (i1 + i2) / 2
  
  mergeSort2(lista, i1, medio, listaTrabajo)  # Ordenamos la primera mitad (llamada recursiva!)
  mergeSort2(lista, medio + 1, i2, listaTrabajo)   # Ordenamos la segunda mitad (llamada recursiva!)
  
  # Las dos mitades están cada una ordenada
  
  punt1 = i1
  punt2 = medio + 1
  puntB = i1

# Mergueamos
  
  while ( (punt1 <= medio) and (punt2 <= i2) ): 
    if (lista[punt1] < lista[punt2]):
      listaTrabajo[puntB] = lista[punt1]
      punt1 += 1
    else:
      listaTrabajo[puntB] = lista[punt2]
      punt2 += 1
      
    puntB += 1
      
  for i in range(punt1, medio + 1):  # Terminamos de copiar los que queden en la primera mitad
    listaTrabajo[puntB] = lista[i]
    puntB += 1
      
  for i in range(punt2, i2 + 1): # Terminamos de copiar los que queden en la segunda mitad
    listaTrabajo[puntB] = lista[i]
    puntB += 1

  for i in range(i1, i2 + 1):  # Copiamos el trozo en la original
    lista[i] = listaTrabajo[i]
    
  

# Genera una lista de numeros aleatorios  
def generaListaAleatoria():
  tamanioLista = 10000;

  lista = []

  for i in range(tamanioLista):
    lista.append(random.randint(0, 10000000));
    
  return lista