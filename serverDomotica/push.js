var gcm = require('node-gcm');

function androidPush (data, title, ids){
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
}

androidPush("push test 2", "node says to waxa", ["APA91bElBpkPMFmBX6kaifE_oPcMCXJu1lyTaW-zQKlHtDJM6PB-LzeAXFojMyYVPJ0g8E5_TmSBwku0W_8i1iKCgGMEMJrQleJtClriWS_O3EQeyQQRVjt5pt68QNNX-3YGgxKU-uBlRUClKci8pr9AQxO1u2ihGA"]);