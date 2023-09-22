def sum(x):
    y=0
    while x>0:
        y+=x%10
        x//=10
    return y

print(sum(7182))