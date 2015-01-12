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
Desarrolle una aplicacion web sencilla que nos permita crear una imagen SVG
dinamica (que cambie cada vez que visitemos la pagina) y aleatoria.
Por ejemplo, que cada vez que se visite la pagina dibuje elipses, rectangulos,
etc. de colores y posiciones distintas.
"""

import web
import random

urls = ('/', 'index')
app = web.application(urls, globals())

class index:

    def GET(self):

        web.header('Content-Type', 'image/svg+xml')

        imagen_svg = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
        imagen_svg = imagen_svg + '<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">'
        imagen_svg = imagen_svg + rectangulo()
        imagen_svg = imagen_svg + elipse()
        imagen_svg = imagen_svg + rectangulo()
        imagen_svg = imagen_svg + elipse()
        imagen_svg = imagen_svg + '</svg>'

        return imagen_svg  # El XML del gráfico SVG


def rectangulo():
    """ Dibuja un rectangulo aleatorio (los colores los obtiene mediante una funcion lambda) """

    x = random.randint(0, 500)
    y = random.randint(0, 500)

    widht = random.randint(0, 200)
    height = random.randint(0, 200)

    r = lambda: random.randint(0,255)
    color = '#%02X%02X%02X' % (r(),r(),r())

    return '<rect x="%s" y="%s" width="%s" height="%s" style="fill:%s" />' % (x, y, widht, height, color)


def elipse():
    """ Dibuja una elipse aleatoria (los colores los obtiene mediante una funcion lambda) """

    cx = random.randint(0, 500)
    cy = random.randint(0, 500)

    rx = random.randint(0, 200)
    ry = random.randint(0, 200)

    r = lambda: random.randint(0,255)
    color = '#%02X%02X%02X' % (r(),r(),r())

    color_line = '#%02X%02X%02X' % (r(),r(),r())

    return '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" style="fill:%s;stroke:%s;stroke-width:2" />' % (cx, cy, rx, ry, color, color_line)


if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()
