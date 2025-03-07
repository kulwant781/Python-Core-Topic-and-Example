#recursion.py


var = int(input("Enter a number: "))
#print("The factorial of the number is: ", math.factorial(var))

def factorial(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("The factorial of the number is: ", factorial(var))

# //////////////////////////////////////////////////////////////////////////////////////

def generate_fibonacci(n):
    """Generate a Fibonacci sequence of n terms.""" # this is a docstring
    if n <= 0:
        return "Please enter a positive integer."
    
    # Initialize the first two terms
    fib_sequence = [0, 1]
    
    for i in range(2, n):
        # Add the sum of the last two terms to the sequence
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence[:n]  # Return the sequence up to n terms

# Input from the user
num_terms = int(input("Enter the number of terms: "))
result = generate_fibonacci(num_terms)
print("Fibonacci Sequence:", result)
print(generate_fibonacci.__doc__) #print the docstring