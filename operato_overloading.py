class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return (f"{self.i}i + {self.j}j + {self.k}k")
    
    def __add__(self, x):
        return Vector(self.i + x.i, self.j + x.j, self.k+ x.k)


V1 = Vector(3, 2, 5)
print(V1)

V2 = Vector(1, 2, 5)
print(V1 + V2)