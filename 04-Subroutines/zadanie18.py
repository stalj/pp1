def numbers(n):
    s = ""
    for i in range (1, n+1):
        s += str(i) + " "
    return s 

x = 15
print(f'Numbers <1,{x}>: {numbers(x)}')
