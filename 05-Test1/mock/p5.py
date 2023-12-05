def f(t,c,n):
    count = 0
    for iteration in t:
        if iteration == c:
            count += 1
    if count == n:
        return True
    else:
        return False

# print(f("abcdef","b",2))