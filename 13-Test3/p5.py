class C:
    def __init__(self,numbers):
        self.numbers=numbers
    def __str__(self):
        sum=0
        result=''
        print(list(enumerate(self.numbers)))
        for i,num in enumerate(self.numbers):
            sum+=num
            result+=str(num)
            if i < len(self.numbers) - 1:
                result += '+'
        result+='='+str(sum)
        return result

c = C([5, 12])
print(c)  

c = C([6, 0, 15])
print(c)

