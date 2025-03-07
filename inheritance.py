# This is class
class Emp:
    #This is construcare
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showdetail(self):
        print(f"Employee ID: {self.id}, Name: {self.name}")

# Now defining the `programing` class outside `Emp` for inheritance
class programing(Emp):
    pass
    # def lang(self):
    #     print("This is the programming class inheriting from the Emp class.")

# Create instances /object
e1 = programing("Kulwant", 781)
e2 = programing("Ishant", 900)

# Call methods
e1.showdetail()
e2.showdetail()
# e2.lang()


