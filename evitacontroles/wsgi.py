# -*- coding: UTF-8 -*-
"""
--------------------------------------------------------------------------------
DAI - Desarrollo de Aplicaciones para Internet
Grado en Ingeniería Informática (UGR)

Proyecto Final: Evita Controles

2015 - Ernesto Serrano <erseco@correo.ugr.es>
--------------------------------------------------------------------------------

WSGI config for evitacontroles project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/

--------------------------------------------------------------------------------
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evitacontroles.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
