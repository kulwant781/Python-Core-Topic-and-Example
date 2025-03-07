class Person:
    name = "kulwant"
    Des = "Python dev"
    Salary = 60

    def info(self):
        print(f"{self.name} is {self.Des} Good")


a = Person()
b = Person()
c = Person()

b.name = "Gurpreet"
b.Dec = "Content Writer"

a.info()
b.info()
c.info()