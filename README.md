Evita Controles
===============

Proyecto final de la asignatura de Desarrollo de Aplicaciones para Internet (DAI) del Grado en Ingeniería Informática de la Universidad de Granada (UGR)

Consiste en un website que geoposiciona en un mapa los controles policiales reportados por los usuarios.

Este proyecto está realizado como prueba de las siguientes tecnologías:

* Django 1.7.1
* Twitter Bootstrap 3.3.1
* Twitter API (tweepy)
* Hightcharts
* Google Maps
* JSON



Instalación:
------------
Para hacerlo funcionar debemos instalar como mínimo la versión 1.7.1 de django y en los repositorios de Ubuntu 14.04 van por la versión 1.6 así que se deberá instalar mediante "pip", los pasos son los siguientes:

Instalamos pip:
`sudo apt-get install python-pip`

Instalamos django:
`sudo pip install django`

El proceso en MACOSX es similar, podemos instalar python-pip mediante:
`sudo easy_install pip`


Tambien se requiere el modulo tweepy, para instalarlo:
`sudo pip install tweepy`

Una vez hecho esto habrá que sincronizar la base de datos mediante:
`python manage.py syncdb`

Y ejecutar el servidor de pruebas:
`python manage.py runserver`