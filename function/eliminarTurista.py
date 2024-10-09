from database import collection_turistas

collection_turistas.delete_many({"ID": {"$gt": 0}})
print("Turista eliminado")

for turistas in collection_turistas.find():
    print(turistas)