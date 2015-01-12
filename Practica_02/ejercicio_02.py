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
Averigue el mecanismo mas habitual que ofrece web.py para servir contenidos 
estaticos tales como imagenes u hojas de estilo. Anada algunas imagenes estaticas 
a su aplicacion y compruebe que el cliente es capaz de acceder a ellas directamente 
a traves de una URL.
Aunque el metodo habitual para servir paginas web de web.py es el uso de templates, 
modifique el ejemplo original del punto anterior para generar en vez de simplemente 
el codigo Hello, World!, generar un fichero HTML correcto en el que se incluya, 
entre los demas elementos necesarios, una pagina de estilo CSS y alguna imagen 
estatica.
"""

import web
        
# Asocia cualquier ruta url con la clase 'hola'
urls = (
    '/(.*)', 'hola'  # Expresión regular, clase asociada
)
app = web.application(urls, globals())

class hola:        
    # name es el contenido del primer paréntesis    
    def GET(self, name):    # petición GET
    #     if not name:  name = 'mundo'
    #     return 'Hola, ' + name + '!'

    	html = '''
        	<html>
        	<head>
	        	<title>Ejercicio 2</title>
	        	<link href="./static/style.css" rel="stylesheet" type="text/css" />
        	</head
        	<body>
        		<h1>Bienvenidos</h2>
        		<img src="./static/black.jpg" />
        		<a href="http://www.google.es">Pulse para buscar</a>

        	</body>
        	'''

    	return html

# Para que se ejecute como aplicación independiente 
# con el servidor de web propio
if __name__ == "__main__":
    app.run()	