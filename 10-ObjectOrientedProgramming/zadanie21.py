import statistics
class Statistics():
    def __init__(self, numbers):
        self.numbers = numbers
    def maximum(self):
        print(f"Maximum: {max(self.numbers)}")
    def minimum(self):
        print(f"Minimum: {min(self.numbers)}")
    def arithmetic(self):
        print(f"Arithmetic mean: {sum(self.numbers)/len(self.numbers)}")
    def median(self):
        print(f"Median: {statistics.median(self.numbers)}")
    def add(self):
        number = int(input("Enter number you want to add to the set: "))
        self.numbers.append(number)
    def display(self):
        print(" ".join(map(str, self.numbers)))
    
stat = Statistics([12, 37, 6, 9])
stat.display()
stat.add()
stat.display()
stat.maximum()
stat.minimum()
stat.arithmetic()
stat.median()
