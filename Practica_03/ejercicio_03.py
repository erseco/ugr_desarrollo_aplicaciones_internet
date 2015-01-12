#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = "Ernesto Serrano"
__copyright__ = "Copyleft 2007, Ernesto Serrano"
__credits__ = "DAI - Desarrollo de Aplicaciones para Internet"
__company__ = "UGR - Universidad de Granada"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "erseco@correo.ugr.es"
__status__ = "Production"
__comments_ = """
Crear un pequeño sitio usando el sistema de plantillas Mako
"""
import web

from web.contrib.template import render_mako

# Importante, las sesiones no funcionan en debug si no se alamacenan en web.config
web.config.debug = True
urls = (
        '/login', 'login',
        '/logout', 'logout',
        '/index', 'index',
        '/', 'index'
        )

app = web.application(urls, locals(), autoreload=True)

# Almacenando en webconfig la sesion podemos usar el modo debug
if web.config.get('_session') is None:
    ses = web.session.Session(
        app,
        web.session.DiskStore('sessions'),
          initializer={
            'logged_in': 'false',
            'user': '',
            'links': []
          })
    web.config._session = ses
else:
    ses = web.config._session



# input_encoding and output_encoding is important for unicode
# template file. Reference:
# http://www.makotemplates.org/docs/documentation.html#unicode
render = render_mako(
        directories=['templates'],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )

class index:
    def GET(self):

        links = []

        user_data = web.input(page="index")

        if ses._initializer['logged_in'] == 'true':

            links = ses._initializer['links']

            # asi solo tendremos maximo 3 elementos en la lista
            if len(links) > 2:
                links.pop(0)


            links.append(user_data.page)

            ses._initializer['links'] = links

        values = {
            'site_name': 'DAI - Desarrollo de Aplicaciones para internet',
            'author': 'Ernesto Serrano',
            'license': '2014 Copyleft',
            'links': links,
            'page': user_data.page,
            'subtitle': 'Practica 3',
            'logged_in': ses._initializer['logged_in'],
            'user': ses._initializer['user'],

        }

        return render.ejercicio_03(**values)
        # Another way:
        # return render.ejercicio_02(**locals())

class login:
    def GET(self):

        input = web.input()

        user = input['user']
        password = input['password']

        if user == 'ernesto' and password == '1234':

            # NOTA: Por alguna extraña razon no funciona ses.user cuando
            # se llama a web.seeother, mejor usar ses._initializer['user']

            # ses.user = user
            # ses.logged_in = 'true'

            ses._initializer['user'] = user
            ses._initializer['logged_in'] = 'true'

        raise web.seeother('/index')

class logout:
    def GET(self):

        ses._initializer['user'] = ''
        ses._initializer['logged_in'] = 'false'

        raise web.seeother('/index')


if __name__ == "__main__":
    app.run()
