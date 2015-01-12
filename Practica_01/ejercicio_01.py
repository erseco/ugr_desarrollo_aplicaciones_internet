#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#-------------------------------------------------------------------------------
#
# DAI - Desarrollo de Aplicaciones para Internet
#
# 2014 Ernesto Serrano <erseco@correo.ugr.es>
#
#-------------------------------------------------------------------------------

Programe un mini-juego de "adivinar" un numero (entre 1 y 100) que el ordenador establezca al azar. 
El usuario puede ir introduciendo numeros y el ordenador le responderia con mensajes del estilo 
"El numero buscado el mayor / menor". 
El programa debe finalizar cuando el usuario adivine el numero (con su correspondiente mensaje de felicitacion) 
o bien cuando el usuario haya realizado 10 intentos incorrectos de adivinacion.

#-------------------------------------------------------------------------------
'''

from random import randint


rnd = randint(1,100)
encontrado = False

for x in xrange(1,10):

	valor = input ("Introduzca un numero del 1 al 100: ")

	if valor == rnd:
		encontrado = True
		print("Valor encontrado")
		break # Salimos de la ejecucin del programa
	elif valor > 100 or valor < 1:
		print "El numero tiene que estar entre el rango [1-100]"
	elif valor > rnd:
		print("El numero es menor que el introducido")
	elif valor < rnd:
		print("El numero es mayor que el introducido")

if not encontrado:
	print("El valor no se ha encontrado tras 10 itentos.")