from modelado import turista

class DAO:    
    #Turistas
    def get_users(self, *, id=None, nombre=None, apellido=None, provincia=None, comentario=None):
        
        if id is not None and nombre is None and apellido is None and provincia is None and comentario is None:
            query = turista.single_user_by_id(id=id)
        elif id is not None and nombre is not None:
            query = turista.user_level(id=id, nombre=nombre)
        elif nombre is not None:
            query = turista.user_by_name(nombre=nombre)
        elif apellido is not None:
            query = turista.user_by_lastname(apellido=apellido)
        elif provincia is not None:
            query = turista.user_by_dni(provincia=provincia)
        elif comentario is not None:
            query = turista.user_by_municipality(comentario=comentario)
        else:
            query = turista.all_users()
        return self.connection.execute(query).fetchall() 