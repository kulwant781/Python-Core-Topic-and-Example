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


# multiple data print 
# List of data
data_list = ["Kulwant, 30, Singh", "Guri, 28, Kaur", "Lovepreet, 1, Singh"]

# Create multiple objects and print their details
persons = [persons.stringChange(data) for data in data_list]

for person in persons:
    person.say_hello()