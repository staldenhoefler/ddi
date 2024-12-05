import json
import random
from datetime import datetime, timedelta
import os

# Directory to store JSON files
output_dir = "products_json"
os.makedirs(output_dir, exist_ok=True)

# Categories and sample properties
categories = {
    "Elektronik": ["TechBrand", "InnoTech", "FutureGadgets", "GigaTech", "NanoGear"],
    "Haushalt": ["CleanMaster", "HomePlus", "EcoAppliances", "SmartHome", "DailyEssentials"],
    "Bücher": ["BestBooks", "ReadNow", "EpicReads", "PageTurner", "BookHive"],
    "Kleidung": ["FashionFit", "WearDaily", "StylePro", "TrendLine", "ClassicThreads"],
    "Spielzeug": ["FunTime", "PlayWorld", "KidZone", "HappyToys", "AdventurePlay"],
    "Sport": ["FitGear", "ActiveLife", "ProSports", "OutdoorX", "HealthPlus"],
    "Möbel": ["CozyHome", "DesignSpace", "WoodCraft", "ModernLiving", "ComfortZone"],
    "Kosmetik": ["BeautyCare", "GlowEssence", "SkinSmooth", "LuxCosmetics", "NatureCare"],
    "Automobil": ["AutoParts", "DriveTech", "CarZone", "MotoGear", "SpeedPro"],
    "Garten": ["GreenLife", "GrowSmart", "GardenPro", "PlantBuddy", "EcoGardens"],
    "Musik": ["SoundWave", "TuneWorld", "BeatHub", "HarmonyGear", "MusicPlus"],
    "Bürobedarf": ["OfficePro", "WorkSmart", "DeskEssentials", "StationeryHub", "TaskMaster"],
    "Reisen": ["TravelEase", "JetSetter", "Wanderlust", "GoExplore", "AdventureGear"],
    "Lebensmittel": ["FreshChoice", "DailyDelights", "OrganicHub", "TastePro", "KitchenEssentials"],
    "Haustierbedarf": ["PetCare", "HappyPaws", "FurFriends", "AnimalEssentials", "PawfectGear"],
    "Gaming": ["GameZone", "PlayPro", "ConsoleGear", "LevelUp", "PixelWorld"],
    "Gesundheit": ["WellnessHub", "CarePlus", "MediTech", "HealthMate", "VitalLife"]
}


colors = ["Silber", "Schwarz", "Weiß", "Blau", "Rot"]
review_texts = [
    "Fantastisches Produkt, ich bin begeistert!",
    "Super Preis-Leistungs-Verhältnis, klare Kaufempfehlung.",
    "Leider entsprach das Produkt nicht meinen Erwartungen.",
    "Top Qualität, ich werde es wieder kaufen!",
    "Die Lieferung war schnell, aber das Produkt mittelmäßig.",
    "Einfach zu bedienen und sehr nützlich im Alltag.",
    "Das Design ist modern, aber die Funktionalität könnte besser sein.",
    "Eine absolute Enttäuschung, würde ich nicht nochmal kaufen.",
    "Sehr langlebig und robust, perfekt für den täglichen Gebrauch.",
    "Tolles Produkt, aber etwas zu teuer.",
    "Einfach klasse, meine ganze Familie liebt es!",
    "Das Produkt war beschädigt, als es ankam. Nicht zufrieden.",
    "Übertrifft meine Erwartungen in jeder Hinsicht.",
    "Nicht schlecht, aber es gibt bessere Alternativen.",
    "Sehr vielseitig einsetzbar, ich bin zufrieden.",
    "Die Beschreibung war irreführend, nicht wie erwartet.",
    "Ein absolutes Must-Have für alle, die Qualität schätzen!",
    "Mittelmäßige Qualität, aber akzeptabel für den Preis.",
    "Perfekt für meine Bedürfnisse, ich bin sehr zufrieden.",
    "Die Verarbeitung ist hervorragend, absolut empfehlenswert.",
    "Ich hatte mehr erwartet, leider nur durchschnittlich.",
    "Schnelle Lieferung und tolles Produkt, ich bin begeistert!",
    "Nicht das, was ich gesucht habe, aber es funktioniert.",
    "Exzellenter Kundenservice und ein großartiges Produkt.",
    "Die Funktionalität ist großartig, genau was ich brauchte.",
    "Könnte besser sein, aber insgesamt okay.",
    "Das Produkt ist hochwertig und hält, was es verspricht.",
    "Leider nach kurzer Zeit defekt, keine Empfehlung.",
    "Ich bin begeistert, das Produkt hat mein Leben vereinfacht.",
    "Würde ich jedem empfehlen, der ein zuverlässiges Produkt sucht."
]


# Helper functions
def random_date(start_date, end_date):
    """Generate a random date between start_date and end_date."""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def generate_review(review_id, customer_id):
    """Generate a single review."""
    return {
        "reviewID": str(review_id),
        "customerID": str(customer_id),
        "stars": random.randint(1, 5),
        "text": random.choice(review_texts),
        "date": random_date(datetime(2023, 1, 1), datetime(2024, 12, 1)).strftime("%Y-%m-%d"),
    }


def generate_product(product_id):
    """Generate a product with reviews and varied properties."""
    # Wähle eine zufällige Kategorie und eine Marke
    category = random.choice(list(categories.keys()))
    brand = random.choice(categories[category])

    # Eigenschaften basierend auf der Kategorie
    properties = {
        "brand": brand,
        "color": random.choice(colors),
    }

    # Zusätzliche Merkmale abhängig von der Kategorie
    if category == "Elektronik":
        properties.update({
            "warranty": f"{random.randint(1, 3)} Jahre",
            "power": f"{random.randint(50, 500)} Watt",
        })
    elif category == "Kleidung":
        properties.update({
            "size": random.choice(["S", "M", "L", "XL"]),
            "material": random.choice(["Baumwolle", "Polyester", "Wolle"]),
        })
    elif category == "Bücher":
        properties.update({
            "author": random.choice(["Max Mustermann", "Anna Meier", "John Doe"]),
            "pages": random.randint(100, 1000),
            "publisher": random.choice(["BookHive", "EpicReads", "PageTurner"]),
        })
    elif category == "Spielzeug":
        properties.update({
            "age_group": random.choice(["3-5 Jahre", "6-8 Jahre", "9+ Jahre"]),
            "material": random.choice(["Plastik", "Holz", "Metall"]),
        })
    elif category == "Haushalt":
        properties.update({
            "energy_class": random.choice(["A", "A+", "A++"]),
            "dimensions": f"{random.randint(10, 100)}x{random.randint(10, 100)}x{random.randint(10, 100)} cm",
        })

    # Produkt generieren
    return {
        "productID": str(product_id),
        "name": f"{category} Produkt {product_id}",
        "category": category,
        "price": round(random.uniform(10, 2000), 2),
        "properties": properties,
        "reviews": [
            generate_review(review_id, random.randint(1000, 9999))
            for review_id in range(1, random.randint(0, 11))  # 2 bis 5 Reviews pro Produkt
        ],
    }

# Generate and save JSON files
num_products = 10000  # Adjust the number of products here
products = [generate_product(product_id) for product_id in range(1, num_products + 1)]

# Speichere alle Produkte in einer JSON-Datei
output_file = "products.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=4)

print(f"Alle {num_products} Produkte wurden in '{output_file}' gespeichert.")
