from mongoengine import ReferenceField, StringField, ListField, IntField, FloatField, EmbeddedDocumentField, EmbeddedDocument, connect
from pymongo import MongoClient
from transformers import pipeline
from pruebas import comentario

client = MongoClient("mongodb+srv://grearte:xS8fu8gVPAz9qGWm@cluster0.dffoict.mongodb.net/?retryWrites=true&w=majority")
db = client['Turismo']
collection_lugares = db['lugar']
collection_turistas = db['turista']

class Comentario(EmbeddedDocument):
    turista_id = ReferenceField('Turista')
    texto = StringField(required=True)

class lugares_for_dao:

    @staticmethod
    def crear_lugar(id, nombre, ubicacion, descripción, horario, comentarios, visitas):
        lugar = {
            "_id" : id,
            "nombre": nombre,
            "ubicacion": ubicacion,
            "descripción": descripción,
            "horario": horario,
            "comentarios": comentarios,
            "visitas": visitas
        }
        collection_lugares.insert_one(lugar)
        print("Lugar creado")

    @staticmethod
    def obtener_Estrellas_Comentarios(comentario):
        #Analizador de los comentarios
        analizador_sentimientos = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
        #comentario = "esta bueno el lugar pero le falta sombra y tachos de basura"
        resultado = analizador_sentimientos(comentario)
        print("El comentario es: ", resultado)

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

    @staticmethod
    def Eliminar_Lugar_por_id(id):
        collection_lugares.delete_one({"_id": id})
        print(f"Lugar con ID {id} eliminado.")

    @staticmethod
    def Obtener_lugar_por_visitas_mayor(visitas):
        for lugar in collection_lugares.find({"visitas": {"$gt": visitas}}):
            print(lugar)

    @staticmethod
    def Obtener_lugar_por_visitas_menor(visitas):
        for lugar in collection_lugares.find({"visitas": {"$lt": visitas}}):
            print(lugar)