var app = angular.module('app.login', ['ngMaterial', 'ngNewRouter']);
  	
app.controller('LoginController', ['$router', '$location', '$http', LoginController]);

app.run(function ($location, $http){
  		
	var registro = {};

	//var url = "http://0.0.0.0:3030/registro/"
	var url = "http://pasarela.lab.inf.uva.es:20062/registro/";

	var logearse = function () {
		$http.post(url, registro)
        .success(function(data){
    		console.log("success", data);
    		$location.path('dispositivos');
  		}).error(function(data){
    		console.log("error", data);
  		});
	};

	if (localStorage.getItem('user') &&	localStorage.getItem('pass') && localStorage.getItem('regid')) {
		registro.user = localStorage.getItem('user');
		registro.pass = localStorage.getItem('pass');
		registro.regid = localStorage.getItem('regid');
		logearse();
	}

});

function LoginController ($router, $location, $http) {
	
	var login = this;

	//login.url = "http://0.0.0.0:3030/registro/"
	login.url = "http://pasarela.lab.inf.uva.es:20062/registro/";

	login.registro = {};

	login.log = function (){
		login.registro.regid = localStorage.getItem('regid');
		console.log(login.registro);
		$http.post(login.url, login.registro)
		.success(function(data){
			console.log("success", data);

        	localStorage.setItem('user', login.registro.user);
			localStorage.setItem('pass', login.registro.pass);
      		
      		console.log("usuario guardado")
			login.registro = {};
			$location.path('dispositivos');	
      	}).error(function(data){
        	console.log("error", data);
        	login.registro = {};
      	});
	};
};