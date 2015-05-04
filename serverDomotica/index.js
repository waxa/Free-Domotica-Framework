var express = require('express');
var request = require('request');
var bodyParser = require('body-parser');
var cors = require('cors');
var gcm = require('node-gcm');

var app = express();

app.use(cors());

app.use(bodyParser.urlencoded({
    extended: true
}));

app.use(bodyParser.json());

var datos = null;

var androidPush = function (data, title, ids){
	var message = new gcm.Message();
	
	message.addData({
		message : data,
		badge : 1,
		title : title
	});

	var sender = new gcm.Sender('AIzaSyCw_KuynDE61IJpeRYgssTHjZFWxo14RAg');

	var registrationIds = [];

	for (var i = 0; i < ids.length; i++)
		registrationIds.push(ids[i]);

	console.log("ids: ", registrationIds);
	console.log("message: ", message);

	sender.send(message, registrationIds, function (err, result) {
		if(err) 
			console.error("error",err);
		else    
			console.log("result",result);
	});	
};

app.post('/registro/', function (req, res) {
	datos = req.body;
	console.log(datos);
 	res.send('ok');
});

app.post('/try/', function(req, res) {
	var data = {
		name : "waxa",
		state : true
	};
	androidPush(data, "try push from express", [datos.regid]);
});

 
var server = app.listen(20062, function () {

  var host = server.address().address;
  var port = server.address().port;

  console.log('Listening at http://%s:%s', host, port);

});
