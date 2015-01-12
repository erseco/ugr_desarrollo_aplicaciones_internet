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
Ejercicio 01 pero con persistencia dbm
"""

import web
from web import form
import dbm

import datetime

templ = web.template.render('templates/')

urls = (
    '/login', 'login',
    '/view', 'view',
    '/change', 'change',
    '/index', 'index',
    '/', 'index'
    )

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

# Esta es la pagina normal, cuando permitimos registrar usuarios
class index:
    def GET(self):
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return templ.ejercicio_04(form)

    def POST(self):
        form = myform()
        if not form.validates():
            return templ.ejercicio_04(form)
        else:

            input = web.input()

            email = input['email']

            db = dbm.open('dbm', 'c')

            email = form.d.email

            for i in form.d:
                print i
                db[email+'_'+i] = str(form.d[i])

            for key in db.keys():
                print(key)

            return "<html><body>Correcto! El senyor %s %s se ha registrado correctamente <a href='view?email=%s'>ver datos</a></body></html>" % (form.d.firstname, form.d.lastname, form.d.email)

# Esta pagina se llama cuando queremos modificar los datos de un usuario
class change:
    def GET(self):

        input = web.input()

        email = input['email']

        form = myform()

        db = dbm.open('dbm', 'r')


        for key in db.keys():
            keyform = key.replace(email+"_", "")
            form[keyform].value = db[key]

        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return templ.ejercicio_04(form)

    def POST(self):
        form = myform()
        if not form.validates():
            return templ.ejercicio_04(form)
        else:

            db = dbm.open('dbm', 'c')

            email = form.d.email

            for i in form.d:
                print i
                db[email + '_' + i] = str(form.d[i])

            for key in db.keys():
                print(key)

            return "<html><body>Correcto! El senyor %s %s se ha registrado correctamente <a href='view?email=%s'>ver datos</a></body></html>" % (form.d.firstname, form.d.lastname, form.d.email)

# esta clase muestra los datos del usuario
class view:
    def GET(self):

        input = web.input()

        email = input['email']


        db = dbm.open('dbm', 'r')

        values = ''

        for key in db.keys():
            if key.startswith(email + "_"):
                values = values + ' ' + key + '=' + db[key] + '<br>'

        return "<html><body><h1>Valores</h1>%s <br /> <a href='change?email=%s'>cambiar datos</a></body></html>" % (values, email)


class login:
    def GET(self):

        input = web.input()

        email = input['email']
        password = input['password']

        db = dbm.open('dbm', 'r')

        if db[email+"_password"] == password:
            raise web.seeother('/view?email='+email)
        else:
            raise web.seeother('/index')


class logout:
    def GET(self):

        ses._initializer['user'] = ''
        ses._initializer['logged_in'] = 'false'

        raise web.seeother('/index')


if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()