import json
import random
from datetime import datetime, timedelta
import os

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["onlineshop"]
products_collection = db["customers"]

# Helper functions
def random_name():
    """Generate a random name."""
    first_names = ["Max", "Anna", "Tom", "Lisa", "Tim", "Sarah", "Paul", "Emma", "Felix", "Laura"]
    last_names = ["Mustermann", "Meier", "Schmidt", "Müller", "Schulze", "Lehmann", "Koch", "Bauer", "Richter"]
    return random.choice(first_names), random.choice(last_names)

def generate_email(first_name, last_name):
    """Generate an email address based on the first and last name."""
    domains = ["gmail.com", "yahoo.com", "outlook.com", "web.de", "icloud.com"]
    return f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"

def random_date(start_date, end_date):
    """Generate a random date between start_date and end_date."""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


def generate_product(product_id):
    """Generate a customer."""
    first_name, last_name = random_name()

    # Produkt generieren
    return {
        "customerID":random.randint(1000, 9999),
        "first_name": f"{first_name}",
        "last_name": f"{last_name}",
        "date_of_birth": f'{random_date(datetime(1950, 1, 1), datetime(2003, 1, 1)).strftime("%Y-%m-%d")}',
        "email": generate_email(first_name, last_name),
    }

# Generate and save JSON files
num_products = 10000  # Adjust the number of products here
customers = [generate_product(product_id) for product_id in range(1, num_products + 1)]

# Speichere alle Produkte in einer JSON-Datei
for product in customers:
    products_collection.insert_one(product)

print(f"Alle {num_products} Produkte wurden in MongoDB-Lokal gespeichert.")
