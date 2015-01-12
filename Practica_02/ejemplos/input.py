# -*- encoding: utf-8 -*-
import web

urls = (
    '/prog', 'prog'  
)
app = web.application(urls, globals())

class prog:        
    def GET(self):
		entrada = web.input(par1="XXX", par2="YYY")  # Podemos especificar valores por defecto
		parametro1 = entrada.par1   # hola
		parametro2 = entrada.par2   # pepe
		return parametro1 + ' ' + parametro2
		
if __name__ == "__main__":
    app.run()
    