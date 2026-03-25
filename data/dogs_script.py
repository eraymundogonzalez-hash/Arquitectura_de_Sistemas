import requests
import os

def descargar_perrito():
    # 1. Crear la carpeta si no existe
    carpeta = "dogs"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        print(f"✅ Carpeta '{carpeta}' creada.")

    # 2. Llamar a la API para obtener el enlace de la foto
    url_api = "https://dog.ceo/api/breeds/image/random"
    
    try:
        respuesta_api = requests.get(url_api)
        respuesta_api.raise_for_status() # Verifica si hubo error en la red
        datos = respuesta_api.json()
        
        if datos["status"] == "success":
            url_imagen = datos["message"]
            # Extraemos el nombre original del archivo de la URL
            nombre_archivo = url_imagen.split("/")[-1]
            ruta_final = os.path.join(carpeta, nombre_archivo)

            # 3. Descargar la imagen real
            imagen_data = requests.get(url_imagen).content
            
            with open(ruta_final, "wb") as archivo:
                archivo.write(imagen_data)
                
            print(f"🐶 ¡Éxito! Perrito descargado en: {ruta_final}")
        else:
            print("❌ La API no respondió con éxito.")

    except Exception as e:
        print(f"💥 Ocurrió un error: {e}")

# Ejecutar la función
if __name__ == "__main__":
    for _ in range(40):  # Descargar 40 perritos
        descargar_perrito()