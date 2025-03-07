# lambda.py
def apply(fx, value):

    return 6 + fx(value)

cube = lambda x : x*x*x    
print(apply(cube ,2))