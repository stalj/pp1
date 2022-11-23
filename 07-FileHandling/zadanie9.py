file = open('numbers.txt','r') 
sum =0 

for line in file:
    print(line, end =' ')
    sum =sum + int(line)

print()
print(sum,end =' ' )