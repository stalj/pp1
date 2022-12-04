def compare(array1, array2):
    arr = True
    s1 = None
    s2 = None
    if len(array1) == len(array2):
        s2 = True
        pass
    else:
        s2 = False
        if len(array1) == len(array2):
            for i in range(int(len(array1))):
                if array1[i] == array2[i]:
                    pass
                else:
                    s1 = False
                if s1 == None:
                    s1 = True
    if s1 != False and s2 != False:
        return arr
    

print(compare(["water","book","sky"] ,  ["water","book","sky"]))
print(compare([True,False] ,  [True,False,True]))
print(compare([5,3,1]  , [5,3,1]))
print(compare([3,2,1] ,  [3,2]))
