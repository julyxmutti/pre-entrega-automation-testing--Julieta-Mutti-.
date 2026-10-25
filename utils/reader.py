import csv
import json

def read_users_csv():
    with open("data/users.csv", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

def read_products_json():
    with open("data/products.json") as file:
        return json.load(file)

data = read_products_json()
print(data)

"""
[
    {
        'usuario': 'standard_user',
        'password': 'secret_sauce'
    },
    {
        'usuario': 'admin',
        'password': '1234'
    },
    {
        'usuario': 'jose',
        'password': '123'
    }
]
"""