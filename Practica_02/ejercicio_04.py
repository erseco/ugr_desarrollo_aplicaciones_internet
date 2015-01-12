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
La biblioteca web.py facilita la creacion y manejo de formularios web a traves 
de su sub-biblioteca de formularios [5]. Aprenda a manejarla al menos de manera 
basica mediante la creacion de algun formulario que pregunte cierta informacion 
al usuario y genere contenido dinamico en base al mismo (aunque sea algo sencillo 
como una frase que dependa de la informacion introducida en dicho formulario).
"""

import web
from web import form

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form( 
    form.Textbox("Nombre"), 
    form.Textbox("Edad", 
        form.notnull,
        form.regexp('\d+', 'Debe ser un numero'),
        form.Validator('Debe ser mayor o igual a 18', lambda x:int(x)>=18))
    )

class index: 
    def GET(self): 
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return render.ejercicio_04(form)

    def POST(self): 
        form = myform() 
        if not form.validates(): 
            return render.ejercicio_04(form)
        else:
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
            return "Correcto! El senyor %s tiene %s anyos" % (form.d.Nombre, form["Edad"].value)

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()