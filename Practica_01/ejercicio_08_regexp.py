#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""""
#
# DAI - Desarrollo de Aplicaciones para Internet
#
# 2014 Ernesto Serrano <erseco@correo.ugr.es>
#
#-----------------------------------------------

Utilizando expresiones regulares (http://docs.python.org/3.4/library/re.html) realice funciones para:
• Identifique cualquier palabra seguida de un espacio y una unica letra mayuscula (por ejemplo: Apellido N).
• Identifique correos electronicos validos (empiece por una expresion generica y vaya refinandola todo lo posible).
• Identifique numeros de tarjeta de credito cuyos dıgitos esten separados por "-" o espacios en blanco cada paquete 
    de cuatro dıgitos: 1234-5678-9012-3456 o 1234 5678 9012 3456.

"""

import re # Funciones para controlar expresiones regulares


nombre = raw_input("Introduzca una palabra seguida de un espacio y una única letra mayúscula: ")
print "El nombre introducido es " +  ("incorrecto","correcto")[bool(re.match(r"[\w\s]+[A-Z]", nombre))]

email = raw_input("Introduca una direccion de e-mail: ") 
print "El email introducido es " +  ("incorrecto","correcto")[bool(re.match(r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$", email))]

tarjeta = raw_input("Introduca una numero de tarjeta de credito: ")
print "El numero introducido es " +  ("incorrecto","correcto")[bool(re.match(r"^\d{4}([\ \-]?)\d{4}\1\d{4}\1\d{4}$", tarjeta))]