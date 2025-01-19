from pymongo import MongoClient

# Verbindung zur MongoDB herstellen
client = MongoClient("mongodb://localhost:27017/")
db = client["onlineshop"]
orders_collection = db["orders"]
customers_collection = db["customers"]

# Aggregations-Pipeline
pipeline = [
    {
        "$lookup": {
            "from": "customers",  # Name der Customers-Sammlung
            "localField": "customerID",
            "foreignField": "customerID",
            "as": "customerData"
        }
    },
    {
        "$unwind": "$customerData"
    },
    {
        "$addFields": {
            "totalOrderValue": {
                "$sum": {
                    "$map": {
                        "input": "$items",
                        "as": "item",
                        "in": {"$multiply": ["$$item.price", "$$item.quantity"]}
                    }
                }
            }
        }
    },
    {
        "$project": {
            "_id": 0,
            "orderID": 1,
            "customerData.first_name": 1,
            "customerData.last_name": 1,
            "totalOrderValue": 1
        }
    },
    {
        "$sort": {
            "totalOrderValue": -1
        }
    }
]

# Aggregationsabfrage ausführen
results = orders_collection.aggregate(pipeline, allowDiskUse=True)

# Ergebnisse ausgeben
for result in results:
    print(result)
