from database import *
from datetime import datetime

turista = {
    "ID": 1,
    "Nombre": "Nombre Anonimo", 
    "Apellido": "Apellido Anonimo",
    "Comentario": "Sin Comentario",
    "fecha_hora": datetime.now()
}

lugar = {
    "ID": 4,
    "Nombre": "Lugar Anonimo",
    "Comentario": "Sin Comentario"
}

collection_turistas.insert_one(turista)
collection_lugares.insert_one(lugar)
print("Turista agregado")

