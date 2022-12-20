class Statistics:
    def __init__(self):
        self.arr=[]
    def addNumbers(self):
        a=input("Enter value: ")
        self.arr.append(a)
    def display(self):
        s=', '
        s=s.join(self.arr)
        print(s)
    def greatest(self):
        self.g=self.arr[0]
        for i in self.arr:
            if int(i)>int(self.g):
                self.g=i
                continue
    def smallest(self):
        self.s=self.arr[0]
        for i in self.arr:
            if int(i)<int(self.s):
                self.s=i
                continue
    def mean(self):
        m=sum(int(self.arr))/len(self.arr)
        print(m)

    def median(self):
        if len(self.arr)%2==0:
            self.median=(int(self.arr[len(self.arr)//2])+int(self.arr[len(self.arr)//2-1]))/2
        else:
            self.median=self.arr[len(self.arr)//2]
    def disp(self):
        print(f'Greatest number:{self.g}\nSmallest number:{self.s}\nArithmetic mean:{self.mean}\nMedian:{self.median}')
