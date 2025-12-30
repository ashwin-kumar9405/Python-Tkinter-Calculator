#  Python-Tkinter-Calculator
Project Overview
This project is a basic GUI calculator built using Python’s Tkinter library.
It performs basic arithmetic operations such as addition, subtraction, multiplication, and division, and displays results in a styled graphical interface.

The purpose of this project is to understand GUI programming, event handling, layout management, and exception handling in Python.

 Code Explanation (Line by Line)
 Importing Tkinter Module

import tkinter as tk
Imports the Tkinter GUI library

tk is an alias used to access Tkinter classes and constants easily

 Function to Handle Button Press

def press(v):
    entry.insert(tk.END, v)
This function is called whenever a number or operator button is clicked

v represents the button value

tk.END ensures the value is added at the end of the entry field

 Function to Clear Display

def clear():
    entry.delete(0, tk.END)
Deletes all characters from the calculator display

Used when the Clear (C) button is pressed

 Function to Perform Calculation

def calc():
This function executes when the equals (=) button is clicked


    try:
        result = eval(entry.get())
entry.get() retrieves the expression entered by the user

eval() evaluates the mathematical expression


        entry.delete(0, tk.END)
        entry.insert(0, result)
Clears the display

Inserts the calculated result


    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
Handles invalid expressions

Prevents program crash and displays "Error"

 Creating the Main Window

root = tk.Tk()
Creates the main application window


root.title("Calculator")
Sets the window title


root.configure(bg="#1e1e1e")
Sets a dark background color


root.resizable(False, False)
Disables window resizing to preserve layout

 Creating the Display Entry Widget

entry = tk.Entry(
Creates a text input field to display numbers and results


    font=("Segoe UI", 20),
Sets the font style and size


    bg="#2d2d2d",
    fg="white",
Dark background with white text for readability


    bd=0,
Removes border for a modern look


    justify="right"
Aligns text to the right like a real calculator

 Placing the Entry Using Grid

entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)
Places the entry at the top

columnspan=4 allows it to stretch across the calculator width

Padding improves UI spacing

 Defining Calculator Buttons

buttons = [
A list containing numbers and operators in display order


    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]
Makes button creation easier and avoids repetition

 Initial Grid Position

r = 1
c = 0
r = row index

c = column index

Buttons start from row 1 (below entry)

 Creating Buttons Dynamically

for b in buttons:
Loops through each button value

 Equals Button

if b == "=":
Checks if the button is "="


command=calc
Calls calc() function when clicked

 Operator Buttons

elif b in ("+", "-", "*", "/"):
Identifies operator buttons


command=lambda x=b: press(x)
Inserts operator into the display

 Number Buttons
python
Copy code
else:
Handles digits and decimal point


command=lambda x=b: press(x)
Inserts clicked value into the entry

 Button Placement

btn.grid(row=r, column=c, padx=5, pady=5)
Places button in grid

Padding improves spacing



c += 1
Moves to next column



if c > 3:
    c = 0
    r += 1
Moves to next row after 4 columns

 Clear Button (Full Width)

clear_btn = tk.Button(
Creates a clear button


width=22, height=2
Makes it wider than other buttons


command=clear
Calls clear() function


clear_btn.grid(row=r, column=0, columnspan=4)
Spans across all columns at the bottom

 Running the Application

root.mainloop()
Starts the Tkinter event loop

Keeps the calculator running until closed

 Conclusion
This project demonstrates:

GUI development using Tkinter

Event-driven programming

Dynamic widget creation

Exception handling

Clean and readable Python code

The calculator is simple, user-friendly, and serves as a strong foundation for building advanced GUI applications.

 Author
Venkat Ashwin Kumar
B.Tech Computer Science

