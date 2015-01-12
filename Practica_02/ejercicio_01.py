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
En la pagina web oficial de web.py podemos encontrar un ejemplo mini- malista 
(“Hola Mundo”) en el que se utiliza el framework para crear un apli- cacion web 
extremadamente sencilla que saluda al usuario. Copie dicho codigo, ejecutelo, 
compruebe que funciona e intente entender cada parte de dicho pro- grama. 
Es posible que necesite consultar la API o el “Libro de Recetas” de la biblioteca.
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
        if not name:  name = 'mundo'
        return 'Hola, ' + name + '!'

# Para que se ejecute como aplicación independiente 
# con el servidor de web propio
if __name__ == "__main__":
    app.run()	