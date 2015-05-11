#!/usr/bin/python

import RPi.GPIO as GPIO

class Lampara :
	
	def __init__(self, name) :
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(11, GPIO.OUT)
		self.name = name

	def getState(self) :
		aux = {}
		aux["name"] = self.name
		aux["state"] = GPIO.input(11)
		return aux

	def setValue(self, state) :
		if state :
			GPIO.output(11,1)
		else :
			GPIO.output(11,0)
