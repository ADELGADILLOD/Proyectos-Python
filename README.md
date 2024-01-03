Se agrega PyFTP.py, el cual es el __mail__ y el archivo PyFTP.exe, el cual es el ejecutable de un solo archivo.
Librerías Propias:
GDC (Google Drive Conect):
	Funciones:
		credentials: Inicia sesión en Google Drive con ayuda de un archivo .json, este se crea atravez de la api de Google, documentación oficial en Google.com.
		list_files_in_folder: Devuleve el listado de todos los archivos de la carpeta dada.
		delete_files_in_folder: Con ayuda del ID de carpeta, eliminará todos los archivos de la carpeta.
		upload_files_from_folder: Carga los archivos de una carpeta local hacia la carpeta de Google Drive dada, los archivos que tengan la extensión dada en una lista ".extensión".
SFTPConect:
	Funciones:
		SFTPC: Conecta con una carpeta SFTP dada con un servidor, usuario y contraseña.
		SFTPD: Descarga los archivos deseados de una carpeta dada hacia una carpeta local.
configtxt:
	Funciones:
		create_confirg: Genera el archivo de configuración.
		config: Si el archivo de configuración no existe, lo genera llamando a la función create_config, después de validar que el archivo de configuración exista, valida el nombre de configuración que se necesita.
		completePath: Entrega una ruta completa dependiendo del sistema operativo donde se esté ejecutando.
Licencias y credenciales, deberán de ser creadas o compartidas en las carpetas dadas en el archivo de configuración.
