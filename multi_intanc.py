class Employee:
    def __init__(self, name):
        self.name =  name

    def show(self):
        print("My name is {self.name}")

class Dance:
    def __init(self, dance):
        Self.dance = dance
    
    def show(self):
        print("My Fav dance {self.dance}")

class EmpDance(Employee, Dance):
    def __init(self):
        self.name : name
        self.dance : dance

E1 = EmpDance("Kulwant", "Punjabi")
E1.show()