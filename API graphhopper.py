import requests

url = "https://graphhopper.com/api/1/route"

query = {
  "profile": "car",
  "point": ["-18.4783,-70.3126", "-41.4693,-72.9411"],  # Arica to Puerto Montt
  "locale": "en",
  "elevation": "false",
  "instructions": "true",
  "calc_points": "true",
  "points_encoded": "false",  # Set to false to simplify decoding
  "key": "c5facc37-4414-4c70-b339-1848d3b09abb"
}

try:
    response = requests.get(url, params=query)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    
    if "paths" in data and len(data["paths"]) > 0:
        distance = data["paths"][0]["distance"]
        time_in_seconds = data["paths"][0]["time"] / 1000  # Convert from milliseconds to seconds
        
        # Convert time to hours, minutes, and seconds
        hours = int(time_in_seconds // 3600)
        minutes = int((time_in_seconds % 3600) // 60)
        seconds = int(time_in_seconds % 60)
        
        print(f"La distancia entre Arica y Puerto Montt es de {distance} metros.")
        print(f"El tiempo estimado de viaje es de {hours} horas, {minutes} minutos y {seconds} segundos.")
    else:
        print("No se pudo calcular la distancia y el tiempo. Verifique los puntos y parámetros.")
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")
except ValueError:
    print("Error al procesar la respuesta JSON.")
