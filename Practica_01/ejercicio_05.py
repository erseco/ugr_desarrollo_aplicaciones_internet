#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#
# DAI - Desarrollo de Aplicaciones para Internet
#
# 2014 Ernesto Serrano <erseco@correo.ugr.es>
#
#-----------------------------------------------

Cree un programa que:

Genere aleatoriamente una cadena de [ y ].
Compruebe mediante una funcion si dicha secuencia esta balanceada, es decir, que se componga 
de parejas de corchetes de apertura y cierre correctamente anidados. 

Por ejemplo:
• [] → Correcto
• [[][[]]] → Correcto • [][] → Correcto
• ][ → Incorrecto
• [[][[ → Incorrecto • []][[] → Incorrecto

'''
import string
import random

# Funcion para generar una lista aleatoria de caracteres
def generador(size, chars):
	return ''.join(random.choice(chars) for _ in range(size))

# Funcion padra comprbar si está balanceada
def esta_balanceada(cadena):

	cuenta = 0

	# Contamos el numero de corchetes abiertos y cerrados.
	for el in cadena:
	  if el == "[":
	    cuenta += 1
	  else:
	    cuenta -= 1

	  if (cuenta < 0):
	    resultado = False
	    break;

	# Si queda alguno abierto, problema
	if (cuenta > 0):
		resultado = False
	else:
	  	resultado = True
  
	return "Balanceada: " + str(resultado)


# Generamos una cadena de [] de tamaño 100
cadena = generador(8, "[]")

# Imprimimos los resultados
print cadena
print esta_balanceada(cadena)


