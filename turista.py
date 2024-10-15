from mongoengine import Document, StringField, IntField, ReferenceField, EmbeddedDocumentField, EmbeddedDocument
from pymongo import MongoClient

client = MongoClient("mongodb+srv://grearte:xS8fu8gVPAz9qGWm@cluster0.dffoict.mongodb.net/?retryWrites=true&w=majority")
db = client['Turismo']
collection_turistas = db['turista']

class Comentario(EmbeddedDocument):
    turista_id = ReferenceField('Turista')
    texto = StringField(required=True)

class Turista():
    id = IntField(primary_key=True, required=True)
    nombre = StringField(required=True, max_length=50)
    apellido = StringField(required=True, max_length=50)
    provincia = StringField(required=True, max_length=50)
    comentario = EmbeddedDocumentField(Comentario)

# DAO para Turista
class turista_for_dao:

    @staticmethod
    def crear_turista(id, nombre, apellido, provincia):
        turista = {
            "_id": id,
            "nombre": nombre,
            "apellido": apellido,
            "provincia": provincia,
            # "comentario": comentario
        }
        collection_turistas.insert_one(turista)

    @staticmethod
    def obtener_todos_los_turistas():
        for turista in collection_turistas.find():
            print(turista)
    
    @staticmethod
    def obtener_turista_por_id(id):
        for turista in collection_turistas.find({"_id": id}):
            print(turista)
    
    @staticmethod
    def obtener_turista_por_nombre(nombre):
        for turista in collection_turistas.find({"nombre": nombre}):
            print(turista)

    @staticmethod
    def obtener_turistas_por_provincia(provincia):
        for turista in collection_turistas.find({"provincia": provincia}):
            print(turista)

    @staticmethod
    def obtener_turista_por_apellido(apellido):
        for turista in collection_turistas.find({"apellido": apellido}):
            print(turista)

    @staticmethod
    def obtener_turistas_por_comentarios(comentarios):
        for turista in collection_turistas.find({"comentario": comentarios}):
            print(turista)
    