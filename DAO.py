from turista import turista_for_dao
from lugaresTuristicos import lugares_for_dao

class TuristaDAO:
    @staticmethod
    def get_turistas(id, nombre, apellido, provincia, comentario):

        if id is not None and nombre is None and apellido is None and provincia is None and comentario is None:
            turista_for_dao.obtener_turista_por_id("_id" == id)
        elif id is not None and nombre is not None and apellido is None and provincia is None and comentario is None:
            turista_for_dao.obtener_turista_por_nombre("nombre" == nombre)
        elif id is not None and nombre is not None and apellido is not None and provincia is None and comentario is None:
            turista_for_dao.obtener_turistas_por_apellido("apellido" == apellido)
        elif id is not None and nombre is not None and apellido is not None and provincia is not None and comentario is not None:
            turista_for_dao.obtener_turistas_por_provincia("provincia" == provincia)
        elif id is not None and nombre is not None and apellido is not None and provincia is not None and comentario is not None:
            turista_for_dao.obtener_turistas_por_comentario("comentario" )
        else: 
            turista_for_dao.obtener_todos_los_turistas()
    
    @staticmethod
    def get_lugares(id, nombre, ubicacion, descripción, horario, comentarios):
        if id is not None and nombre is None and ubicacion is None and descripción is None and horario is None and comentarios is None:
            lugares_for_dao.obtener_lugar_por_id(id)
        elif id is not None and nombre is not None and ubicacion is None and descripción is None and horario is None and comentarios is None:
            lugares_for_dao.obtener_lugar_por_nombre(nombre)
        elif id is not None and nombre is not None and ubicacion is not None and descripción is None and horario is None and comentarios is None:
            lugares_for_dao.obtener_lugar_por_ubicacion(ubicacion)
        elif id is not None and nombre is not None and ubicacion is not None and descripción is not None and horario is None and comentarios is None:
            lugares_for_dao.obtener_lugar_por_descripción(descripción)
        elif id is not None and nombre is not None and ubicacion is not None and descripción is not None and horario is not None and comentarios is None:
            lugares_for_dao.obtener_lugar_por_horario(horario)
        else: 
            lugares_for_dao.obtener_todos_los_lugares()