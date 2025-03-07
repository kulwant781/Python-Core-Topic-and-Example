x = 4 # Global variable

def welcome():
    y= 5 # Local variable

    #but change the value of x
    global x
    x = 10
    print("Welcome to the world of Python")
    print(y)
welcome()
print(x)

# What is the output of the following code?