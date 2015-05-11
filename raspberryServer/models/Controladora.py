#!/usr/bin/python

import models

class Controladora :

    def __init__(self) :
		self.lampara = models.Lampara("Lampara")

    def setValue(self, jobj):
		if jobj["name"].lower() == "lampara" :
			self.lampara.setValue(jobj["state"]);
			return self.lampara.getState()
		
		return {}
 
    def getValues(self):
		out = []
		out.append(self.lampara.getState())
 
		return {"devices" : out}
