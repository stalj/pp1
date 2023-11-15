time = 0
washing_product = str(input("What do you want to wash?"))
rinse = bool(input('Do you want an additional rinse?(True/False)'))
spin = bool(input('Do you want an additional spin?(True/False)'))
washing_product = washing_product.lower()
if washing_product == 'jacket':
    time = time + 40
    if spin == 'True':
        time = time + 9
    elif rinse == 'True':
        time = time + 15
elif washing_product == 'shoes':
    time = time + 20
    if spin == False:
        time = time + 9
    elif rinse == True:
        time = time + 15
elif washing_product == 'underware':
    time = time + 70
    if spin == 'True':
        time == time + 9
    elif rinse == 'True':
        time = time + 15
print(f'Total washing time: {time}')