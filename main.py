import tkinter as tk
from tkinter import messagebox
import math

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Create the display widget
display = tk.Entry(root, width=30, borderwidth=10, font=("Arial", 18))
display.grid(row=0, column=0, columnspan=5)


# Button click function
def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))


# Button clear function
def button_clear():
    display.delete(0, tk.END)


# Button backspace function
def button_backspace():
    current = display.get()[:-1]
    display.delete(0, tk.END)
    display.insert(0, current)


# Button equal function
# Button equal function
# Button equal function
def button_equal():
    try:
        expression = display.get()

        # Replace function names with math library functions
        expression = expression.replace('tan(', 'math.tan(math.radians(')
        expression = expression.replace('sin(', 'math.sin(math.radians(')
        expression = expression.replace('cos(', 'math.cos(math.radians(')
        expression = expression.replace('√', 'math.sqrt(')
        expression = expression.replace('log(', 'math.log10(')
        expression = expression.replace('ln(', 'math.log(')

        # Ensure all parentheses are closed
        while expression.count('(') > expression.count(')'):
            expression += ')'

        # Evaluate the expression
        result = eval(expression, {"math": math})

        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error","Invalid Input")
        display.delete(0, tk.END)

# Define the buttons
button_1 = tk.Button(root, text="1", padx=30, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=30, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=30, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=30, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=30, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=30, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=30, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=30, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=30, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=30, pady=20, command=lambda: button_click(0))

button_add = tk.Button(root, text="+", padx=29, pady=20, command=lambda: button_click("+"))
button_subtract = tk.Button(root, text="-", padx=31, pady=20, command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=30, pady=20, command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=31, pady=20, command=lambda: button_click("/"))

button_equal = tk.Button(root, text="=", padx=30, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=40, pady=20, command=button_clear)
button_backspace = tk.Button(root, text="←", padx=28, pady=20, command=button_backspace)

button_sin = tk.Button(root, text="sin", padx=28, pady=20, command=lambda: button_click("sin"))
button_cos = tk.Button(root, text="cos", padx=28, pady=20, command=lambda: button_click("cos"))
button_tan = tk.Button(root, text="tan", padx=28, pady=20, command=lambda: button_click("tan"))
button_log = tk.Button(root, text="log", padx=28, pady=20, command=lambda: button_click("log"))
button_ln = tk.Button(root, text="ln", padx=31, pady=20, command=lambda: button_click("ln"))
button_sqrt = tk.Button(root, text="√", padx=30, pady=20, command=lambda: button_click("√"))
button_exp = tk.Button(root, text="exp", padx=24, pady=20, command=lambda: button_click("math.exp"))
button_open_paren = tk.Button(root, text="(", padx=30, pady=20, command=lambda: button_click("("))
button_close_paren = tk.Button(root, text=")", padx=30, pady=20, command=lambda: button_click(")"))

# Place the buttons on the grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)

button_equal.grid(row=5, column=2)
button_clear.grid(row=6, column=0, columnspan=2, sticky="we")  # Moved to its own row
button_backspace.grid(row=1, column=4)

button_sin.grid(row=1, column=3)
button_cos.grid(row=2, column=3)
button_tan.grid(row=2, column=4)
button_log.grid(row=3, column=3)
button_ln.grid(row=3, column=4)
button_sqrt.grid(row=4, column=3)
button_exp.grid(row=4, column=4)
button_open_paren.grid(row=5, column=3)
button_close_paren.grid(row=5, column=4)

# Run the application
root.mainloop()
