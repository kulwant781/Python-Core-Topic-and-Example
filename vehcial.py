class Vehicle:  # Fixed spelling from "Vehicel" to "Vehicle"
    
    # Class variable (global for all instances)
    Wheels = 4  

    def __init__(self, carcolor, brandmodel):  # Accept parameters
        # Instance variables (specific to each object)
        self.carcolor = carcolor
        self.brandmodel = brandmodel  

    def show_details(self):  # Fixed spelling from "showdeatils" to "show_details"
        print(f"Car {self.brandmodel} and color {self.carcolor}, also all cars have {self.Wheels} tyres.")

# Creating an instance with parameters
V1 = Vehicle("Black", "Audi")  # Now it correctly passes arguments
V2 = Vehicle("Green", "Swfit") 

# This is value update in car color and model 
V1.carcolor = 'Grey'
V1.brandmodel = 'Maninder'

# print the   value
V1.show_details()
V2.show_details()
