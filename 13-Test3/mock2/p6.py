class C:
    def __init__(self,stronk):
        self.stronk=stronk
    def m(self):
        dic={}
        a=self.stronk
        for i in a:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        return dic
print(C("my moon").m())