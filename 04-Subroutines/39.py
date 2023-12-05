def f(sentense):
    var = ""
    for iteration in sentense:
        if iteration != " ":
            var += iteration
    return var

print(f("A programming language is a system of notation for writing computer programs"))
print(eval("2+3-4+5-0"))