from mongoengine import Document, StringField, IntField, connect

from pymongo import MongoClient

client = MongoClient("mongodb+srv://grearte:xS8fu8gVPAz9qGWm@cluster0.dffoict.mongodb.net/?retryWrites=true&w=majority")
db = client['Turismo']
collection_turistas = db['turista']

#connect(db='Turismo', host="mongodb+srv://grearte:xS8fu8gVPAz9qGWm@cluster0.dffoict.mongodb.net/?retryWrites=true&w=majority")


# Definir el documento (equivalente a una tabla en SQL)
class Turista(Document):
    id = IntField(primary_key=True, required=True)
    nombre = StringField(required=True, max_length=50)
    apellido = StringField(required=True, max_length=50)
    provincia = StringField(required=True, max_length=50)
    comentario = StringField(max_length=200)

# DAO para Turista
class turista:

    @staticmethod
    def crear_turista(id, nombre, apellido, provincia, comentario=""):
        """
        Crear un nuevo turista en la base de datos.
        """
        turista = Turista(
            id=id,
            nombre=nombre,
            apellido=apellido,
            provincia=provincia,
            comentario=comentario
        )
        turista.save()  # Guardar en la base de datos
        return turista

    @staticmethod
    def obtener_turista_por_nombre(nombre):
        """
        Obtener un turista por su nombre.
        """

        query = db.collection_turistas.find({"nombre": nombre})

        return query

    @staticmethod
    def obtener_turista_por_apellido(apellido):
        """
        Obtener un turista por su apellido.
        """
        return Turista.objects(apellido=apellido)

    @staticmethod
    def obtener_todos_los_turistas():
        """
        Obtener todos los turistas de la base de datos.
        """
        return connect

    @staticmethod
    def obtener_turista_por_id(id):
        """
        Obtener un turista por su ID.
        """
        return Turista.objects(id=id).first()

    @staticmethod
    def obtener_turistas_por_provincia(provincia):
        """
        Obtener todos los turistas de una provincia específica.
        """
        return Turista.objects(provincia=provincia)

    @staticmethod
    def obtener_turistas_por_comentario(comentario):
        """
        Obtener todos los turistas que tienen un comentario particular.
        """
        return Turista.objects(comentario=comentario)

    @staticmethod
    def obtener_todos_los_turistas():
        """
        Obtener todos los turistas de la base de datos.
        """

        query = connect.Turista.find()

        return query

