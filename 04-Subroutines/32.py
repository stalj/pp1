def function(n1, n2, n3):
    var = False
    if n1 < 0:
        var = True
    if n2 < 0:
        var = True
    if n3 < 0:
        var = True

    return var

print(function(11,6,4))