from textblob import TextBlob

# Listas de palabras clave
palabras_buenas = [
    "encantó", "excelente", "fantástico", "maravilloso", "increíble", "bueno", "perfecto", "agradable", "sorprendente", "recomiendo"
]

palabras_malas = [
    "mala", "peor", "terrible", "horrible", "desagradable", "no recomiendo", "queja", "falló", "deficiente", "aburrido"
]

def analizar_comentario(comentario):
    # Convertir el comentario a minúsculas para una comparación insensible a mayúsculas
    
    comentario = comentario.lower()
    
    # Contadores para palabras buenas y malas
    conteo_buenas = sum(1 for palabra in palabras_buenas if palabra in comentario)
    conteo_malas = sum(1 for palabra in palabras_malas if palabra in comentario)

    # Clasificación basada en los conteos
    if conteo_buenas > conteo_malas:
        return "Bueno"
    elif conteo_buenas < conteo_malas:
        return "Malo"
    else:
        return "Normal"

comentarios = [
    "Me encantó el lugar, volveré sin duda!",
    "La atención fue muy mala, no recomiendo este lugar.",
    "Fue una experiencia normal, nada especial."
]

for comentario in comentarios:
    clasificacion = analizar_comentario(comentario)
    print(f"Comentario: '{comentario}' -> Clasificación: {clasificacion}")
