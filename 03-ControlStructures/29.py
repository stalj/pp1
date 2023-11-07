jacket = 40
underwear = 70
shoes = 20
rinsing = 15
spinning = 9

time = 0

washing_item = input("washing product: ")
rinse = input("rinse?: ")
spin = input("spin?: ")

if washing_item == "jacket":
    time += jacket
if washing_item == "underwear":
    time += underwear
if washing_item == "shoes":
    time += shoes

if rinse[0] == "y":
    time += rinsing
if spin[0] == "y":
    time += spinning

print(f"total washing time: {time} minutes")

