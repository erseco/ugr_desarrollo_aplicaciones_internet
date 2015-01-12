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

urls = (
        '/(.*)', 'index'
        )

app = web.application(urls, globals(), autoreload=True)

# input_encoding and output_encoding is important for unicode
# template file. Reference:
# http://www.makotemplates.org/docs/documentation.html#unicode
render = render_mako(
        directories=['templates'],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )

class index:
    def GET(self, name):

        values = {
            'site_name': 'DAI - Desarrollo de Aplicaciones para internet',
            'author': 'Ernesto Serrano',
            'license': '2014 Copyleft',
            'link1': 'Enlace 1',
            'link2': 'Enlace 2',
            'link3': 'Enlace 3',
            'subtitle': 'Practica 3',

        }

        return render.ejercicio_02(**values)
        # Another way:
        # return render.ejercicio_02(**locals())

if __name__ == "__main__":
    app.run()
