var app = angular.module('app.factory', ['ngCordova', 'app.ajustes']);

app.factory('GCMRegistrationService', function(SENDER_ID) {
    var pushNotification = window.plugins.pushNotification;
    var isAndroidDevice = function() {
        var platform = device.platform;
        return platform === 'android' || platform === 'Android';
    };

    return {
        registerOnGCM: function() {
            if (isAndroidDevice()) {
                pushNotification.register(function(result) {
                    console.log(result);
                }, function() {
                    alert('Error registering device on GCM ');
                }, {
                    "senderID": 610138117757,
                    "ecb": "onNotificationGCMEvent"
                });
            } else {
                alert('Your device platform is not Android!!!');
            }
        }
    };
});

app.factory('NotificationService', function($http, IP_REGISTRO) {

    var deviceRegistrationId;
    function registerOn3rdPartyServer(registrationId) {
        deviceRegistrationId = registrationId;
   
        $http.post(IP_REGISTRO ,{user: "waxa", regid: deviceRegistrationId})
        .success(function(data){
        	localStorage.setItem('regid', deviceRegistrationId);
        }).error(function(data){
            console.log("err");
        });
    }

    return {
        handleNotification: function(e) {

            switch (e.event) {
                case 'registered':
                    if (e.regid.length > 0)
                        registerOn3rdPartyServer(e.regid);
                    break;
                case 'message':
                    alert(JSON.stringify(e));
                    console.log(JSON.stringify(e));
                    break;
                case 'error':
                    console.log('GCM error = ' + e.msg);
                    break;
                default:
                    console.log('An unknown GCM event has occurred');
                    break;
            }
        }
    };
});