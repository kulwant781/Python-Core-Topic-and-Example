#importing tkinter library
import tkinter as tk
from tkinter.constants import SUNKEN

# Initialize the main application window
window = tk.Tk()
window.title('Calculator ajay')

# Create a frame for the calculator
frame = tk.Frame(bg="green", padx=10)
frame.pack()

# Entry widget for displaying input and results
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)

# Define a function to handle button clicks and display numbers
def myclick(number):
    entry.insert(tk.END, number)

# Define a function to evaluate the expression entered
def equal():
    try:
        expression = entry.get()  # Get the expression from the entry widget
        result = eval(expression)  # Evaluate the expression
        entry.delete(0, tk.END)  # Clear the entry widget
        entry.insert(tk.END, result)  # Display the result
    except Exception as e:
        entry.delete(0, tk.END)  # Clear the entry widget
        entry.insert(tk.END, "Error")  # Display an error message

# Define a function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Button labels and their respective positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create buttons and place them in the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(master=frame, text=text, width=5, height=2, command=equal)
    elif text == "C":
        button = tk.Button(master=frame, text=text, width=5, height=2, command=clear)
    else:
        button = tk.Button(master=frame, text=text, width=5, height=2, command=lambda t=text: myclick(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the application
window.mainloop()
