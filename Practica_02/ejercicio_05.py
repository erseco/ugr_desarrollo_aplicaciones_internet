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
La idea de este ejercicio es crear una aplicacion web dinamica que a partir de
ciertos parametros sea capaz de generar en directo una imagen fractal.
Para esta tarea podemos reutilizar el codigo de los ejercicios de la primera
sesion de practicas (ejercicio sobre el fractal de Mandelbrot)
"""

import web
from web import form

import mandelbrot

import time # Funciones de tiempo

import os # Funciones para comprobar si existen los ficheros

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
    form.Textbox("x1",
        form.notnull,
        form.regexp('^-?[0-9]\d*(\.\d+)?', 'Debe ser un numero'),
        value=-2),
    form.Textbox("y1",
        form.notnull,
        form.regexp('^-?[0-9]\d*(\.\d+)?', 'Debe ser un numero'),
        value=-2),
    form.Textbox("x2",
        form.notnull,
        form.regexp('^-?[0-9]\d*(\.\d+)?', 'Debe ser un numero'),
        value=2),
    form.Textbox("y2",
        form.notnull,
        form.regexp('^-?[0-9]\d*(\.\d+)?', 'Debe ser un numero'),
        value=2),
    form.Textbox("ancho",
        form.notnull,
        form.regexp('\d+', 'Debe ser un numero'),
        value=500),
    form.Textbox("iteracciones",
        form.notnull,
        form.regexp('\d+', 'Debe ser un numero'),
        value=200),
    form.Textbox("color1",
        id="color1",
        value="#123456"),
    form.Textbox("color2",
        id="color2",
        value="#654321")
    )

class index:

    # Variable estática para que al llegar a 10 se lance el borrado de imagenes
    contador_peticiones = 0

    def GET(self):
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return render.ejercicio_05(form)

    def POST(self):
        form = myform()
        if not form.validates():
            return render.ejercicio_05(form)
        else:


            # Limpiamos la cache (solo se hará cada 10 peticiones)
            clean_cache()

            # Obtenemos los valores
            x1 = float(form.d.x1)
            y1 = float(form.d.y1)
            x2 = float(form.d.x2)
            y2 = float(form.d.y2)
            ancho = int(form.d.ancho)
            iteraciones = int(form.d.iteracciones)
            color1 = form.d.color1
            color2 = form.d.color2

            nombreFicheroPNG = 'images/imagen_x1%sy1%sx2%sy2%sancho%scolor1%scolor2%s.png' % (x1, y1, x2, y2, ancho, color1, color2)

            if not os.path.exists(nombreFicheroPNG):
                #mandelbrot.renderizaMandelbrot(x1, y1, x2, y2, ancho, iteraciones, nombreFicheroPNG)

                paleta = (HTMLColorToRGB(color1), HTMLColorToRGB(color2))

                nColoresPaleta = 10
                mandelbrot.renderizaMandelbrotBonito(x1, y1, x2, y2, ancho, iteraciones, nombreFicheroPNG, paleta, nColoresPaleta)


            web.header('Content-Type', 'image/png')
            return open(nombreFicheroPNG, 'rb')  # Datos binarios

def HTMLColorToRGB(colorstring):
    """ convert #RRGGBB to an (R, G, B) tuple """
    colorstring = colorstring.strip()
    if colorstring[0] == '#': colorstring = colorstring[1:]
    if len(colorstring) != 6:
        raise ValueError, "input #%s is not in #RRGGBB format" % colorstring
    r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
    r, g, b = [int(n, 16) for n in (r, g, b)]
    return (r, g, b)

def clean_cache():
    """ Limpia las imagenes antiguas cada 10 peticiones """

    if index.contador_peticiones > 10:
        index.contador_peticiones = 0

        print "limpiando..."

        path = "images"

        now = time.time()

        for f in os.listdir(path):

            f = os.path.join(path, f)

            if os.stat(f).st_mtime < now - 1 * 86400:

                if os.path.isfile(f):

                    os.remove(f)

    else:
        index.contador_peticiones = index.contador_peticiones + 1

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()