def f(filename):
    tekst=str(filename)

    import re
    x=re.split("\W",tekst)

    return x[0]
  

    

print(f("plik.js"))