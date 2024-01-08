washing_product = str(input('What do you want to wash?: '))
spin = str(input('Would you like an additional spin? No/Yes: '))
rinse = str(input('Would you like an additional rinse? No/Yes: '))
washing_product = washing_product.lower()
washing_times = {
    "shoes" : 20,
    "jacket": 40,
    "underware" : 70
}
total_time = washing_times.get(washing_product, 0)
if rinse == 'Yes':
    total_time+=15
if spin == 'Yes':
    total_time+=9
print(f'Total washing time: {total_time}')