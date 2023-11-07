def f(human_age):
    if human_age==1:
        dogs_age=10
        return dogs_age
    else:  
        dogs_age=(human_age-2)*4+20
        return dogs_age

print(f(15))
print(f(2))
print(f(1))