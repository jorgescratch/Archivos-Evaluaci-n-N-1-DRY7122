import json
from datetime import datetime, timedelta

ruta_archivo = "/home/devasc/labs/devnet-src/parsing/myfile.json"

try:
	with open(ruta_archivo) as archivo:
		ourjson = json.load(archivo)
		print("archivo JSON cargado correctamente.")

		if "expires_in" in ourjson:
			tiempo_expiracion_segundos = int(ourjson["expires_in"])
			fecha_expiracion = datetime.now() + timedelta(seconds=tiempo_expiracion_segundos)
			tiempo_restante = fecha_expiracion - datetime.now()
			print("Valor del token: ", ourjson.get("access_token"))
			print("Fecha de expiración del token:", fecha_expiracion)
			print("Tiempo restante antes de que caduque el token:", tiempo_restante)
		else:
    			print("La clave 'expires_in' no está presente en el archivo JSON.")
except FileNotFoundError:
	print("El archivo JSON no se encontró en la ruta especificada.")
except json.JSONDecodeError:
	print("Error al decodificar el archivo JSON.")
