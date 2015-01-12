import web

# Plantillas en el directorio './plantilas'
plantilla = web.template.render('plantillas/')
        
urls = (
    '/(.*)', 'hola'
)
app = web.application(urls, globals())

class hola:        
    def GET(self, name): 
        return plantilla.inicio(name) # llama a plantillas/inicio.html pasando la variable name

if __name__ == "__main__":
    app.run()	 