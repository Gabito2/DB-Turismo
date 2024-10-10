from ConexionDB import *

print("Turistas:")
for turista in collection_turistas.find():
    print(turista)
