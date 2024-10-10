import conexionDB 
from modelado import turista
print("DAOturista")

#get turistas por id
turista_DAO = turista()
datos = turista_DAO.get_turista_by_id(1)
print(f"Turista: {datos}")


