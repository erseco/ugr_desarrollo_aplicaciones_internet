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
Ejercicio 04 pero con persistencia mongodb usando el sistema de plantillas Mako
"""
import web
from web import form
from pymongo import MongoClient
import datetime
from web.contrib.template import render_mako
import pprint #para formatear diccionarios

import hashlib #para sacar el hash de la contraseña


# Importante, las sesiones no funcionan en debug si no se alamacenan en web.config
web.config.debug = True
urls = (
        '/all', 'all', #mostramos toda la informacion del dbm
        '/register', 'register',
        '/view', 'view',
        '/edit', 'edit',
        '/login', 'login',
        '/logout', 'logout',
        '/index', 'index',
        '/', 'index'
        )

app = web.application(urls, locals(), autoreload=True)

client = MongoClient('mongodb://localhost:27017/')

# Almacenando en webconfig la sesion podemos usar el modo debug
if web.config.get('_session') is None:
    ses = web.session.Session(
        app,
        web.session.DiskStore('sessions'),
          initializer={
            'logged_in': False,
            'user': '',
            'email': ''
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


register_form = form.Form(
    form.Textbox("firstname",
        form.notnull
    ),
    form.Textbox("lastname",
        form.notnull
    ),
    form.Textbox("email",
        form.notnull,
        form.regexp(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$', 'Debe ser un email')
    ),

    form.Password("password",
        form.notnull,
        form.regexp(r'^.{8,}$', "debe ser mayor de 7") #
        # form.Validator("Debe ser de minimo 7 caracteres", lambda i: len(i) > 7)
    ),
    form.Password("re_password",
        form.notnull
    ),
    form.Checkbox("accept_license",
        form.Validator("Acepta las clausulas", lambda i: i == 'true'),
        value='true'
    ),
    form.Button("submit"),
    validators = [
        form.Validator("Los passwords no coinciden", lambda i: i.password == i.re_password)
    ]

)

class index:
    def GET(self2):

        user = ''
        if ses._initializer['logged_in'] == True:
            user = ses._initializer['user']

        site_name = 'DAI - Desarrollo de Aplicaciones para internet'
        author = 'Ernesto Serrano'
        license = '2014 Copyleft'
        subtitle = 'Practica 3'
        page = 'index'
        logged_in = ses._initializer['logged_in']


        # Pasamos todas las variables locales al template
        return render.ejercicio_04bis(**locals())

class view:
    def GET(self2):

        # Si no está logueado nos vamos al indice
        if ses._initializer['logged_in'] == False:
            raise web.seeother('/index')

        else:

            email = ses._initializer['email']

            db = client['test-database']

            query = db.posts.find_one({"email": email})


            # Con esto mostramos la coleccion de forma bonita
            htmlLines = []
            for textLine in pprint.pformat(query).splitlines():
                htmlLines.append('<br/>%s' % textLine) # or something even nicer
            values = '\n'.join(htmlLines)


            user = ses._initializer['user']
            site_name = 'DAI - Desarrollo de Aplicaciones para internet'
            author = 'Ernesto Serrano'
            license = '2014 Copyleft'
            subtitle = 'Practica 3'
            page = 'view'
            logged_in = ses._initializer['logged_in']

            # Pasamos todas las variables locales al template
            return render.ejercicio_04bis(**locals())

class edit:
    def GET(self2):

        # Si no está logueado nos vamos al indice
        if ses._initializer['logged_in'] == False:
            raise web.seeother('/index')

        email = ses._initializer['email']

        form = register_form()

        db = client['test-database']

        query = db.posts.find_one({"email": email})



        for key in form.d:
            form[key].value = query[key]

        # Hacemos el e-mail de solo lectura
        form['email'].attrs['readonly'] = True

        form['accept_license'].attrs['checked'] = True
        form['accept_license'].value = 'true'


        user = ses._initializer['user']
        site_name = 'DAI - Desarrollo de Aplicaciones para internet'
        author = 'Ernesto Serrano'
        license = '2014 Copyleft'
        subtitle = 'Practica 3'
        page = 'register'
        logged_in = ses._initializer['logged_in']

        return render.ejercicio_04bis(**locals())

    def POST(self2):
        form = register_form()
        if not form.validates():

            site_name = 'DAI - Desarrollo de Aplicaciones para internet'
            author = 'Ernesto Serrano'
            license = '2014 Copyleft'
            subtitle = 'Practica 3'
            page = 'register'
            logged_in = ses._initializer['logged_in']
            user = ses._initializer['user']


            return render.ejercicio_04bis(**locals())
        else:

            email = form.d.email

            db = client['test-database']

            query = db.posts.find_one({"email": email})

            form.d.password  = hashlib.sha1(form.d.password.encode()).hexdigest()

            db.posts.update(
                {'_id':query['_id']},
                {"$set": form.d},
                upsert=False)

            # Chapuzilla para que no se cambie el e-mail (por si se toquetea)
            # db.posts.update(
            #     {'_id':query['_id']},
            #     {"email": email},
            #     upsert=False)


            # Actualizamos el usaurio
            ses._initializer['user'] = form.d.firstname + " " + form.d.lastname

            site_name = 'DAI - Desarrollo de Aplicaciones para internet'
            author = 'Ernesto Serrano'
            license = '2014 Copyleft'
            subtitle = 'Practica 3'
            page = 'registered'
            logged_in = ses._initializer['logged_in']
            firstname = form.d.firstname
            lastname = form.d.lastname
            user = ses._initializer['user']




            return render.ejercicio_04bis(**locals())
class register:
    def GET(self2):

        form = register_form()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally

        site_name = 'DAI - Desarrollo de Aplicaciones para internet'
        author = 'Ernesto Serrano'
        license = '2014 Copyleft'
        subtitle = 'Practica 3'
        page = 'register'
        logged_in = ses._initializer['logged_in']
        user = ses._initializer['user']


        return render.ejercicio_04bis(**locals())

    def POST(self2):
        form = register_form()
        if not form.validates():

            site_name = 'DAI - Desarrollo de Aplicaciones para internet'
            author = 'Ernesto Serrano'
            license = '2014 Copyleft'
            subtitle = 'Practica 3'
            page = 'register'
            logged_in = ses._initializer['logged_in']
            user = ses._initializer['user']


            return render.ejercicio_04bis(**locals())
        else:

            db = client['test-database']

            email = form.d.email

            # Codificamos el sha1 de la contraseña
            password  = hashlib.sha1(form.d.password.encode()).hexdigest()

            # Asignamos el password (si lo hacemos con form.d.password no furula)
            form['password'].value = password

            print form.d.password

            posts = db.posts
            post_id = posts.insert(form.d)

            site_name = 'DAI - Desarrollo de Aplicaciones para internet'
            author = 'Ernesto Serrano'
            license = '2014 Copyleft'
            subtitle = 'Practica 3'
            page = 'registered'
            logged_in = ses._initializer['logged_in']
            user = ses._initializer['user']
            firstname = form.d.firstname
            lastname = form.d.lastname


            return render.ejercicio_04bis(**locals())


class login:
    def GET(self2):

        input = web.input()

        email = input['email']
        password = input['password']

        password = hashlib.sha1(password.encode()).hexdigest()

        db = client['test-database']

        query = db.posts.find_one({"email": email, "password": password})

        if query:

            # NOTA: Por alguna extraña razon no funciona ses.user cuando
            # se llama a web.seeother, mejor usar ses._initializer['user']

            # ses.email = email
            # ses.logged_in = True

            ses._initializer['email'] = email
            ses._initializer['user'] = query['firstname'] + " " + query["lastname"]
            ses._initializer['logged_in'] = True

            raise web.seeother('/view')

        else:
            raise web.seeother('/index')

class logout:
    def GET(self):

        if ses._initializer['logged_in'] == False:
            raise web.seeother('/index')

        ses._initializer['email'] = ''
        ses._initializer['user'] = ''
        ses._initializer['logged_in'] = False

        raise web.seeother('/index')


# Mostramos el contenido completo del dbm para depuración
class all:
    def GET(self):

        db = client['test-database']

        query = db.posts.find()


        values = pprint.pformat(query)

        return values


if __name__ == "__main__":
    app.run()
