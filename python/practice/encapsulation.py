class Person:
    def __init__(self,name,rollno):
        self.name=name
        self.__rollno=rollno

    def get__rollno(self):
            return self.__rollno
        
p1=Person("Ram",15)
print(p1.get__rollno())
