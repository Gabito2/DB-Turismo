from turista import turista_for_dao
from QR.GenerarQRCristo import obtener_ultimo_id 

class TuristaDAO:

    # @staticmethod
    def get_turistas():

        # if id is not None and nombre is None and apellido is None and provincia is None and comentario is None:
        #     return turista.collection_turistas.find({"_id": id})
        
        # elif id is not None and nombre is not None:
        #     return turista.collection_turistas.find({"nombre": nombre})
        
        # elif id is not None and apellido is not None and nombre is not None:
        #     return turista.collection_turistas.find({"apellido": apellido})
        
        # elif id is not None and apellido is not None and nombre is not None and provincia is not None:
        #     return turista.collection_turistas.find({"provincia": provincia})
        
        # elif id is not None and apellido is not None and nombre is not None and provincia is not None and comentario is not None:
        #     return turista.collection_turistas.find({"comentario": comentario})
        
        # else:
        if id is not None:
            return turista_for_dao.obtener_todos_los_turistas()