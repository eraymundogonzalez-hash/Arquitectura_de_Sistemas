import requests
import os

def descargar_gatito():
    # 1. Carpeta específica para michis
    carpeta = "cats"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    # 2. URL de TheCatAPI (nos devuelve una lista con un objeto)
    url_api = "https://api.thecatapi.com/v1/images/search"
    
    try:
        respuesta = requests.get(url_api)
        respuesta.raise_for_status()
        datos = respuesta.json()
        
        # La API de gatos devuelve una lista: [{"id":"...", "url":"..."}]
        url_imagen = datos[0]["url"]
        
        # Extraer extensión (jpg, png, gif) y ponerle nombre
        extension = url_imagen.split(".")[-1]
        nombre_archivo = f"gato_{datos[0]['id']}.{extension}"
        ruta_final = os.path.join(carpeta, nombre_archivo)

        # 3. Descarga de la imagen
        imagen_data = requests.get(url_imagen).content
        
        with open(ruta_final, "wb") as archivo:
            archivo.write(imagen_data)
            
        print(f"🐱 ¡Misión cumplida! Michi guardado como: {ruta_final}")

    except Exception as e:
        print(f"😿 Algo salió mal: {e}")

if __name__ == "__main__":
    for _ in range(40):  # Descargar 40 gatitos
        descargar_gatito()