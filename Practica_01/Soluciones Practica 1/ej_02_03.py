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

import sys
import re

line = "sdfFFG S"

# Comprueba si es un apellido inicial
def apellidoInicial(string):
  a = re.compile(r'([A-Za-z]+) ([A-Z])')
  return a.match(string)

# Comprueba si es un email
def email(string):
  a = re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b')
  return a.match(string)

# Comprueba si es un numero de tarjeta visa
def tarjetaCredito(string):
  a = re.compile(r'([0-9]{4}) ([0-9]{4}) ([0-9]{4}) ([0-9]{4})|([0-9]{4})-([0-9]{4})-([0-9]{4})-([0-9]{4})')
  return a.match(string)
  


while True:
  print "\nIntroduce un texto... "
  leido = sys.stdin.readline()
  
  if apellidoInicial(leido):
    print "SI es un Apellido Inicial"
  else:
    print "NO es un Apellido Inicial"

  if email(leido):
    print "SI es un Email"
  else:
    print "NO es un Email"
    
  if tarjetaCredito(leido):
    print "SI es un numero de tarjeta"
  else:
    print "NO es un numero de tarjeta"
    