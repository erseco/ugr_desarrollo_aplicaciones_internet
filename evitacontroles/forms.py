# -*- coding: UTF-8 -*-
"""
--------------------------------------------------------------------------------
DAI - Desarrollo de Aplicaciones para Internet
Grado en Ingeniería Informática (UGR)

Proyecto Final: Evita Controles

2015 - Ernesto Serrano <erseco@correo.ugr.es>
--------------------------------------------------------------------------------

Aqui definimos los formularios que van a estar disponibles en nuestra aplicación

--------------------------------------------------------------------------------
"""
from django import forms

from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

from django.core.mail import send_mail


from .models import Category, UserPoint

class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea())
    cc_myself = forms.BooleanField(required=False)


    def send_email(self):

        email = self['email'].value
        subject = self['subject'].value
        message = self['message'].value
        cc_myself = self['cc_myself'].value

        send_mail(subject, message, email, ['erseco@gmail.com'], fail_silently=False)

        if cc_myself:
            send_mail(subject, message, 'info@evitacontroles.es', [email] , fail_silently=False)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class UserPointForm(forms.ModelForm):
    class Meta:
        model = UserPoint
        fields = ('category', 'user',  'lat', 'lng', 'text',)

