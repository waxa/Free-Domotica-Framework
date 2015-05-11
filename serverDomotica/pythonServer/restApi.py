#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import json
import models

controladora = models.Controladora()

urls = (
	'/setValue/', 		'SetValue',
	'/getValues/', 		'GetValues',
	'/pushValues/',		'PushValues',
	'/registro/',		'Registro'
)

print "datos cargados"

app = web.application(urls, globals())

class SetValue :
	def OPTIONS (self) :
		web.header('Access-Control-Allow-Origin','*')
		web.header('Access-Control-Allow-Credentials','true')
		web.header('Access-Control-Allow-Headers','Origin, X-Requested-With, Content-Type, Accept')
		web.header("Access-Control-Allow-Methods","GET,POST,OPTIONS,PUT,DELETE")
	def POST (self) :
		web.header("Content-Type","application/json; charset=utf-8")
		web.header('Access-Control-Allow-Origin',      '*')
		web.header('Access-Control-Allow-Credentials', 'true')
		web.header('Access-Control-Allow-Headers', 
			'Origin, X-Requested-With, Content-Type, Accept')
		web.header("Access-Control-Allow-Methods","GET,POST,OPTIONS,PUT,DELETE")
		jobj = json.loads(web.data())
		dicc = controladora.setValue(jobj)
		print dicc
		return json.dumps(dicc)

class GetValues :
	def GET (self) :
		web.header("Content-Type","application/json; charset=utf-8")
		web.header('Access-Control-Allow-Origin',      '*')
		web.header('Access-Control-Allow-Credentials', 'true')
		web.header('Access-Control-Allow-Headers', 
			'Origin, X-Requested-With, Content-Type, Accept')
		web.header("Access-Control-Allow-Methods", "GET, PUT, POST")
		dicc = controladora.getValues()
		print dicc
		return json.dumps(dicc)

class PushValues :
	def OPTIONS (self) :
		web.header('Access-Control-Allow-Origin','*')
		web.header('Access-Control-Allow-Credentials','true')
		web.header('Access-Control-Allow-Headers','Origin, X-Requested-With, Content-Type, Accept')
		web.header("Access-Control-Allow-Methods","GET,POST,OPTIONS,PUT,DELETE")
	def POST (self) :
		web.header("Content-Type","application/json; charset=utf-8")
		web.header('Access-Control-Allow-Origin',      '*')
		web.header('Access-Control-Allow-Credentials', 'true')
		web.header('Access-Control-Allow-Headers', 
			'Origin, X-Requested-With, Content-Type, Accept')
		web.header("Access-Control-Allow-Methods","GET,POST,OPTIONS,PUT,DELETE")
		controladora.pushValues()

class Registro :
	def OPTIONS (self) :
		web.header('Access-Control-Allow-Origin','*')
		web.header('Access-Control-Allow-Credentials','true')
		web.header('Access-Control-Allow-Headers','Origin, X-Requested-With, Content-Type, Accept')
		web.header("Access-Control-Allow-Methods","GET,POST,OPTIONS,PUT,DELETE")
	def POST (self) :
		web.header("Content-Type","application/json; charset=utf-8")
		web.header('Access-Control-Allow-Origin',      '*')
		web.header('Access-Control-Allow-Credentials', 'true')
		web.header('Access-Control-Allow-Headers', 
			'Origin, X-Requested-With, Content-Type, Accept')
		web.header("Access-Control-Allow-Methods","GET,POST,OPTIONS,PUT,DELETE")
		jobj = json.loads(web.data())
		controladora.setIdPush(jobj)
		return json.dumps({"state" : "ok"})

		
if __name__ == "__main__":
	app.run()
