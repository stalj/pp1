def f(dictionary, grade):
    for i in dictionary:
        for j in dictionary.values():
            for k in j["grades"]:
                if grade in j["grades"]:
                    return(True)
                else:
                    return(False)

print(f ({"subject": {"name" : "math"
,"grades":[3,5,3,3,4]}},3))