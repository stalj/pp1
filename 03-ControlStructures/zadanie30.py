a = str(input('Enter time (24-hour format): '))
if len(a)==5:
    b = a[0]
    c = a[1]
    d = int(b+c)
    f = a[3]
    g = a[4]
    h = int(f+g)
    if d > 12 and d < 24:
        if a[3]== '0':
            print(f"Time in 12-hour format:{d-12}:0{h}pm") 
        else:
            print(f"Time in 12-hour format:{d-12}:{h}pm")
    elif d == 24:
        if a[3]=='0':
            print(f"Time in 12-hour format:{d-12}:0{h}am") 
        elif a[4]=='0':
            print(f"Time in 12-hour format:{d-12}:{h}0am")
        else:
            print(f"Time in 12-hour format:{d-12}:{h}am")
    elif d > 9 and d <= 12:
        if a[3]=='0':
            print(f"Time in 12-hour format:{d}:0{h}am") 
        elif a[4]=='0':
            print(f"Time in 12-hour format:{d}:{h}0am")
        else:
            print(f"Time in 12-hour format:{d}:{h}am")
if len(a)==4:
    e = a[0]
    i = int(e)
    j = a[2]
    k= a[3]
    l = int(j+k)
    if i>0 :
        if a[2]=='0':
            print(f"Time in 12-hour format:{e}:0{l}am") 
        else:
            print(f"Time in 12-hour format:{e}:{l}am")