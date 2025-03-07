

'''THIS IS THE CLASS PASSTO OTHER CLASS AND CALLING METHOD'''
class Parent:
    def parentmethod(self):
        print(f"Kulwant")

class chlidclass(Parent):
    def child(self):
        super().parentmethod()
        print(f"rohit")
      

P2 = chlidclass()
P2.child()

'''THIS IS THE __init__ PASS TO OTHER CLASS AND CALLING METHOD'''


class Parent:
    def __init__(self, name, id):
        self.name = name
        self.id = int(id)

    def parentmethod(self):
        pass
        # print(f"{self.name} and {self.id}")

class chlidclass(Parent):
    def __init__(self, name, id, lang):
        super().__init__(name, id) #this is the parent claa constuter in call child constuter using the super() keyword 
        self.lang = lang

    def child(self):
        super().parentmethod() #this is the parent claas method in call child method  super() keyword 
        print(f"{self.name} and {self.lang} and {self.id}")

P2 = chlidclass("kulwant","9393", "English")
P2.child()