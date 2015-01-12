# -*- encoding: utf-8 -*-
import web

urls = (
    '/set', 'CookieSet',
    '/get', 'CookieGet'
)
app = web.application(urls, globals())


# setcookie(name, value, expires="", domain=None, secure=False) 

class CookieSet:
    def GET(self):
        i = web.input(peso='25')
        web.setcookie('peso', i.peso, 3600)
        return "Peso almacenado en la cookie"

class CookieGet:
    def GET(self):
        try: 
             return "Tu peso es: " + web.cookies().peso
        except:
             return "No existe la Cookie."



if __name__ == "__main__":
    app.run()
    