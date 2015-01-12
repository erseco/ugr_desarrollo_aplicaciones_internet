#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#
# DAI - Desarrollo de Aplicaciones para Internet
#
# 2014 Ernesto Serrano <erseco@correo.ugr.es>
#
#-----------------------------------------------

Cree un programa que lea de un fichero de texto un numero entero n y escriba en otro fichero de 
texto el n-esimo numero de la sucesion de Fibonacci (http://es.wikipedia.org/wiki/Sucesi\%C3\%B3n_de_Fibonacci).

'''
# Funcion para calcular el enésimo digito de la sucesión de fibonacci
def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Leemos el fichero
file_in = open("fichero.txt", "rt")
n = file_in.read()

# Comprobamos que lo que tengamos sea un numero
if n.isdigit():
	n = int(n)

	# Creamos el fichero de salida
	file_out = open("salida.txt", "wt")

	# Escribimos el enesimo digito de la sucesión de fibonacci
	file_out.write(str(fibonacci(n)))

	# Cerramos el fichero
	file_out.close()




