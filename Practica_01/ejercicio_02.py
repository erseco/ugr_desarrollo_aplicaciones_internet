#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#
# DAI - Desarrollo de Aplicaciones para Internet
#
# 2014 Ernesto Serrano <erseco@correo.ugr.es>
#
#-----------------------------------------------

Programe un par de funciones de ordenacion de matrices de numeros distintas (burbuja, seleccion,
insercion, mezcla, monticulos..) http://es. wikipedia.org/wiki/Algoritmo_de_ordenamiento.
Realice un programa que genere aleatoriamente matrices de numeros aleatorios y use dicho metodos
para comparar el tiempo que tardan en ejecutarse.

'''

import random # Librería de numeros aleatorios
import time

def burbuja(matriz):
    not_complete = True
    while not_complete:
        not_complete = False
        for val, item in enumerate(matriz):
            if val == len(matriz)-1: val = 0
            else:
                if matriz[val] > matriz[val+1]:
                    matriz[val], matriz[val+1] = matriz[val+1], matriz[val]
                    not_complete = True
    return matriz

def seleccion(matriz):
	for i in range(len(matriz)):
	    mini = min(matriz[i:]) #find minimum element
	    min_index = matriz[i:].index(mini) #find index of minimum element
	    matriz[i + min_index] = matriz[i] #replace element at min_index with first element
	    matriz[i] = mini                  #replace first element with min element

	return matriz

# Generamos un vector de enteros de tamaño 100
lista = [int(1000*random.random()) for i in xrange(100)]


# Mostramos los resultados
print lista


inicio = time.time()
print burbuja(lista[:])
fin = time.time()
print "Ha tardado: " + str(fin - inicio)


inicio = time.time()
print seleccion(lista[:])
fin = time.time()
print "Ha tardado: " + str(fin - inicio)
