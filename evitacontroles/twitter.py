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
# consumer_key = "X0J539IFVSaYatPfyVCFMILkc"
# consumer_secret = "uHGp3DcaTN7lA2ARVQ3s1Q51BYmGcPsp74rE5SLixpiggJjLVQ"
# access_token = "2964281927-N4NZzREUubmuVPsrjnEbtyaXylRBbDvzV7IBdUp"
# access_token_secret = "J3ovNywWwmqvWKCDRsAlUSM1LSjtDW7V90ya4yc4nOcS4"

consumer_key = "AL5MJELgEzz3fEA7RE500PxPv"
consumer_secret = "ZSnGbMFY9Th2bw9s3qTL7YlE91YLH4RpCzECxuodJwnG7dsIvM"
access_token = "2964281927-G4ibTUp1MG0dbqLsQmNo2tWDaac4IC2EHmI8gWO"
access_token_secret = "PLo3w7xmWu7EluNFqZwt2GGVHOY6WMAuGPcdMH8IaOozJ"




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


