from mongoengine import Document, StringField, IntField, connect

# Conexión a MongoDB
connect(db='Turismo', host="mongodb+srv://grearte:xS8fu8gVPAz9qGWm@cluster0.dffoict.mongodb.net/?retryWrites=true&w=majority")

# Definir el documento (equivalente a una tabla en SQL)
class Turista(Document):
    id = IntField(primary_key=True, required=True)
    nombre = StringField(required=True, max_length=50)
    apellido = StringField(required=True, max_length=50)
    provincia = StringField(required=True, max_length=50)
    comentario = StringField(max_length=200)

# DAO para Turista
class TuristaDAO:

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
    def obtener_todos_los_turistas():
        """
        Obtener todos los turistas de la base de datos.
        """
        return Turista.objects()

    @staticmethod
    def obtener_turista_por_id(turista_id):
        """
        Obtener un turista por su ID.
        """
        return Turista.objects(id=turista_id).first()

    @staticmethod
    def obtener_turistas_por_provincia(provincia):
        """
        Obtener todos los turistas de una provincia específica.
        """
        return Turista.objects(provincia=provincia)

    @staticmethod
    def actualizar_turista(turista_id, **kwargs):
        """
        Actualizar los detalles de un turista usando su ID.
        """
        turista = Turista.objects(id=turista_id).first()
        if turista:
            turista.update(**kwargs)
            return turista.reload()
        return None

    @staticmethod
    def eliminar_turista(turista_id):
        """
        Eliminar un turista de la base de datos usando su ID.
        """
        turista = Turista.objects(id=turista_id).first()
        if turista:
            turista.delete()
            return True
        return False

    @staticmethod
    def obtener_todos_los_turistas():
        """
        Obtener todos los turistas de la base de datos.
        """
        return Turista.objects()

