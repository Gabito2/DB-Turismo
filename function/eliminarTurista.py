from ConexionDB import *

collection_turistas.delete_many({"ID": {"$gt": 0}})
print("Turista eliminado")

# collection_lugares.delete_many({"_id": {"$gt": 0}})
# print("Lugar eliminado")

for turistas in collection_turistas.find():
    print(turistas)

# for lugares in collection_lugares.find():
#     print(lugares)