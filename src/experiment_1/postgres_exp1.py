import psycopg2
import random



def connect_to_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="onlineshop",
            user="postgres",
            password="admin"
        )
        return connection
    except Exception as e:
        print("Fehler bei der Verbindung zur Datenbank:", e)
        return None

def add_features_for_electronics(connection):
    try:
        cursor = connection.cursor()

        # 1. Hole alle Produkt-IDs der Kategorie "Elektronik"
        select_query = "SELECT productID FROM Produkte WHERE Kategorie = 'Elektronik'"
        cursor.execute(select_query)
        products = cursor.fetchall()

        if not products:
            print("Keine Produkte in der Kategorie 'Elektronik' gefunden.")
            return

        # 2. Neue Eigenschaften für jedes Produkt in der Tabelle "produteigenschaften" hinzufügen
        insert_query = """
        INSERT INTO Produkteigenschaften (productID, AttributName, AttributWert)
        VALUES (%s, %s, %s)
        """

        for product in products:
            features = ["4G", "5G", "Satellit", "3G"]
            features = random.sample(features, random.randint(1, len(features)))
            feature_name = "Netzwerktechnologie"

            product_id = product[0]  # Extrahiere productID
            for feature in features:
                cursor.execute(insert_query, (product_id, feature_name, feature))

        connection.commit()
        print("Eigenschaften wurden erfolgreich für Produkte der Kategorie 'Elektronik' hinzugefügt.")
    except Exception as e:
        print("Fehler beim Hinzufügen von Eigenschaften:", e)
        connection.rollback()
    finally:
        cursor.close()

    # Hauptfunktion erweitern
def main():
    connection = connect_to_db()
    if not connection:
        return

    try:
        # Füge Eigenschaften für Produkte der Kategorie Elektronik hinzu
        add_features_for_electronics(connection)

    except Exception as e:
        print("Fehler in der Hauptfunktion:", e)
    finally:
        connection.close()
        print("Datenbankverbindung geschlossen.")



if __name__ == "__main__":
    main()
