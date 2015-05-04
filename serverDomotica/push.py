#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import httplib

url = "https://android.googleapis.com/gcm/send"
header = {"Authorization": "key=AIzaSyCw_KuynDE61IJpeRYgssTHjZFWxo14RAg", "Content-Type" : "application/json", "Accept-Encoding" : "application/json" }

idMovil = []
idMovil.append("APA91bG9BDxU47tcKjsPvn-310oTGO4bhKVnjI2CGLFBFiU_YrrHujkXLooTf2VWROZqLk3V1yv5kuwo6IWCZub4kD6zLTSE-Auijpwu0HXtFy3qD7H9ir7ytKlKzhFQiY3U3VG7v9FJgNNxdGB34vVagYlZOOZWX8CH5gxyGV5yzcEkFG1azks")
# idMovil.append("")
# idMovil.append("APA91bElBpkPMFmBX6kaifE_oPcMCXJu1lyTaW-zQKlHtDJM6PB-LzeAXFojMyYVPJ0g8E5_TmSBwku0W_8i1iKCgGMEMJrQleJtClriWS_O3EQeyQQRVjt5pt68QNNX-3YGgxKU-uBlRUClKci8pr9AQxO1u2ihGA")

data = { 
	"registration_ids" : idMovil,
	"data" : {
		"message" : "funciona?",
		"badge" : 1,
    	"title" : "PERO QUE ES ESTO"
    }
}

r = requests.post(url, data = json.dumps(data), headers = header)
print "-------------------------------"
print "peticion enviada"
print r.text
print "-------------------------------"

