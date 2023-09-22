def f(d,n):
    loty=""
    y=0
    for x in d:
        if d[f"{x}"]>n:
            loty+=x
            loty+=","

    return loty[:-1]

print(f({"LO231":137,"BA7878":92,"NZ15":288},100))
