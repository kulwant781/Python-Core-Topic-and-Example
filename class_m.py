class Emp:
    company_name ="Apple"

    def show(self):
        print(F"This is a method {self.name} of class Emp {self.company_name}")

    @classmethod #this is a class method in 

    def newcomany(self,company):
        self.company_name = company

        print(f"Company name is changed to {self.company_name}")
        
e1 = Emp()
e1.name = "John"
e1.company_name = "Google"
e1.show()
e1.newcomany("Microsoft")