# -*- coding: UTF-8 -*-
"""
--------------------------------------------------------------------------------
DAI - Desarrollo de Aplicaciones para Internet
Grado en Ingeniería Informática (UGR)

Proyecto Final: Evita Controles

2015 - Ernesto Serrano <erseco@correo.ugr.es>
--------------------------------------------------------------------------------

Esta clase obtiene información de twitter

--------------------------------------------------------------------------------
"""

import tweepy
import time
import json

# Consumer keys and access tokens, used for OAuth
consumer_key = "_PUT_YOUR_DATA_HERE_"
consumer_secret = "_PUT_YOUR_DATA_HERE_"
access_token = "_PUT_YOUR_DATA_HERE_"
access_token_secret = "_PUT_YOUR_DATA_HERE_"




# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def get_twits_with_geo(palabra):
	lista = []
	for r in tweepy.Cursor(api.user_timeline).items(200):
		if palabra in r.text:
			fecha = str(r.created_at)
			#if fecha <= time.strftime('%Y-%m-%d'):
			if str(r.geo) != 'None':
				texto = r.text
				coordenadas = str(r.geo).split('[')[1].split(']')[0]
				lat = coordenadas.split(',')[0]
				lon = coordenadas.split(',')[1]
				lista.append({
							"fields":{
							"category":None,
 							"text":texto,
 							"date":fecha,
 							"user":"Bot de dai",
 							"lat":lat,
 							"lng":lon
							},
							"model":"evitacontroles.userpoint",
							"pk":1
					},)
	return json.dumps(lista)
#print(get_twits_with_geo('#evitacontrol'))


