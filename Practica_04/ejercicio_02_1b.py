#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = "Ernesto Serrano"
__copyright__ = "Copyleft 2007, Ernesto Serrano"
__credits__ = "DAI - Desarrollo de Aplicaciones para Internet"
__company__ = "UGR - Universidad de Granada"
__license__ = "GPL"
__version__ = "0.4"
__email__ = "erseco@correo.ugr.es"
__status__ = "Production"
__comments_ = """
Usando el siguiente codigo de ejemplo (basado en etree), se pide que se realice un
pequeño script en Python que lea de disco un feed RSS cualquiera y:

	* Cuente el numero de noticias o contenidos en el fichero RSS.
	* Contabilice el numero de imagenes que contiene.
	* Busque algun termino concreto (que se pueda pasar como parametro al script)
		en los contenidos del RSS.
	* Descargue las imagenes de los feeds a su disco duro (por ejemplo usando
		urllib[6]).
"""

from lxml import etree
import urllib2
import sys

tree = etree.parse('portada.xml')

# Obtenemos la información
search_string = sys.argv[1] if len(sys.argv) > 1 else ""
n_articulos = 0
n_imagenes = 0
search = 0


# Root element
rss = tree.getroot()
# Los elementos funcionan como listas # First child
channel = rss[0]
for e in channel:
	if (e.tag == 'item'):
		n_articulos = n_articulos + 1 # Incrementamos el valor (python no soporta ++)

	for item in e:
	 	if (item.tag == 'enclosure' and item.get('type') == 'image/jpeg'):

			n_imagenes = n_imagenes + 1 # Incrementamos el valor (python no soporta ++)

			# Extraemos el elemnto url, que es la imagen
			img_url = item.get('url')

			# Extraemos el nombre de la imagen
			file_name = img_url.split('/')[-1]

			# Obtenemos la imagen
			f = urllib2.urlopen(img_url)

			# Creamos el archivo de destino
			local_file = open("images/"+file_name, "wb")
		    # Escribimos la imagen en local
			local_file.write(f.read())
			local_file.close()

		elif item.tag == "title" and search_string != "" and search_string in item.text:
			search = search +1


# Imprimimos la informacion
print "Numero de artículos: %s" % (n_articulos);
print "Numero de imágenes: %s" % (n_imagenes);
print "Encontrada la cadena: %s veces" % search



# ’portada.xml’ es un rss en
# http://ep00.epimg.net/rss/elpais/portada.xml
