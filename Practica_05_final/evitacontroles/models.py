# -*- coding: UTF-8 -*-
"""
--------------------------------------------------------------------------------
DAI - Desarrollo de Aplicaciones para Internet
Grado en Ingeniería Informática (UGR)

Proyecto Final: Evita Controles

2015 - Ernesto Serrano <erseco@correo.ugr.es>
--------------------------------------------------------------------------------

Aquí definimos los modelos de acceso a datos, básicamente Category y UserPoint

--------------------------------------------------------------------------------
"""
from django.db import models
from django.forms import ModelForm

from django.contrib.auth.models import User

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    class Meta:
        verbose_name_plural = 'categories'
    def __unicode__(self):
        return u"%s" % self.name
    @models.permalink
    def get_absolute_url(self):
        return ('category_detail', [self.id])
    @models.permalink
    def get_update_url(self):
        return ('category_update', [self.id])
    @models.permalink
    def get_delete_url(self):
        return ('category_delete', [self.id])

class UserPoint(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    lat = models.FloatField()
    lng = models.FloatField()
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'userpoints'
        ordering = ['date']
    def __unicode__(self):
        return u"%s) %s [lat=%s, lng=%s]" % (self.id, self.text, self.lat, self.lng)
    @models.permalink
    def get_absolute_url(self):
        return ('userpoint_detail', [self.id])
    @models.permalink
    def get_update_url(self):
        return ('userpoint_update', [self.id])
    @models.permalink
    def get_delete_url(self):
        return ('userpoint_delete', [self.id])
