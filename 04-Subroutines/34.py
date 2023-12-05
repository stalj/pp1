def function(number):
    string_var = ""
    for iteration in range(1, number + 1):
        string_var += str(iteration)
    return string_var

print(function(4))
