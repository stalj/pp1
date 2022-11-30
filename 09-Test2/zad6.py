import json
def f(age, course, average):
    with open("test.json", "r") as f:
        a=json.load(f)
        h=[]
        all=0
        licznik=0
    for i in a:
        if i['age'] >=age:
            #k=[]
            for j in i['studies']['courses']:
                #print(j)
                if j['name']==course:
                    d=0
                    all=0
                    avg=0
                    for n in j['grades']:
                        all=all+n
                        d+=1
                    avg=all//d


                    if avg>=average:
                        licznik=licznik+1

                else:
                    continue
        else:
            continue
    return licznik
print(f(6, "statistics", 4))

