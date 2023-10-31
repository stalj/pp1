def f(name, surname):
    import json
    m=[]
    with open("data.json", "r") as f:
        a=json.load(f)
        for i in a:
            if i["name"]==name and i["surname"]==surname:
                m.append(i["languages"])
        stronk=''
        for i in m:
            for j in i:
                stronk=stronk+j+","
        a=stronk.strip(",")
        return a

