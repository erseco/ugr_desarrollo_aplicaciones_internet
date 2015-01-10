#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
--------------------------------------------------------------------------------
DAI - Desarrollo de Aplicaciones para Internet
Grado en Ingeniería Informática (UGR)

Proyecto Final: Evita Controles

2015 - Ernesto Serrano <erseco@correo.ugr.es>
--------------------------------------------------------------------------------

Punto de entrada a la aplicacion de django, desde aqui podemos lanzar comandos
para syncroninizar la base de datos o para ejecutar comandos, algunos son:

python manage.py syncdb
python manage.py dbshell
python manage.py runserver

--------------------------------------------------------------------------------
'''
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evitacontroles.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
