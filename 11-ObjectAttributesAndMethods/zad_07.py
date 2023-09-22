class Student():
    uni="UEK"
    id=100000
    

    def __init__(self,name,surname,field):
        self.name=name
        self.surname=surname 
        self.id=Student.id
        Student.id+=1
        self.field=field

    def __str__(self):
        return(f"Name:{self.name} Surname:{self.surname} Indeks:{self.id} Field:{self.field} Uniwersit:{Student.uni}")

a=Student("Wiktoria","Sadło","Inomatyka")
print(a)

b=Student("Asia","Kot","Zarzadzanie")
print(b)