Este projecto permitira en algun momento futuro conectar tus dispositivos de domotica a tu movil de una forma transparente

Acualmente en desarrollo en una fase muy temprana.

La parte del código de la aplicación que trata las notificaciones push en angular (sin ionic) esta adaptada del codigo del repositorio https://github.com/marlandy/ionic-cordova-pushnotifications (que si que incluía ionic) 

Actualmente implementandose:
	<ul>
		<li>activar desactivar dispositivos de la rasp</li>
		<li>notificar al telefono cuando un sensor lance un evento</li>
	</ul>

Para iniciar el proyecto :
	<ol>
		<li>Clona el repositorio
			<ul><li>git clone https://github.com/waxa/Free-Domotica-Framework.git</li></ul>
		</li>
		<li>Instala las dependencias de la aplicacion
			<ul>
				<li>cd Free-Domotica-Framework/appDomotica</li>
				<li>bower install</li>
			</ul>
		</li>
		<li>Crea un nuevo proyecto cordova llamado cordovaBuild en la raiz del projecto (en realidad llamalo como quieras, pero asi estaria ya incluido en el gitignore)
			<ul>
				<li>cd Free-Domotica-Framework</li>
				<li>cordova create cordovaBuild --link-to=appDomotica/</li>
			</ul>
		</li>
		<li>Instala los siguientes plugins de cordova
			<ul>
				<li>cordova platform add android --save</li>
				<li>cordova plugin add https://github.com/phonegap-build/PushPlugin.git --save</li>
				<li>cordova plugin add org.apache.cordova.network-information --save</li>
				<li>cordova plugin add https://git-wip-us.apache.org/repos/asf/cordova-plugin-device.git --save</li>
				<li>cordova run</li>
			</ul>
		</li>
	</ol>

Necesitas configurar el archivo appDomotica/app/ajustes.js con tus respectivos datos

Si despues de hacer todo esto la app no funciona prueba a modificar el archivo cordovaBuild/config.xml y añade lo siguiente (con el formato xml):
	<ul>
		<li> \<access origin="\*" \\\></li>
		<li> \<allow-navigation href="\*" \\\></li>
		<li> \<allow-intent href="\*" \\\></li>
	</ul>

Esto ultimo es una burrada, deberia funcionar solo con lo anterior, probarlo solo como ultimo recurso
