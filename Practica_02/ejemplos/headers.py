# -*- encoding: utf-8 -*-
import web

urls = (
    '/texto', 'manda_texto',
    '/png', 'manda_imagen_png',
    '/svg', 'manda_imagen_svg'
)
app = web.application(urls, globals())

class manda_texto:
	def GET(self):      # tipo / subtipo
		web.header('Content-Type', 'text/plain; charset=iso-8859-1')
		return "Pepe"

class manda_imagen_png:
	def GET(self):
		web.header('Content-Type', 'image/png')
		return imagen_png  # Datos binarios
		
class manda_imagen_svg:
	def GET(self):
		web.header('Content-Type', 'image/svg+xml')

		imagen_svg = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
						<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">
						    <rect x="50" y="50" width="150" height="50" style="fill:#ff0000" />
						</svg>'''
		return imagen_svg  # El XML del gráfico SVG


if __name__ == "__main__":
    app.run()
    