import os
import random

# 5 cats and 5 dog breeds, list should be in small case with type of animal and prefix concatinated with the breed name 
breeds = [
    "cat_british_shorthair",
    "cat_siamese",
    "cat_mainecoon",
    "cat_ragdoll",
    "cat_persian",
    "dog_labrador_retriever",
    "dog_german_shepherd",
    "dog_golden_retriever",
    "dog_poodle",
    "dog_bulldog"
]

# nested hashmap as state as key and values as their cities
# cities_by_state = {
#     "California": ["Los Angeles", "San Francisco", "San Diego"],
#     "New York": ["New York City", "Buffalo", "Rochester"],
#     "Texas": ["Houston", "Dallas", "Austin"],
#     "Florida": ["Miami", "Orlando", "Tampa"],
#     "Illinois": ["Chicago", "Springfield", "Peoria"]
# }
us_city_short_codes = [
    "NYC",  # New York City
    "LA",   # Los Angeles
    "CHI",  # Chicago
    "HOU",  # Houston
    "PHX",  # Phoenix
    "PHL",  # Philadelphia
    "SAN",  # San Antonio
    "SD",   # San Diego
    "DAL",  # Dallas
    "SFO",  # San Francisco
    "BOS",  # Boston
    "ATL",  # Atlanta
    "MIA",  # Miami
    "DEN",  # Denver
    "SEA"   # Seattle
]

cat_names = ["Whiskers","Mittens","Fluffy","Smokey","Tigger","Luna","Simba","Shadow","Oliver","Bella","Max","Chloe","Leo","Lucy","Ginger"]
dog_names = ["Buddy","Bailey","Max","Charlie","Lucy","Cooper","Daisy","Rocky","Luna","Sadie","Toby","Molly","Oscar","Stella","Rosie"]
animal_colors = ["Black","White","Gray","Ginger","Tabby","Brown","Tan","Black",  "White","Gray"]
cat_toys = ["Feather wand","Catnip mice","Interactive laser pointer","Scratching post","Tunnel","String","Ball with bell","Cat tree","Sisal mouse","Fishing rod toy"]
dog_activities = ["Walking","Running","Fetching","Playing frisbee","Swimming","Hiking","Agility training","Obedience training","Dog park playtime","Chewing on toys"]

cat_header = "name,age,color,weight,favorite_toy"
dog_header = "name,age,color,weight,favorite_activity"

base_path = 'data'

city="Los Angeles"
state="California"

for city in us_city_short_codes:
    if not os.path.exists(f'data\\{city}'):
        os.makedirs(f'data\\{city}')
    for i in range(random.randrange(1, len(breeds))):
        # print(i)
        breed = random.choice(breeds)
        # print(breed)
        path = f'data\\{city}\\{breed}.csv'
        print(path)
        f = open(path, 'w')
        if breed.startswith('cat'):
            f.write(cat_header + '\n')
        else:
            f.write(dog_header + '\n')
        for _ in range(5):
            if breed.startswith('cat'):
                name = random.choice(cat_names)
                age = random.randint(0, 10)
                color = random.choice(animal_colors)
                weight = round(random.random() * 5, 2)
                favorite_toy = random.choice(cat_toys)
                f.write(f'{name},{age},{color},{weight},{favorite_toy}\n')
            else:
                name = random.choice(dog_names)
                age = random.randint(0, 20)
                color = random.choice(animal_colors)
                weight = round(random.random() * 52, 2)
                favorite_activity = random.choice(dog_activities)
                f.write(f'{name},{age},{color},{weight},{favorite_activity}\n')
        f.close()
