import qrcode
import matplotlib.pyplot as plt
from function.ConexionDB import *  # Asegúrate de que esto tenga la conexión correcta a MongoDB y la colección 'collection_turistas'
from datetime import datetime

# Información del Lugar
monumento = {
    "Codigo QR": "https://gabito2.github.io/proyectDB.github.io/"
}

# URL de Google Maps
url_google_maps = monumento["Codigo QR"]

# Generar el QR
qr = qrcode.QRCode(
    version=1,  # Tamaño del QR
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
    box_size=10,  # Tamaño de cada caja
    border=4  # Borde alrededor del QR
)
qr.add_data(url_google_maps)  # Añadir URL al QR
qr.make(fit=True)

# Crear imagen del QR
imagen_qr = qr.make_image(fill='black', back_color='white')

# Guardar el QR en un archivo
imagen_qr.save("qr_CristoPortezuelo.png")

# Mostrar el QR usando matplotlib
plt.imshow(imagen_qr)
plt.axis('off')  # No mostrar ejes
plt.show()

print("QR generado, guardado como qr_CristoPortezuelo.png y mostrado en pantalla.")

# Función para obtener el último ID en la colección
def obtener_ultimo_id():
    # Obtener el documento con el ID más alto
    ultimo_turista = collection_turistas.find_one(
        sort=[("ID", -1)]
    )

    # Si no hay documentos, empezar desde 0
    if ultimo_turista is None:
        return 0
    
    return ultimo_turista.get("ID", 0)

# Función para crear un turista anónimo e insertarlo en la base de datos
def crear_turista_anonimo():
    ultimo_id = obtener_ultimo_id()
    nuevo_id = ultimo_id + 1
    
    turista_anonimo = {
        "ID": nuevo_id,
        "Nombre": "Nombre Anonimo",
        "Apellido": "Apellido Anonimo",
        "Provincia": "Provincia Desconocida",
        "Comentario": "Sin Comentario",
        "fecha_hora": datetime.now()
    }
    
    # Insertar el nuevo turista en la base de datos
    collection_turistas.insert_one(turista_anonimo)
    
    print(f"Turista anónimo creado e insertado con ID: {nuevo_id}")

# Llamar a la función para crear y guardar un turista anónimo
crear_turista_anonimo()
