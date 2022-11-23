file = open('shopping.txt', 'w')

for i in range(5):
    groseries = input(':')
    file.write(f'{groseries}\n')
file.close()
#p = 'mleko chleb woda'
#p.split(" , ")