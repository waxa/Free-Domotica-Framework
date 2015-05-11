#!/usr/bin/python

import RPi.GPIO as GPIO

class ActuadorRele :
	
	def __init__(self, name, pin) :
		self.name = name
		self.pin = pin

		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)

		GPIO.setup(self.pin, GPIO.OUT)
		

	def getState(self) :
		aux = {}
		aux["name"] = self.name
		aux["state"] = GPIO.input(self.pin)
		return aux

	def setValue(self, state) :
		if state :
			GPIO.output(self.pin,1)
		else :
			GPIO.output(self.pin,0)
