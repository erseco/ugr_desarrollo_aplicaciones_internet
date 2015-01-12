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
Averigue el mecanismo de web.py para el analisis y manejo de distintas URLs. 
Cree una nueva aplicacion web en la que distintas clases manejen dis- tintas 
URLs para servir paginas distintas dependiendo de la URL introducida. 
Asimismo, serıa conveniente ser capaces de obtener los parametros de una llamada 
GET. Por ultimo, defina una pagina para el caso en que una URL no este definida 
(error HTTP 404, not found [4]).
"""

import web
        
urls = (
    '/home', 'home', 
    '/page1', 'page1',  
    '/page2', 'page2',  
    '/(.*)', 'error404'  # Expresión regular, clase asociada
)
app = web.application(urls, globals())

class home:        
    # name es el contenido del primer paréntesis    
    def GET(self):    # petición GET
         return 'Estas en la pagina HOME' 

class page1:        
    # name es el contenido del primer paréntesis    
    def GET(self):    # petición GET
         return 'Estas en la pagina 1' 

class page2:        
    # name es el contenido del primer paréntesis    
    def GET(self):    # petición GET
         return 'Estas en la pagina 2'

class error404:        
    # name es el contenido del primer paréntesis    
    def GET(self, error):    # petición GET
         return '<h1>Error 404 - Pagina no encontrada</h1>'

# Para que se ejecute como aplicación independiente 
# con el servidor de web propio
if __name__ == "__main__":
    app.run()	