# this is a class 
class Person:
  
  #this is a controter
    def __init__(self, name, dec):
        self.name = name
        self.dec = dec

    def info(self):
        print(f"{self.name} is {self.dec}")


a = Person("kulwant", "Python")
b = Person("gurpreet", "Php")
c = Person("Rohit", "tester")

a.info()
b.info()
c.info()