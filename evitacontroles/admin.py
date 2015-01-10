# -*- encoding: utf-8 -*-
'''
--------------------------------------------------------------------------------
DAI - Desarrollo de Aplicaciones para Internet
Grado en Ingeniería Informática (UGR)

Proyecto Final: Evita Controles

2015 - Ernesto Serrano <erseco@correo.ugr.es>
--------------------------------------------------------------------------------

Aquí definimos que modelos queremos que estén disponibles en la interfaz de
gestion de contenidos automática de django (admin)


--------------------------------------------------------------------------------
'''
from .models import Category, UserPoint

from django.contrib import admin

admin.site.register(Category)
admin.site.register(UserPoint)