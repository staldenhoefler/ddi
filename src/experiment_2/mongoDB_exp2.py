import random
from pymongo import MongoClient

# Verbindung zur MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["onlineshop"]
products_collection = db["products"]

# Kategorien und Mietpreise
categories = ["Streaming", "Fitness", "Software", "Bildung", "Unterhaltung"]
miete_preise = ["9.99", "14.99", "19.99", "29.99", "49.99"]

# Funktion zur Generierung von Abos
def generate_abos(n):
    """Erzeugt n Produkte mit einer monatlichen Miete."""
    abos = []
    for i in range(1, n + 1):
        category = random.choice(categories)
        miete = random.choice(miete_preise)
        abos.append({
            "productID": f"{10000+i}",
            "name": f"{category} Abo {i}",
            "category": "Abo",
            "rent": f"{miete} Fr./Monat",
            "properties": {
                "duration": f"{random.randint(1, 12)} Monate",
                "cancellation_period": f"{random.randint(1, 3)} Monate"
            },
            "reviews": []  # Standardmäßig keine Bewertungen
        })
    return abos

# Abos generieren und in die MongoDB einfügen
def add_abos_to_nosql():
    try:
        abos = generate_abos(50)
        products_collection.insert_many(abos)
        print("50 Abos erfolgreich hinzugefügt.")
    except Exception as e:
        print("Fehler beim Hinzufügen von Abos:", e)

if __name__ == "__main__":
    add_abos_to_nosql()
