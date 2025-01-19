from pymongo import MongoClient

# Verbindung zur MongoDB herstellen
client = MongoClient("mongodb://localhost:27017/")
db = client["onlineshop"]
products_collection = db["products"]

# Aggregations-Pipeline
pipeline = [
      {
        "$match": {
            "properties.color": "Rot"
        }
      }
]

# Aggregationsabfrage ausführen
results = products_collection.aggregate(pipeline, allowDiskUse=True)

# Ergebnisse ausgeben
for result in results:
    print(result)


