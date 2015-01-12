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

# etree sax parser
from lxml import etree

import urllib2
import sys

# Parseamso el xml
doc = etree.parse('portada.xml')

# Obtenemos la información
search_string = sys.argv[1] if len(sys.argv) > 1 else ""
search = doc.xpath("//title[contains(text(),'%s')]" % search_string) if search_string != "" else ""

n_articulos = doc.xpath('count(//item)')
n_imagenes = doc.xpath("count(//enclosure[@type='image/jpeg'])")
imagenes = doc.xpath("//enclosure[@type='image/jpeg']")

# Imprimimos la informacion
print "Numero de artículos: %s" % (n_articulos);
print "Numero de imágenes: %s" % (n_imagenes); # También podríamos haber usado len(imagenes)
print "Encontrada la cadena: %s veces" % len(search)

# Descargamos las imagenes
for img in imagenes:

	# Extraemos el elemnto url, que es la imagen
	img_url = img.get('url')

	# Extraemos el nombre de la imagen
	file_name = img_url.split('/')[-1]

	# Obtenemos la imagen
	f = urllib2.urlopen(img_url)

	# Creamos el archivo de destino
	local_file = open("images/"+file_name, "wb")
    # Escribimos la imagen en local
	local_file.write(f.read())
	local_file.close()




# ’portada.xml’ es un rss en
# http://ep00.epimg.net/rss/elpais/portada.xml