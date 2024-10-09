from database import *

print("Turistas:")
for turista in collection_turistas.find():
    print(turista)

print("Lugares:")
for lugares in collection_lugares.find():
    print(lugares)