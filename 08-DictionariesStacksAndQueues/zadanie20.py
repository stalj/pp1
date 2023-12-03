import json
with open("euro.json", "r") as file:
    data = json.load(file)
print(f'{"Date":<16}{"Buying Rate":<16}{"Selling rate"}')
print('='*44)
for row in data:
    print(f'{row["effectiveDate"]:<16}{row["bid"]:<16}{row["ask"]}')