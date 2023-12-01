countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Gerone", "population":12345678},
    {"name":"Germany", "population":98765432},
    {"name":"Russia", "population":456464546},
    {"name":"Not-Russia", "population":4},
]

n= 0
while n < len(countries):
    print(countries[n]["name"], countries[n]["population"])
    n += 1

