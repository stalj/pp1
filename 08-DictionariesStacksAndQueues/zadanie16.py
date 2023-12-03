Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]
def hotel_list(hotels):
    arr1 = []
    if hotels == "Kraków":
        for i in Hotels_in_Krakow:
             arr1.append(i["name"])
    if hotels == "Sopot":
        for i in hotels_in_Sopot:
            arr1.append(i["name"])
    return ", ".join(arr1)
def avg_price(hotels):
    sum = 0
    count = 0
    if hotels == "Kraków":
        for i in Hotels_in_Krakow:
            sum += i["price"]
            count+=1
    if hotels == "Sopot":
        for i in hotels_in_Sopot:
            sum += i["price"]
            count+=1
    return int(sum/count)
print(f"Hotels in Krakow: {hotel_list("Kraków")}")
print(f"Average hotel price in Krakow: {avg_price("Kraków")}")
print(f"Hotels in Sopot: {hotel_list("Sopot")}")
print(f"Average hotel price in Sopot: {avg_price("Sopot")}")
print(f"Cheaper hotels in: {"Kraków" if avg_price("Kraków")<avg_price("Sopot") else "Sopot"}")