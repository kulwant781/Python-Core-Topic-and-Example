class persons:

    def __init__(self, name, age, lname):
        self.name = name
        self.age = int(age)
        self.lname = lname

    def say_hello(self):
        print(f"Hello, my name is {self.name}{self.lname} and I am {self.age} years old.")

    @classmethod
    def stringChange(cls, data):
        return cls(data.split(",")[0], data.split(",")[1], data.split(",")[2])
    

# single data print 
data = "kulwant, 30, singh"
P1 = persons.stringChange(data) #function name call and pass the data
P1.say_hello() 

# print(dir(P1))
# print(help(P1))
# print(P1.__dict__())