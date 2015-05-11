var app = angular.module('app', ['ngNewRouter', 'app.factory', 'app.login', 'app.dispositivos', 'app.test']);

app.run(function (GCMRegistrationService){
    
    var androidConfig = {
        "senderID": "610138117757"
    };

    document.addEventListener("deviceready", function(){
        
        if (localStorage.getItem('regid'))
            console.log("registrado");
        else
            GCMRegistrationService.registerOnGCM();

    }, false);

});

app.controller('AppController', ['$router', AppController]);

function AppController ($router) {

    $router.config([
        { path: '/', redirectTo: '/login' },
        { path: '/login', component: 'login' },
        { path: '/dispositivos', component: 'dispositivos' },
        { path: '/test', component: 'test' }
    ]);

    this.debug = true;

};