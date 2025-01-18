import random
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["onlineshop"]
products_collection = db["products"]

def add_network_features_to_electronics():
    """Fügt allen Produkten der Kategorie 'Elektronik' neue Netzwerktechnologie-Eigenschaften hinzu."""
    try:
        # 1. Produkte der Kategorie "Elektronik" finden
        electronics_products = products_collection.find({"category": "Elektronik"})

        if not electronics_products:
            print("Keine Produkte in der Kategorie 'Elektronik' gefunden.")
            return

        # 2. Neue Eigenschaften hinzufügen
        features = ["4G", "5G", "Satellit", "3G", 2, 5.2]

        for product in electronics_products:
            # Wähle zufällige Werte aus den Features aus
            selected_features = random.sample(features, random.randint(1, len(features)))

            # Update mit neuen Eigenschaften
            products_collection.update_one(
                {"_id": product["_id"]},  # Produkt anhand der ID identifizieren
                {"$set": {"properties.Netzwerktechnologie": selected_features}}
            )

        print("Netzwerktechnologie-Eigenschaften erfolgreich hinzugefügt.")
    except Exception as e:
        print("Fehler beim Hinzufügen der Netzwerktechnologie:", e)

# Funktion in die Hauptlogik integrieren
def main():
    add_network_features_to_electronics()

if __name__ == "__main__":
    main()