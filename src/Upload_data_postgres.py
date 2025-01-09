import psycopg2
import json

# Verbindung zur PostgreSQL-Datenbank herstellen
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


# Daten in die Tabelle einfügen
def insert_data(cursor, table_name, data):
    keys = data.keys()
    columns = ', '.join(keys)
    values = ', '.join([f"%({k})s" for k in keys])
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    cursor.execute(query, data)

# JSON-Daten laden und in die richtige Struktur bringen
def process_json_data(json_file, table_name):
    with open(json_file, 'r', encoding='utf-8') as file:
        raw_data = json.load(file)

    processed_data = []

    if table_name == "Kunden":
        for item in raw_data:
            processed_data.append({
                "customerID": item["customerID"],
                "Vorname": item["first_name"],
                "Nachname": item["last_name"],
                "Geburtsdatum": item["date_of_birth"],
                "Email": item["email"]
            })
    elif table_name == "Produkte":
        for item in raw_data:
            processed_data.append({
                "productID": item["productID"],
                "Name": item["name"],
                "Kategorie": item["category"],
                "Preis": item["price"]
            })
    elif table_name == "Produkteigenschaften":
        for product in raw_data:
            product_id = product["productID"]
            properties = product.get("properties", {})
            for key, value in properties.items():
                processed_data.append({
                    "productID": product_id,
                    "AttributName": key,
                    "AttributWert": value
                })
    elif table_name == "Bewertungen":
        for item in raw_data:
            product_id = item["productID"]
            for review in item.get("reviews", []):
                rewiew_id = str(review["reviewID"])
                processed_data.append({
                    "productID": product_id,
                    "reviewID": rewiew_id,
                    "customerID": review["customerID"],
                    "Sterne": review["stars"],
                    "Text": review["text"],
                    "Datum": review["date"]
                })
    elif table_name == "Bestellungen":
        for item in raw_data:
            order_id = int(item["orderID"])
            processed_data.append({
                "orderID": order_id,
                "customerID": item["customerID"],
                "Datum": item["orderDate"],
                "Gesamtpreis": item["totalPrice"]
            })
    elif table_name == "Bestelldetails":
        for order in raw_data:
            order_id = order["orderID"]
            order_id = int(order_id)
            for product in order.get("items", []):
                processed_data.append({
                    "orderID": order_id,
                    "productID": product["productID"],
                    "Name": product["name"],
                    "Menge": product["quantity"],
                    "Preis": product["price"],
                    "Zwischensumme": product["subtotal"]
                })
    return processed_data

# JSON-Daten hochladen
def upload_json_to_db(connection, json_file, table_name):
    try:
        data = process_json_data(json_file, table_name)

        cursor = connection.cursor()

        # Daten iterieren und in die Tabelle einfügen
        for item in data:
            insert_data(cursor, table_name, item)

        connection.commit()
        print(f"Daten aus {json_file} wurden erfolgreich in {table_name} hochgeladen.")
    except Exception as e:
        print(f"Fehler beim Hochladen von {json_file}:", e)
        connection.rollback()
    finally:
        cursor.close()

# Hauptfunktion
def main():
    connection = connect_to_db()
    if not connection:
        return

    try:
        # Lade Daten für verschiedene Tabellen hoch
        upload_json_to_db(connection, "Exports_NoSQL/onlineshop.customers.json", "Kunden")
        upload_json_to_db(connection, "Exports_NoSQL/onlineshop.products.json", "Produkte")
        upload_json_to_db(connection, "Exports_NoSQL/onlineshop.products.json", "Produkteigenschaften")
        upload_json_to_db(connection, "Exports_NoSQL/onlineshop.products.json", "Bewertungen")
        upload_json_to_db(connection, "Exports_NoSQL/onlineshop.orders.json", "Bestellungen")
        upload_json_to_db(connection, "Exports_NoSQL/onlineshop.orders.json", "Bestelldetails")

    except Exception as e:
        print("Fehler in der Hauptfunktion:", e)
    finally:
        connection.close()
        print("Datenbankverbindung geschlossen.")

if __name__ == "__main__":
    main()
