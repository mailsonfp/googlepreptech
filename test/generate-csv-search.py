import csv
import random
from datetime import datetime, timedelta

# Lista de restaurantes com ID de cozinha
restaurants = [
    ("Deliciousgenix",11), ("Herbed Delicious",9), ("Deliciousscape",1), ("Hideaway Delicious",12),
    ("Cuts Delicious",8), ("Lord Delicious",18), ("Hilltop Delicious",6), ("Fine Delicious",4),
    ("Deliciousish",12), ("Havana Delicious",8), ("Deliciouspad",13), ("Deliciousbea",15),
    ("Deliciousquipo",19), ("Fed Delicious",4), ("Hotspot Delicious",13), ("Gusto Delicious",2),
    ("Deliciouszen",5), ("Deliciouszilla",2), ("Deliciousio",19), ("Crisp Delicious",18),
    ("Deliciousoryx",2), ("Bang Delicious",18), ("Deliciouszoid",4), ("Hearty ChowClick",8),
    ("Traditional Chow",11), ("Bash Chow",9), ("Minty Chow",5), ("Chowaza",12), ("Lucha Chow",14),
    ("Hut Chow",3), ("Wish Chow",1), ("Chowish",19), ("Bazaar Chow",1), ("Story Chow",19),
    ("Hideout Chow",15), ("Strip Chow",19), ("Aroma Chow",18), ("Chowology",6), ("Chowify",2),
    ("Piece Chow",13), ("Cave Chow",6), ("Wagon Chow",1), ("Choworyx",7), ("Whole Chow",4),
    ("Central Chow",1), ("Ambrosial Chow",15), ("Place Chow",11), ("Reservation Table",13),
    ("Chopped Table",3), ("Herbed Table",12), ("Palate Table",14), ("Grove Table",13),
    ("Fodder Table",8), ("Tablebes",13), ("Chow Table",2), ("Bay Table",18), ("Tablebea",10),
    ("Fine Table",12), ("Cellar Table",8), ("Boy Table",13), ("Tableomatic",16), ("Tableque",4),
    ("Tableio",1), ("Tableoont",12), ("Tableadora",8), ("Tableooze",16), ("Garnish Table",4),
    ("Brew Table",8), ("Hotspot Table",15), ("Fresh Table",1), ("Appetite Table",8),
    ("Cave Tasty",18), ("Whole Tasty",5), ("Tastyio",14), ("Lane Tasty",2), ("Nouveau Tasty",9),
    ("Relish Tasty",13), ("Tastyooze",11), ("Binge Tasty",4), ("Fed Tasty",2), ("Diced Tasty",7),
    ("Tastylux",14), ("Tastyaza",18), ("Grill Tasty",2), ("Tastyopolis",8), ("Stand Tasty",16),
    ("Feast Tasty",18), ("Baby Tasty",8), ("Fodder Tasty",9), ("Takeout Tasty",11),
    ("Wrap Tasty",4), ("Tastylia",3), ("Havana Tasty",11), ("Crumb Tasty",11), ("Dished Tasty",18),
    ("Chop Grill",17), ("Festive Grill",6), ("Me Grill",9), ("Lounge Grill",5), ("Coastal Grill",17),
    ("Perfection Grill",7), ("Hungry Grill",9), ("Cater Grill",5), ("Presto Grill",15),
    ("Crispy Grill",19), ("Grilltastic",14), ("Grillsio",19), ("Tasteful Grill",2),
    ("Yummy Grill",15), ("Crisp Grill",19), ("Grillya",13), ("Cuts Grill",8), ("Grillarc",13),
    ("Wish Grill",3), ("Dished Grill",8), ("Divine Grill",7), ("Wedge Grill",2), ("Gusto Grill",3),
    ("Chef Grill",19), ("Grove Palace",1), ("Tasteful Palace",12), ("Perfection Palace",3),
    ("Palaceio",14), ("Palaceado",4), ("Flavor Palace",14), ("Palaceadri",11), ("Hotspot Palace",3),
    ("Palaceopedia",8), ("Gusto Palace",9), ("Feed Palace",7), ("Smash Palace",1),
    ("Gnaw Palace",13), ("Dished Palace",5), ("Spicy PalaceClick to check domain availability.",9),
    ("Nouveau Palace",4), ("Relish Palace",9), ("Palaceistic",9), ("Palacearo",4),
    ("Place Palace",17), ("Aroma Palace",1), ("Fury Palace",17), ("Palacex",18),
    ("Palaceocity",15), ("Ambrosial Yummy",17), ("Nibble Yummy",2), ("Accent Yummy",17),
    ("Yummylia",5), ("Hotspot Yummy",17), ("Chef Yummy",12), ("Acclaimed Yummy",8),
    ("Yummyella",6), ("Palace Yummy",19), ("Sizzle Yummy",18), ("Galore Yummy",9),
    ("Yummyquipo",7), ("Divine Yummy",13), ("Aladdin Yummy",15), ("Yummyscape",13),
    ("Yummylance",6), ("Crisp Yummy",13), ("Cantina Yummy",18), ("Cellar Yummy",6),
    ("Festive Yummy",15), ("Upscale Yummy",11), ("Lucha Yummy",3), ("Diced Yummy",14),
    ("Factory Yummy",13), ("Dude Kitchen",5), ("Kitchengenics",8), ("Galore Kitchen",11),
    ("Story Kitchen",15), ("Kitchenbia",12), ("Fuel Kitchen",2), ("Dished Kitchen",14),
    ("Kitchenish",6), ("Bang Kitchen",11), ("Bit Kitchen",18), ("Kitchenlia",1),
    ("Kitchenster",1), ("Devine Kitchen",16), ("Connoisseur Kitchen",19), ("Munchies Kitchen",9),
    ("Fine Kitchen",17), ("Crisp Kitchen",2), ("Hut Kitchen",17), ("Kitchenvio",12),
    ("Kitchenarc",15), ("Kitchenry",11), ("Safety Kitchen",6), ("Smash Kitchen",7),
    ("Brew Kitchen",18), ("Connoisseur Bar",17), ("Bariva",10), ("Barscape",4), ("Hot Bar",2),
    ("Place Bar",13), ("Grill Bar",5), ("Dine Bar",15), ("Wave Bar",3), ("Embaixada Mineira",20),
    ("Mineiro Prime",20), ("Orfeu",20)
]

