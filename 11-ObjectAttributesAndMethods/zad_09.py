import  random
class Arrays():

    @staticmethod
    def fa(len,x):
        array=[]
        for i in range(len):
            array.append(x)
        return array

    @staticmethod
    def fb(lenght,x,y):
        array=[]
        for z in range(lenght):
            array.append(random.randrange(x,y))
        return array

    @staticmethod
    def fc(array, value_from, value_to):
        sum=0
        for x in array:
            if x>=value_from and x<=value_to:
                sum+=1
        return sum

a=Arrays.fa(6,8)
print(a)

    
