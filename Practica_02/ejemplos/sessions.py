# -*- encoding: utf-8 -*-
import web
web.config.debug = False
urls = (
    "/count", "count",
    "/reset", "reset"
)
app = web.application(urls, locals())
ses = web.session.Session(app,
      web.session.DiskStore('sessions'),
      initializer={'count': 0})

class count:
    def GET(self):
        ses.count += 1
        return "Cuenta: " + str(ses.count)

class reset:
    def GET(self):
        ses.kill()
        return """Sesion reseteada"""

if __name__ == "__main__":
    app.run()