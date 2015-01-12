# -*- coding: UTF-8 -*-
"""
--------------------------------------------------------------------------------
DAI - Desarrollo de Aplicaciones para Internet
Grado en Ingeniería Informática (UGR)

Proyecto Final: Evita Controles

2015 - Ernesto Serrano <erseco@correo.ugr.es>
--------------------------------------------------------------------------------

Definicion de las urls (dispatcher) de nuestro proyecto

--------------------------------------------------------------------------------
"""

from django.conf.urls import patterns, include, url


from .views import HomePageView, \
    MapView, AboutView, ContactView, StatsView, \
    CreditsView, ServerInfoView, RegistrationView, \
    UserPointList, NewUserPoint, ViewUserPoint, EditUserPoint, DeleteUserPoint, \
    GetTwitterPointsJson, GetUserPointsJson

from views import CategoryList, \
    EditCategory, DeleteCategory, CategoryDetail,\
    NewCategory

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', HomePageView.as_view(), name='home'),

    url(r'^map/', MapView.as_view(), name='map'),
    url(r'^about/', AboutView.as_view(), name='about'),
    url(r'^contact/', ContactView.as_view(), name='contact'),

    url(r'^credits/', CreditsView.as_view(), name='credits'),
    url(r'^serverinfo/', ServerInfoView.as_view(), name='serverinfo'),

    url(r'^stats/', StatsView.as_view(), name='stats'),

    url(r'^points_twitter.json', GetTwitterPointsJson.as_view(), name='points_twitter'),
    url(r'^points_users.json', GetUserPointsJson.as_view(), name='points_users'),


)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'home.html'}, name='mysite_login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='mysite_logout'),
    url(r'^registration/', RegistrationView.as_view(), name='registration'),
)


category_urls = patterns('',
    url(r'^Update$', EditCategory.as_view(), name='category_update'),
    url(r'^Delete$', DeleteCategory.as_view(), name='category_delete'),
)

userpoint_urls = patterns('',
    url(r'^Update$', EditUserPoint.as_view(), name='userpoint_update'),
    url(r'^Delete$', DeleteUserPoint.as_view(), name='userpoint_delete'),
)

urlpatterns += patterns('',
    url(r'^categories$', CategoryList.as_view(), name='category_list'),
    url(r'^category/new$', NewCategory.as_view(), name='category_insert'),
    url(r'^category/(?P<pk>[\w-]+)/', include(category_urls)),


    url(r'^userpoints$', UserPointList.as_view(), name='userpoint_list'),
    url(r'^userpoint/new$', NewUserPoint.as_view(), name='userpoint_insert'),
    url(r'^userpoint/(?P<pk>[\w-]+)/', include(userpoint_urls)),

)
