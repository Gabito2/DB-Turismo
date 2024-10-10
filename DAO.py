from modelado import turista

from mongoengine import connect
connect(db='Turismo', host="mongodb+srv://grearte:xS8fu8gVPAz9qGWm@cluster0.dffoict.mongodb.net/?retryWrites=true&w=majority")

class TuristaDAO:

    def __init__(self):
        self.connection = connect(db='Turismo', host="mongodb+srv://grearte:xS8fu8gVPAz9qGWm@cluster0.dffoict.mongodb.net/?retryWrites=true&w=majority")
    
    def hi_test(self):
        print("Hola mundo")

    

    # Obtener turistas según diferentes parámetros
    def get_turistas(self, *, id=None, nombre=None, apellido=None, provincia=None, comentario=None):
        if id is not None and nombre is None and apellido is None and provincia is None and comentario is None:
            query = turista.turista.obtener_turista_por_id(id=id)
        elif id is not None and nombre is not None:
            query = turista.turista.obtener_turistas_por_provincia(provincia=provincia)
        elif nombre is not None:
            query = turista.turista.obtener_turista_por_nombre(nombre=nombre)
        elif apellido is not None:
            query = turista.turista.obtener_turista_por_apellido(apellido=apellido)
        elif comentario is not None:
            query = turista.turista.obtener_turistas_por_comentario(comentario=comentario)
        else:
            query = turista.turista.obtener_todos_los_turistas()
        return self.connection.execute(query).fetchall() 
        
    