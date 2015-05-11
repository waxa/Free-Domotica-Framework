#!/usr/bin/python

import models
import requests
import json

class Controladora :

	def __init__(self) :
		self.url = "http://95.39.206.192:5555/"
		self.idTest = "APA91bElBpkPMFmBX6kaifE_oPcMCXJu1lyTaW-zQKlHtDJM6PB-LzeAXFojMyYVPJ0g8E5_TmSBwku0W_8i1iKCgGMEMJrQleJtClriWS_O3EQeyQQRVjt5pt68QNNX-3YGgxKU-uBlRUClKci8pr9AQxO1u2ihGA"
		self.servKey = "AIzaSyCw_KuynDE61IJpeRYgssTHjZFWxo14RAg"
		self.GCMPushService = models.GCMPush(self.servKey, True)

	def setValue(self, jobj):
		r = requests.post(self.url+"setValue/", data = json.dumps(jobj))

		return json.loads(r.text)

	def setIdPush(self, jobj):
		if jobj["regid"] is not None :
			self.idTest = jobj["regid"]

	def getValues(self):
		r = requests.get(self.url+"getValues/")

		return json.loads(r.text)
	
	def pushValues(self) :
		self.GCMPushService.push([self.idTest], "Free Domotica Framework!", "Un sensor requiere tu atencion!")