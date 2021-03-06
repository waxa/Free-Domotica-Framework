var app = angular.module('app.dispositivos', []);
	
app.controller('DispositivosController', ['$http',DispositivosController]);

function DispositivosController ($http) {

	var dispositivos = this;
	//dispositivos.urlBase = "http://95.39.206.192:5555/";
	//dispositivos.urlBase = "http://192.168.1.9:8080/";
	dispositivos.urlBase = "http://pasarela.lab.inf.uva.es:20062/";

	dispositivos.dispos = [];

	dispositivos.probar = function (){
		if (dispositivos.uno)
			dispositivos.uno = false;
		else
			dispositivos.uno = true;
	}

	dispositivos.get = function (){
		$http.get(dispositivos.urlBase + 'getValues/')
      	.success(function(data){
        	console.log(data.devices);
        	dispositivos.dispos = data.devices;
      	}).error(function(data){
        	console.log("set fallo");
      	});
	};	

	dispositivos.set = function (indice, dispo, estado) {
		$http.post(dispositivos.urlBase + 'setValue/', {
			name : dispo.name,
			state : estado
		}).success(function(data){
        	console.log(data);
        	dispositivos.dispos[indice] = data;
      	}).error(function(data){
        	console.log("set fallo");
      	});
	};

	dispositivos.crearDispo = function (nombre, estado){
		return {
			name : nombre,
			state: estado
		};
	};

	dispositivos.relleno = function() {
		for (var i = 0; i < 10; i++){
			dispositivos.dispos.push(dispositivos.crearDispo("waxa", false));
		}
	};

	dispositivos.get();
	//dispositivos.relleno();
};
