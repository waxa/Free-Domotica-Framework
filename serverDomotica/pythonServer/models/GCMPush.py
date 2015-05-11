#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author waxa <waxaman@gmail.com>

import json
import requests

class GCMPush :
	
	#	@param servKey : A serer key from google console
	#	@param verbose : optional param to print info from push request
	def __init__(self, servKey, verbose = False) :
		self.servKey = servKey
		self.url = "https://android.googleapis.com/gcm/send"
		self.header = {"Authorization": "key="+self.servKey, "Content-Type" : "application/json", "Accept-Encoding" : "application/json" }
		self.verbose = verbose
		

	# 	@param regIds : A list with registers ID's from android devices. Must be strings
	#	@param title : A title for you notification, for basic usage on cordova push plugin, don't need on android native
	#	@param message : The text on you notification, for basic usage on cordova push plugin, don't need on android native
	#	@param extras : You can pass extra data (string, json, etc) on this param
	def push(self, regIds, title, message, extras = None) :

		data = { 
			"registration_ids" : regIds,
			"data" : {
				"message" : message,
		    	"title" : title
		    }
		}

		if extras is not None:
			data["data"]["extras"] = extras

		r = requests.post(self.url, data = json.dumps(data), headers = self.header)

		if self.verbose :
			print "-------------------------------"
			print "push info"
			print r.text
			print "-------------------------------"

