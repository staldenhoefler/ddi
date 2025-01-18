import psycopg2
import random

# Verbindung zur PostgreSQL-Datenbank
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
            "productID": 10000 + i,
            "name": f"{category} Abo {i}",
            "category": "Abo",
            "rent": miete,
            "duration": f"{random.randint(1, 12)} Monate",
            "cancellation_period": f"{random.randint(1, 3)} Monate"
        })
    return abos

# Abos in die PostgreSQL-Datenbank einfügen
def add_abos_to_sql(connection):
    try:
        cursor = connection.cursor()

        # Überprüfen, ob die Spalte "Miete" existiert, und hinzufügen, falls nicht vorhanden
        cursor.execute("""
        ALTER TABLE Produkte
        ADD COLUMN IF NOT EXISTS Miete VARCHAR(20);
        """)

        # Generiere die Abo-Daten
        abos = generate_abos(50)

        # Einfügen der Abo-Daten
        insert_query = """
        INSERT INTO Produkte (productID, Name, Kategorie, Preis, Miete)
        VALUES (%s, %s, %s, NULL, %s);
        """

        for abo in abos:
            cursor.execute(insert_query, (
                abo["productID"],
                abo["name"],
                abo["category"],
                abo["rent"]
            ))
            cursor.execute("""
            INSERT INTO Produkteigenschaften (productID, AttributName, AttributWert)
            VALUES (%s, %s, %s);
            """, (
                abo["productID"],
                "duration",
                abo["duration"]
            ))
            cursor.execute("""
            INSERT INTO Produkteigenschaften (productID, AttributName, AttributWert)
            VALUES (%s, %s, %s);
            """, (
                abo["productID"],
                "cancellation_period",
                abo["cancellation_period"]
            ))

        connection.commit()
        print("50 Abos erfolgreich hinzugefügt.")
    except Exception as e:
        print("Fehler beim Hinzufügen von Abos:", e)
        connection.rollback()
    finally:
        cursor.close()

if __name__ == "__main__":
    connection = connect_to_db()
    if connection:
        add_abos_to_sql(connection)
        connection.close()
