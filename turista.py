from mongoengine import Document, StringField, IntField, ReferenceField, EmbeddedDocumentField, EmbeddedDocument
from pymongo import MongoClient
from function.ConexionDB import collection_lugares

client = MongoClient("mongodb+srv://grearte:xS8fu8gVPAz9qGWm@cluster0.dffoict.mongodb.net/?retryWrites=true&w=majority")
db = client['Turismo']
collection_turistas = db['turista']

class Comentario(EmbeddedDocument):
    turista_id = ReferenceField('Turista')
    texto = StringField(required=True)

# DAO para Turista
class turista_for_dao:

    @staticmethod
    def crear_turista(id, nombre, apellido, provincia, comentario):
        turista = {
            "_id": id,
            "nombre": nombre,
            "apellido": apellido,
            "provincia": provincia,
            "comentario": comentario
        }
        collection_turistas.insert_one(turista)

    @staticmethod
    def obtener_todos_los_turistas():
        for turista in collection_turistas.find():
            print(turista)

    @staticmethod
    def eliminar_turista_por_id(id):
        collection_turistas.delete_one({"_id": id})
        print(f"Turista con ID {id} eliminado.")

    @staticmethod
    def obtener_turistas_por_nombre_y_provincia(nombre, provincia):
        for turista in collection_turistas.find({"nombre": nombre, "provincia": provincia}):
            print(turista)


    @staticmethod
    def contar_turistas_por_provincia(provincia):
        count = collection_turistas.count_documents({"provincia": provincia})
        print(f"Total de turistas en {provincia}: {count}")

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