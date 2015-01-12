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
El formulario debe preguntar los siguientes datos personales a los usuarios de
la web: nombre, apellidos, DNI, correo electronico, fecha de nacimiento,
direccion, contrasena, verificacion de la contrasena, forma de pago preferida
(contra reembolso o tarjeta VISA), numero de la tarjeta VISA, aceptacion de las
clausulas de proteccion de datos, boton de mandar.
"""

import web
from web import form

templ = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
    form.Textbox("firstname",
        form.notnull
    ),
    form.Textbox("lastname",
        form.notnull
    ),
    form.Textbox("dni",
        form.notnull,
        form.regexp(r'(\d{7})([-]?)([A-Z]{1})', 'Debe ser un DNI valido')
    ),
    form.Textbox("email",
        form.notnull,
        form.regexp(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$', 'Debe ser un email')
    ),
    form.Dropdown("day", [(d, d) for d in range(1, 32)]),
    form.Dropdown("month", [(d, d) for d in range(1, 13)]),
    form.Dropdown("year", [(d, d) for d in range(1900, 2013)]),

    form.Textbox("address",
        form.notnull
    ),

    form.Password("password",
        form.notnull,
        form.regexp(r'^.{7,}$', "debe ser mayor de 7") #
        # form.Validator("Debe ser de minimo 7 caracteres", lambda i: len(i) > 7)
    ),
    form.Password("re_password",
        form.notnull
    ),
    form.Radio('payment_type',
        ['Contrarrembolso', 'Tarjeta VISA', 'Tarjeta de compra del cortingles']
    ),
    form.Textbox("visa_number",
        form.notnull,
        form.regexp(r'^\d{4}([\ \-]?)\d{4}\1\d{4}\1\d{4}$', 'Debe ser un numero de tarjeta valido')
    ),
    form.Checkbox("accept_license",
        form.Validator("Acepta las clausulas", lambda i: i == 'true'),
        value='true'
    ),
    form.Button("submit"),
    validators = [
        form.Validator("Los passwords no coinciden", lambda i: i.password == i.re_password),
        form.Validator("La fecha debe de ser correcta", lambda i: checkDate(i.year, i.month, i.day))
    ]

)

# Cmprobamos si la fecha es correcta haciendo uso de la clase datetime
def checkDate(year, month, day):

    try:
        # OJO! Atencion a la comprobación, que hay que pasar int en lugar de string
        newDate = datetime.datetime(int(year),int(month),int(day))
        return True
    except ValueError:
        return False


class index:
    def GET(self):
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return templ.ejercicio_01(form)

    def POST(self):
        form = myform()
        if not form.validates():
            return templ.ejercicio_01(form)
        else:
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.

            return "Correcto! El senyor %s %s se ha registrado correctamente" % (form.d.firstname, form.d.lastname)

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()