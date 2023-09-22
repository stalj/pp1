def f(n):
    if n<=0:
        return ("")
    elif n>0 and n<=5:
        y=""
        for x in range(n):
            y+="/"
        return f'"{y}"'
    elif n>5:
        y=""
        for x in range(n//5):
            for a in range(5):
                y+="/"
            if x != n//5-1:
                y+="-"
            elif x == n//5-1 and n%5!=0:
                y+="-"
        if n%5!=0:
            for b in range(n%5):
                y+="/"
        return f'"{y}"'

print(f(12))