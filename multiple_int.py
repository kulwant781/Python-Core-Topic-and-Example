class Employee:
    def __init__(self, name):
        self.name =  name

    def show(self):
        print(f"My name is {self.name}")

class Dance:
    def __init__(self, dance):
        self.dance = dance
    
    def show(self):
        print(f"My Fav dance {self.dance}")

class EmpDance(Employee,Dance):
    def __init__(self, name, dance):

        Employee.__init__(self, name)
        Dance.__init__(self, dance)
  
    def show(self):
        # Call both show() methods from Employee and Dance
        Employee.show(self)
        Dance.show(self)

E1 = EmpDance("Kulwant", "Punjabi")
E1.show()


# class Employee:
#     def __init__(self, name):
#         self.name = name  # Correct initialization

#     def show(self):
#         print(f"My name is {self.name}")

# class Dance:
#     def __init__(self, dance):
#         self.dance = dance  # Fixed capitalization of 'self'

#     def show(self):
#         print(f"My favorite dance is {self.dance}")

# class EmpDance(Employee, Dance):
#     def __init__(self, name, dance):
#         # Initialize parent classes using super() and explicitly calling Dance
#         Employee.__init__(self, name)
#         Dance.__init__(self, dance)

#     def show(self):
#         # Call both show() methods from Employee and Dance
#         Employee.show(self)
#         Dance.show(self)

# # Creating an object of EmpDance
# E1 = EmpDance("Kulwant", "Punjabi")
# E1.show()