# Lista de culinárias com ID
cuisines = [
    ("American",1), ("Chinese",2), ("Thai",3), ("Italian",4), ("French",5), ("Japanese",6),
    ("Turkish",7), ("Korean",8), ("Vietnamese",9), ("Indian",10), ("Spanish",11), ("Greek",12),
    ("Mexican",13), ("Malaysian",14), ("African",15), ("German",16), ("Indonesian",17),
    ("Russian",18), ("Other",19), ("Brazilian",20)
]

# Função para buscar nome da culinária pelo ID
def get_cuisine_name(cuisine_id):
    for name, cid in cuisines:
        if cid == cuisine_id:
            return name
    return None

# Função para gerar uma linha
def generate_row():
    restaurant = random.choice(restaurants)
    restaurant_name, cuisine_id = restaurant
    cuisine_name = get_cuisine_name(cuisine_id)

    row = {
        # "restaurantName": restaurant_name if random.random() < 0.9 else None,
        "restaurantName": None,
        "distance": random.randint(1, 10) if random.random() < 0.9 else None,
        "customerRating": random.randint(1, 5) if random.random() < 0.9 else None,
        "price": round(random.uniform(10.00, 50.00), 2) if random.random() < 0.9 else None,
        "cuisineName": None
        # "cuisineName": cuisine_name if random.random() < 0.9 else None
    }

    # Garantir que pelo menos uma coluna esteja preenchida
    if all(v is None for v in row.values()):
        row["distance"] = random.randint(1, 10) if random.random() < 0.9 else None
        row["price"] = round(random.uniform(10.00, 50.00), 2) if random.random() < 0.9 else None

    return row


# Gerar arquivos com lógica de data
start_date = datetime(2025, 5, 1)


countFile = 10
for i in range(1, 6):
    current_month = start_date.month + i - 1
    current_year = start_date.year + (current_month - 1) // 12
    current_month = (current_month - 1) % 12 + 1
    current_date = datetime(current_year, current_month, 1)

    countFile += 1

    with open(f"planilha_{countFile}.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "restaurantName", "distance", "customerRating", "price", "cuisineName", "searchDate"
        ])
        writer.writeheader()

        day = current_date
        for _ in range(1000):
            row = generate_row()
            row["searchDate"] = day.strftime("%Y-%m-%d")
            writer.writerow({k: ("" if v is None else v) for k, v in row.items()})
            day += timedelta(days=1)
            if day.month != current_date.month:
                day = current_date