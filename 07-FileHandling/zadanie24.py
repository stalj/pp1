import csv
with open("studentslist.txt", mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row['age']) < 30:
            print(f"{row['first_name']:8}{row['last_name']:8}{row['email']}")