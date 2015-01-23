#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = "Ernesto Serrano"
__copyright__ = "Copyleft 2007, Ernesto Serrano"
__credits__ = "DAI - Desarrollo de Aplicaciones para Internet"
__company__ = "UGR - Universidad de Granada"
__license__ = "GPL"
__version__ = "0.4c"
__email__ = "erseco@correo.ugr.es"
__status__ = "Production"
__comments_ = """
Twitter API con el sistema de plantillas Mako
"""
import web
from web import form
import dbm
import datetime
import json

import feedparser

import tweepy


from web.contrib.template import render_mako

# Importante, las sesiones no funcionan en debug si no se alamacenan en web.config
web.config.debug = True
urls = (
        '/all', 'all', #mostramos toda la informacion del dbm
        '/twitter', 'twitter',
        '/map', 'map',
        '/pocket', 'pocket',
        '/save', 'save',
        '/read', 'read',
        '/clear', 'clear',
        '/register', 'register',
        '/view', 'view',
        '/edit', 'edit',
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
        form.regexp(r'^.{7,}$', "debe ser mayor de 7") #
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
        subtitle = 'Practica 4'
        page = 'index'
        logged_in = ses._initializer['logged_in']

        feed = feedparser.parse('portada.xml')

        items = feed["items"]

#for item in items:

        # Pasamos todas las variables locales al template
        return render.ejercicio_04(**locals())

class view:
    def GET(self2):

        # Si no está logueado nos vamos al indice
        if ses._initializer['logged_in'] == False:
            raise web.seeother('/index')

        else:

            email = ses._initializer['email']

            db = dbm.open('dbm', 'r')

            values = ''

            for key in db.keys():
                if key.startswith(email + "_"):
                    values = values + ' ' + key + '=' + db[key] + '<br>'

            user = ses._initializer['user']
            site_name = 'DAI - Desarrollo de Aplicaciones para internet'
            author = 'Ernesto Serrano'
            license = '2014 Copyleft'
            subtitle = 'Practica 4'
            page = 'view'
            logged_in = ses._initializer['logged_in']

            # Pasamos todas las variables locales al template
            return render.ejercicio_04(**locals())

class edit:
    def GET(self2):

        # Si no está logueado nos vamos al indice
        if ses._initializer['logged_in'] == False:
            raise web.seeother('/index')

        email = ses._initializer['email']

        form = register_form()

        db = dbm.open('dbm', 'r')


        pocket_data = [1000,1222]


        for key in db.keys():
            keyform = key.replace(email+"_", "")
            if keyform in form.d:
                form[keyform].value = db[key]

        # Hacemos el e-mail de solo lectura
        form['email'].attrs['readonly'] = True

        form['accept_license'].attrs['checked'] = True
        form['accept_license'].value = 'true'






        user = ses._initializer['user']
        site_name = 'DAI - Desarrollo de Aplicaciones para internet'
        author = 'Ernesto Serrano'
        license = '2014 Copyleft'
        subtitle = 'Practica 4'
        page = 'register'
        logged_in = ses._initializer['logged_in']

        return render.ejercicio_04(**locals())

class twitter:
    def GET(self2):


        hashtag = "ugr"

        # Consumer keys and access tokens, used for OAuth
        consumer_key = "_PUT_YOUR_DATA_HERE_"
        consumer_secret = "_PUT_YOUR_DATA_HERE_"
        access_token = "_PUT_YOUR_DATA_HERE_"
        access_token_secret = "_PUT_YOUR_DATA_HERE_"
        # OAuth process, using the keys and tokens
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        # Creation of the actual interface, using authentication
        api = tweepy.API(auth)
        # https://dev.twitter.com/docs/api/1.1/get/search/tweets
        tweets = api.search(q=hashtag, count=20)
        # # Mostramos los campos del objeto Tweet
        # print dir(tweets[0])
        # # Mostramos los campos del objeto author del Tweet
        # print dir(tweets[0].author)
        # # Mostramos el nombre del Autor del Tweet.
        # print tweets[0].author.name


        user = ses._initializer['user']
        site_name = 'DAI - Desarrollo de Aplicaciones para internet'
        author = 'Ernesto Serrano'
        license = '2014 Copyleft'
        subtitle = 'Practica 4'
        page = 'twitter'
        logged_in = ses._initializer['logged_in']

        return render.ejercicio_04(**locals())


class map:
    def GET(self2):


        user = ses._initializer['user']
        site_name = 'DAI - Desarrollo de Aplicaciones para internet'
        author = 'Ernesto Serrano'
        license = '2014 Copyleft'
        subtitle = 'Practica 4'
        page = 'map'
        logged_in = ses._initializer['logged_in']

        return render.ejercicio_04(**locals())

class pocket:
    def GET(self2):

        # # Si no está logueado nos vamos al indice
        # if ses._initializer['logged_in'] == False:
        #     raise web.seeother('/index')

        email = ses._initializer['email']

        form = register_form()

        db = dbm.open('dbm', 'r')


        for key in db.keys():
            keyform = key.replace(email+"_", "")
            if keyform in form.d:
                form[keyform].value = db[key]

        # Hacemos el e-mail de solo lectura
        form['email'].attrs['readonly'] = True

        form['accept_license'].attrs['checked'] = True
        form['accept_license'].value = 'true'


        user = ses._initializer['user']
        site_name = 'DAI - Desarrollo de Aplicaciones para internet'
        author = 'Ernesto Serrano'
        license = '2014 Copyleft'
        subtitle = 'Practica 4'
        page = 'pocket'
        logged_in = ses._initializer['logged_in']

        return render.ejercicio_04(**locals())

    def POST(self2):
        form = register_form()
        if not form.validates():

            site_name = 'DAI - Desarrollo de Aplicaciones para internet'
            author = 'Ernesto Serrano'
            license = '2014 Copyleft'
            subtitle = 'Practica 4'
            page = 'register'
            logged_in = ses._initializer['logged_in']
            user = ses._initializer['user']


            return render.ejercicio_04(**locals())
        else:

            db = dbm.open('dbm', 'c')

            email = form.d.email

            for i in form.d:
                db[email+'_'+i] = str(form.d[i])

            # Chapuzilla para que no se cambie el e-mail (por si se toquetea)
            db[email+'_email'] = email



            # Actualizamos el usaurio
            ses._initializer['user'] = db[email+"_firstname"] + " " + db[email+"_lastname"]

            db.close()

            site_name = 'DAI - Desarrollo de Aplicaciones para internet'
            author = 'Ernesto Serrano'
            license = '2014 Copyleft'
            subtitle = 'Practica 4'
            page = 'registered'
            logged_in = ses._initializer['logged_in']
            firstname = form.d.firstname
            lastname = form.d.lastname
            user = ses._initializer['user']




            return render.ejercicio_04(**locals())
class register:
    def GET(self2):

        form = register_form()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally

        site_name = 'DAI - Desarrollo de Aplicaciones para internet'
        author = 'Ernesto Serrano'
        license = '2014 Copyleft'
        subtitle = 'Practica 4'
        page = 'register'
        logged_in = ses._initializer['logged_in']
        user = ses._initializer['user']


        return render.ejercicio_04(**locals())

    def POST(self2):
        form = register_form()
        if not form.validates():

            site_name = 'DAI - Desarrollo de Aplicaciones para internet'
            author = 'Ernesto Serrano'
            license = '2014 Copyleft'
            subtitle = 'Practica 4'
            page = 'register'
            logged_in = ses._initializer['logged_in']
            user = ses._initializer['user']


            return render.ejercicio_04(**locals())
        else:

            db = dbm.open('dbm', 'c')

            email = form.d.email

            for i in form.d:
                db[email+'_'+i] = str(form.d[i])

            site_name = 'DAI - Desarrollo de Aplicaciones para internet'
            author = 'Ernesto Serrano'
            license = '2014 Copyleft'
            subtitle = 'Practica 4'
            page = 'registered'
            logged_in = ses._initializer['logged_in']
            user = ses._initializer['user']
            firstname = form.d.firstname
            lastname = form.d.lastname


            return render.ejercicio_04(**locals())


class login:
    def GET(self2):

        input = web.input()

        email = input['email']
        password = input['password']

        db = dbm.open('dbm', 'c')

        if not email + "_password" in db.keys():
            raise web.seeother('/index')

        if db[email + "_password"] == password:

            # NOTA: Por alguna extraña razon no funciona ses.user cuando
            # se llama a web.seeother, mejor usar ses._initializer['user']

            # ses.email = email
            # ses.logged_in = True

            ses._initializer['email'] = email
            ses._initializer['user'] = db[email+"_firstname"] + " " + db[email+"_lastname"]
            ses._initializer['logged_in'] = True

            raise web.seeother('/view')

        else:
            raise web.seeother('/index')

class save:
    def GET(self2):

        input = web.input()

        amount = float(input['amount'])

        db = dbm.open('dbm', 'c')

        if not "pocket" in db.keys():
           data = [[29.9, 71.5, 106.4, -20, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4, 54.4]]
        else:
            data = json.loads(db["pocket"])


        data[0].append(amount)


        db["pocket"] = json.dumps(data)

        db.close()


        web.header('Content-Type', 'application/json')
        return data


class read:
    def GET(self2):

        db = dbm.open('dbm', 'c')


        if not "pocket" in db.keys():
           data = json.dumps([[29.9, 71.5, 106.4, -20, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1]])

        else:
            data = db["pocket"]

        web.header('Content-Type', 'application/json')
        return data

class clear:
    def GET(self2):

        db = dbm.open('dbm', 'c')


        if "pocket" in db.keys():
            del db["pocket"]

        db.close()


        return ""


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

        db = dbm.open('dbm', 'c')

        values = ''

        for key in db.keys():
            values = values + ' ' + key + '\t\t=' + db[key] + '\n'


        return values


if __name__ == "__main__":
    app.run()
