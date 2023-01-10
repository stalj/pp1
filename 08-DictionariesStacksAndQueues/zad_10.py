countries=[
    {"country":"Peru","population":3124444},
    {"country":"Germany","population":84000780},
    {"country":"Chile","population":7543328},
    {"country":"Spain","population":9866542},
    {"country":"Korea","population":247900}
]

for x in range(len(countries)):
    for key, value  in countries[x].items():
        print(key,":",value)
    