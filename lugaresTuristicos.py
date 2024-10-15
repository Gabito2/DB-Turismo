from mongoengine import ReferenceField, StringField, ListField, IntField, FloatField, EmbeddedDocumentField, EmbeddedDocument, connect
from pymongo import MongoClient
from turista import Turista


#URL de MongoDB
client = MongoClient("mongodb+srv://grearte:xS8fu8gVPAz9qGWm@cluster0.dffoict.mongodb.net/?retryWrites=true&w=majority")
#Seleccionar la db
db = client['Turismo']
#Seleccionar la colección
collection_lugares = db['lugar']
collection_turistas = db['turista']


class Comentario(EmbeddedDocument):
    turista_id = ReferenceField('Turista')
    texto = StringField(required=True)

class Lugares():
    id = IntField(primary_key=True, required=True)
    nombre = StringField(required=True, max_length=100)
    ubicacion = StringField(required=True , max_length=100) 
    # descripción = StringField(required=True, max_length=500)
    # horario = StringField(required=True, max_length=500) 
    comentarios = ListField(EmbeddedDocumentField(Comentario))

class lugares_for_dao:

    @staticmethod
    def crear_lugar(id, nombre, ubicacion, descripción, horario, comentarios):
        lugar = {
            "_id" : id,
            "nombre": nombre,
            "ubicacion": ubicacion,
            "descripción": descripción,
            "horario": horario,
            "comentarios": comentarios
        }
        collection_lugares.insert_one(lugar)
        print("Lugar creado")
    
    @staticmethod
    def obtener_todos_los_lugares():
        for lugares in collection_lugares.find():
            print(lugares)
    
    @staticmethod
    def obtener_lugar_por_id(id):
        for lugar in collection_lugares.find({"_id": id}):
            print(lugar)
    
    @staticmethod
    def obtener_lugar_por_nombre(nombre):
        for lugar in collection_lugares.find({"nombre": nombre}):
            print(lugar)

    @staticmethod
    def obtener_lugar_por_ubicacion(ubicacion):
        for lugar in collection_lugares.find({"ubicacion": ubicacion}):
            print(lugar)

    @staticmethod
    def obtener_lugar_por_descripción(descripción):
        for lugar in collection_lugares.find({"descripción": descripción}):
            print(lugar)
    
    @staticmethod
    def obtener_lugar_por_horario(horario):
        for lugar in collection_lugares.find({"horario": horario}):
            print(lugar)
    
    @staticmethod
    def obtener_lugar_por_visitas(visitas):
        for lugar in collection_lugares.find({"visitas": visitas}):
            print(lugar)


