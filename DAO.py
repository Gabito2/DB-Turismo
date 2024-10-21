from turista import turista_for_dao
from lugaresTuristicos import lugares_for_dao

class TuristaDAO:
    @staticmethod
    def get_turistas(id, nombre, apellido, provincia, comentario):

        if id is not None:
            print(turista_for_dao.obtener_turista_por_id("_id" == id))
        elif nombre is not None:
            print(turista_for_dao.obtener_turista_por_nombre("nombre" == nombre))
        elif apellido is not None:
            print(turista_for_dao.obtener_turistas_por_apellido("apellido" == apellido))
        elif provincia is not None:
            print(turista_for_dao.obtener_turistas_por_provincia("provincia" == provincia))
        elif comentario is not None:
            print(turista_for_dao.obtener_turistas_por_comentario("comentario" == comentario))
        else: 
            print(turista_for_dao.obtener_todos_los_turistas())
    
    @staticmethod
    def get_lugares(id, nombre, ubicacion, descripción, horario, comentarios):
        if id is not None:
            print(lugares_for_dao.obtener_lugar_por_id(id))
        elif nombre is not None:
            print(lugares_for_dao.obtener_lugar_por_nombre(nombre))
        elif ubicacion is not None:
            print(lugares_for_dao.obtener_lugar_por_ubicacion(ubicacion))
        elif descripción is not None:
            print(lugares_for_dao.obtener_lugar_por_descripción(descripción))
        elif horario is not None:
            print(lugares_for_dao.obtener_lugar_por_horario(horario))
        else:
            print(lugares_for_dao.obtener_todos_los_lugares())