def f(filename):
    import re
    a=re.findall('^\w+[A-Za-z0-9]',filename)
    return a
print(f("eee.py"))