def f(t):
    var = ""
    count = 1
    for iteration in t:
        var += iteration * count + "-"
        count += 1
    var = var[0:len(var) - 1]
    return var

# print(f("a"))