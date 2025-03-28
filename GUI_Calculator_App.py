import tkinter as tk #Python's standard GUI library
from tkinter import messagebox # imported for displaying error messages

#on Click function
def on_click(button_text): 
    if button_text == "=":
        try:
            expression = entry_var.get() # Get the input from the entry field
            result = eval(expression) # Evaluate the expression
            entry_var.set(result) # Display the result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")  # Show error message
            entry_var.set("") # Clear the entry field
    elif button_text == "C": 
        entry_var.set("")# Clears the input field.
    else:
        entry_var.set(entry_var.get() + button_text)# Append the clicked button text to input

# Initialize main window
root = tk.Tk()
root.title("Simple Calculator") #sets the window title.
root.geometry("300x400") #defines the window size.

entry_var = tk.StringVar() #stores user input.

# Entry field
#Entry() creates the text input field.
#grid() places it in the first row, spanning 4 columns.
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)

# Button layout - 2D list (buttons) stores the calculator layout.
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

#A nested loop creates buttons dynamically:
#Button() initializes each button.
#lambda t=text: on_click(t) ensures the correct button value is passed.
#grid() places each button in the correct row and column.

for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: on_click(t))
        button.grid(row=r+1, column=c, ipadx=10, ipady=10, padx=5, pady=5, sticky="nsew")

root.mainloop() 

#end program
