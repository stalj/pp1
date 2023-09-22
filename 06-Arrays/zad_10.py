a=[2,3,4,5,6,7,8]
even=0
odd=0

for x in a:
    if x%2==0:
        even+=1
    else:
        odd+=1

print(f'even:{even} odd:{odd}')