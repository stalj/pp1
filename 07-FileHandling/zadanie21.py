file = open('z21.txt','w')

for i in range(1,10):
    file.write(f'{i},{i**2},{i**3}\n')
file.close()
