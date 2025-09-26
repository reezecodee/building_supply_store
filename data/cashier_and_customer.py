import random

cashiers = [
    # Tasikmalaya
    {
        "name": "Atyla Azfa",
        "gender": "male",
        "branch_store": "Tasikmalaya",
    },
    {
        "name": "Al Harits",
        "gender": "male",
        "branch_store": "Tasikmalaya",
    },
    {
        "name": "Naura Aliya Lestari",
        "gender": "female",
        "branch_store": "Tasikmalaya",
    },
    {
        "name": "Ayu Putri Avicenna",
        "gender": "female",
        "branch_store": "Tasikmalaya"
    },

    # Jakarta
    {
        "name": "Ahmad Adam",
        "gender": "male",
        "branch_store": "Jakarta"
    },
    {
        "name": "Muhammad Fikru",
        "gender": "male",
        "branch_store": "Jakarta"
    },
    {
        "name": "Erinna Elsa Elizha",
        "gender": "female",
        "branch_store": "Jakarta"
    },
    {
        "name": "Fiona Gianna",
        "gender": "female",
        "branch_store": "Jakarta"
    },

    # Bandung
    {
        "name": "Asep Aziz",
        "gender": "male",
        "branch_store": "Bandung"
    },
    {
        "name": "Anwar Arif Akhtar",
        "gender": "male",
        "branch_store": "Bandung"
    },
    {
        "name": "Harum Hafsa",
        "gender": "female",
        "branch_store": "Bandung"
    },
    {
        "name": "Hera Harsha",
        "gender": "female",
        "branch_store": "Bandung"
    },

    # Surabaya
    {
        "name": "Agus Cahyadi",
        "gender": "male",
        "branch_store": "Surabaya"
    },
    {
        "name": "Burhan Bakhtiar",
        "gender": "male",
        "branch_store": "Surabaya"
    },
    {
        "name": "Isabell Inaya",
        "gender": "female",
        "branch_store": "Surabaya"
    },
    {
        "name": "Zahra Jasmine",
        "gender": "female",
        "branch_store": "Surabaya"
    },

    # Medan
    {
        "name": "Chairil Dhaifullah",
        "gender": "male",
        "branch_store": "Medan"
    },
    {
        "name": "Ehsan Aziz",
        "gender": "male",
        "branch_store": "Medan"
    },
    {
        "name": "Kezia Karen",
        "gender": "female",
        "branch_store": "Medan"
    },
    {
        "name": "Kayla Kiki Lena",
        "gender": "female",
        "branch_store": "Medan"
    },

    # Jayapura
    {
        "name": "Faiz Fadlurrahman",
        "gender": "male",
        "branch_store": "Jayapura"
    },
    {
        "name": "Fauzi Ghaffar",
        "gender": "male",
        "branch_store": "Jayapura"
    },
    {
        "name": "Latifa Laila",
        "gender": "female",
        "branch_store": "Jayapura"
    },
    {
        "name": "Marshanda Maharani",
        "gender": "female",
        "branch_store": "Jayapura"
    },

    # Denpasar
    {
        "name": "Ibrahim Iman",
        "gender": "male",
        "branch_store": "Denpasar"
    },
    {
        "name": "Ilyas Jabar",
        "gender": "male",
        "branch_store": "Denpasar"
    },
    {
        "name": "Nina Octavia",
        "gender": "female",
        "branch_store": "Denpasar"
    },
    {
        "name": "Permata Qaila",
        "gender": "female",
        "branch_store": "Denpasar"
    },
]

def random_cashier_name(store_location):
    names = [c["name"] for c in cashiers if c["branch_store"] == store_location]
    return random.choice(names)


# customers
male_first_names = [
    "Budi", "Agus", "Agung", "Hendra", "Tono", "Asep", "Saiful", "Ferry", "Wawan", "Tono"
]
female_first_names = [
    "Ayu", "Syifa", "Azahra", "Nina", "Kayla", "Ananda", "Melania", "Aleena", "Erna", "Maya"
]
last_names = [
    "Kusuma", "Wijaya", "Jayawardana", "Tanuwijaya", "Malaka", "Pahlevi", "Syaiban", "Ubaid", "Shihab", "Thalib"
]

def random_customer_name(gender = "random"):
    if gender == "male":
        first_name = random.choice(male_first_names)
    elif gender == "female":
        first_name = random.choice(female_first_names)
    else:
        all_first_names = male_first_names + female_first_names
        first_name = random.choice(all_first_names)
    
    last_name = random.choice(last_names)

    return f"{first_name} {last_name}"