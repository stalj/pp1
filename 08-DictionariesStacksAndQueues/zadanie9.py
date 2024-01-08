countries = [
    {"name":"Poland", "population":38000000},
    {"name":"England", "population":55980000},
    {"name":"France", "population":67750000},
    {"name":"Italy", "population":59110000},
    {"name":"Spain", "population":47420000}
]
i = 0
print(F"COUNTRY   POPULATION")
while i < len(countries):
    print(f'{countries[i]["name"]:10}{countries[i]["population"]:8}')
    i+=1