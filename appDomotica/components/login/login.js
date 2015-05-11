var app = angular.module('app.login', ['app.factory']);
  	
app.controller('LoginController', ['ViewNavigation', LoginController]);

app.run(function (ViewNavigation){
	ViewNavigation.atLogin();
});

function LoginController (ViewNavigation) {

	var login = this;

	login.registro = {};

	this.toTest = function (){
		ViewNavigation.toTest();	
	};

	login.log = function (){
		login.registro.regid = localStorage.getItem('regid');
		ViewNavigation.logIn(login.registro);
		login.registro = {};
	};
};