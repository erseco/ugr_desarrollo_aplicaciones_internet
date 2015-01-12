#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#
# DAI - Desarrollo de Aplicaciones para Internet
#
# 2014 Ernesto Serrano <erseco@correo.ugr.es>
#
#-----------------------------------------------

 La Criba de Eratostenes (https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes) 
 es un sencillo algoritmo que permite encontrar to- dos los numeros primos menores de un numero natural dado. 
 Programelo.

'''

import sys # Funciones para usar parametros

def criba(n):

	noprimos = []

    # iteramos desde 2 hasta la raiz cuadrada de n
	# y desde lo que lleva i, hasta n / i
	# esto nos permite obtener todos los multiplos de i
	# y agregarlos a el conjunto noprimos
	for i in range(2, int(n ** .5) + 1):
	    if i not in noprimos:
	        for j in range(i, int(n / i) + 1): noprimos.append(i * j)
	        
	# por ultimo creamos una lista con todos los numeros
	# primos desde 2 hasta n
	primos = [p for p in range(2, n + 1) if p not in noprimos]


	return primos

	return primos

if len(sys.argv) == 1 or not sys.argv[1].isdigit():
	print "Uso: %s <numero>", sys.argv[0] 

else:
	n = int(sys.argv[1])
	print criba(n)

