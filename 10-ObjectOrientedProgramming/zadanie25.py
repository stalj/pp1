class C():
    def __init__(self, sectors):
        self.sectors = sectors
    def m1(self, s, n):
        self.sectors.update({s:n})
    def m2(self, s):
        count = 0
        for letter in s:
            if letter in self.sectors.keys():
                count+=self.sectors[letter]
        return count
    
stadion = C({"A":120,"D":150,"G":90,"K":110})
stadion.m1("G",130)
print(stadion.m2("GD"))
print(stadion.m2("KEJ"))
