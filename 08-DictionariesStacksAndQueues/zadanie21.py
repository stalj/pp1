import csv
import json
products = []
with open("products.csv", "r") as file:
    data = csv.DictReader(file)
    for row in data:
        products.append(row)
with open("products.json", "w") as file1:
    json.dump(products, file1, indent = 2)