# -*- coding: UTF-8 -*-
"""
--------------------------------------------------------------------------------
DAI - Desarrollo de Aplicaciones para Internet
Grado en Ingeniería Informática (UGR)

Proyecto Final: Evita Controles

2015 - Ernesto Serrano <erseco@correo.ugr.es>
--------------------------------------------------------------------------------

Aquí se definen las diferentes vistas del proyecto

--------------------------------------------------------------------------------
"""

from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import TemplateView, FormView


from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from django.core import serializers


from django.contrib.auth import authenticate, login


from django.views.generic.list import ListView
from models import Category, UserPoint
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from forms import CategoryForm, UserPointForm
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

import json

from .forms import ContactForm

import server_info

import twitter


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {
            'page': 'home',
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)



class AboutView(TemplateView):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        context = {
            'page': 'about',
            'some_dynamic_value': 'This text comes from django view!',
        }
        form_class = ContactForm
        return self.render_to_response(context)




class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '.'

    def post(self, request, *args, **kwargs):

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)

        if form.is_valid():
            # Si los datos son correctos los enviamos por email
            # NOTA: Está desactivado hasta que esté en un servicio online
            # form.send_email()

            # Establecemos una bandera para mostrar la pagina de datos recibidos
            context["sendok"] = True

        return self.render_to_response(context)


    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        #context["sendok"] = True
        #context["testing_out"] = "this is a new context var"
        return context

class RegistrationView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)
        #context["testing_out"] = "this is a new context var"
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        new_user = form.save()

        #Una vez se ha registrado el usuario hacemos login automáticamente
        new_user = authenticate(username=self.request.POST['username'],
                                password=self.request.POST['password1'])

        login(self.request, new_user)


        return HttpResponseRedirect("/")

class CreditsView(FormView):
    template_name = 'credits.html'

    def get(self, request, *args, **kwargs):
        context = {
            'page': 'credits',
            'some_dynamic_value': 'This text comes from django view!',
        }
        form_class = ContactForm
        return self.render_to_response(context)

class ServerInfoView(FormView):
    template_name = 'serverinfo.html'

    def get(self, request, *args, **kwargs):
        context = {
            'page': 'serverinfo',
            'server_info' : server_info.pyinfo(),
        }
        return self.render_to_response(context)


class StatsView(FormView):
    template_name = 'stats.html'

    def get(self, request, *args, **kwargs):
        context = {
            'page': 'stats',
        }
        return self.render_to_response(context)

# Vistas de las categorías

class CategoryMixin(object):
    model = Category
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Category'})

        kwargs.update({'insert_url': 'category_insert'})
        kwargs.update({'object_list': CategoryMixin.model.objects.all})
        return kwargs

    def get_success_url(self):
        return reverse('category_list')


class CategoryFormMixin(CategoryMixin):
    form_class = CategoryForm
    template_name = 'object_form.html'

class CategoryList(CategoryMixin, ListView):
    template_name = 'object_list.html'

class CategoryDetail(CategoryMixin, DetailView):
    pass

class NewCategory(CategoryFormMixin, CreateView):
    pass

class EditCategory(CategoryFormMixin, UpdateView):
    pass

class DeleteCategory(CategoryMixin, DeleteView):
    template_name = 'object_confirm_delete.html'

# Vistas de los UserPoint

class UserPointMixin(object):
    #print object.person.all
    model = UserPoint
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'UserPoint'})
        kwargs.update({'insert_url': 'userpoint_insert'})
        kwargs.update({'object_list':UserPointMixin.model.objects.all})
        return kwargs
    def get_success_url(self):
        return reverse('userpoint_list')

class UserPointFormMixin(UserPointMixin):
    form_class = UserPointForm
    template_name = 'object_form.html'



class UserPointList(UserPointMixin, ListView):
    template_name = 'object_list.html'

class ViewUserPoint(UserPointMixin, DetailView):
    pass

class NewUserPoint(UserPointFormMixin, CreateView):
    pass

class EditUserPoint(UserPointFormMixin, UpdateView):
    pass

class DeleteUserPoint(UserPointMixin, DeleteView):
    template_name = 'object_confirm_delete.html'



class MapView(UserPointFormMixin, CreateView):
    template_name = 'map.html'
    form_class = UserPointForm

    def get_success_url(self):
        return reverse('map')



# Vistas para obtener los JSON de los puntos
class GetTwitterPointsJson(TemplateView):
    def get(self, request, *args, **kwargs):
        dump = twitter.get_twits_with_geo('#evitacontrol')
        return HttpResponse(dump)


class GetUserPointsJson(TemplateView):
    def get(self, request, *args, **kwargs):
        points = serializers.serialize("json", UserPoint.objects.all())
        return HttpResponse(points)
