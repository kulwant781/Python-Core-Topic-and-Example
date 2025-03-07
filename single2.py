class Cat:
    def __init__(self, name, species):  # Fixed parameter name
        self.name = name
        self.species = species  # Fixed variable name
    
    def makesound(self):
        print(f"{self.name} makes a sound!")

class Animal(Cat):  # Inheriting from Cat
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")  # Fix constructor call
        self.breed = breed  # Store breed information
    
    def makesound(self):
        print("Bark")  # Assuming "Brek" was a typo

# Creating an object of the subclass
A1 = Animal("Checking", "Labrador")
A1.makesound()  # Output: Bark

# Creating an object of the parent class
V2 = Cat("Kitty", "Persian")
V2.makesound()  # Output: Kitty makes a sound!
