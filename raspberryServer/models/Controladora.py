#!/usr/bin/python

import models

class Controladora :

    def __init__(self) :
		self.lampara = models.ActuadorRele("Lampara",11)
		self.rele2 = models.ActuadorRele("Rele2",12)
		self.rele3 = models.ActuadorRele("Rele3",15)
		self.rele4 = models.ActuadorRele("Rele4",16)

    def setValue(self, jobj):
		if jobj["name"].lower() == "lampara" :
			self.lampara.setValue(jobj["state"]);
			return self.lampara.getState()
		
		if jobj["name"].lower() == "rele2" :
			self.rele2.setValue(jobj["state"]);
			return self.lampara.getState()
		
		if jobj["name"].lower() == "rele3" :
			self.rele3.setValue(jobj["state"]);
			return self.lampara.getState()
		
		if jobj["name"].lower() == "rele4" :
			self.rele4.setValue(jobj["state"]);
			return self.lampara.getState()
		

		return {}
 
    def getValues(self):
		out = []
		out.append(self.lampara.getState())
		out.append(self.rele2.getState())
		out.append(self.rele3.getState())
		out.append(self.rele4.getState())
 
		return {"devices" : out}
