class C():

    def __init__(self,dict):
        self.dict=dict

    def m(self,n):
        import re
        z=""
        for x in self.dict:
            srednia=0
            for y in self.dict[x]:
                srednia+=y
            srednia=srednia/len(self.dict[x])
            if srednia>=n:
                z+=x
        results_list=re.findall(r"[A-Z][a-z]+",z)
        results_list=sorted(results_list)
        results_str=""
        i=0
        for j in results_list:
            results_str+=j
            if i!=len(results_list)-1:
                results_str+=","
            i+=1
        print(results_str)

s = C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})
s.m(3)
s.m(4)