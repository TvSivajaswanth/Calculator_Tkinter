from tkinter import *

root = Tk()
root.title("Calculator")

#small label for the last calculation (like 6*5 = 30)
last_label = Label(root, text="", font=("Arial", 10), anchor="e")
last_label.grid(row=0, column=0, columnspan=5, sticky="ew", padx=10)

e = Entry(root, width=30, font=("Arial", 16), justify="right")
e.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

#list box that keeps all past calculations

def click(value):
    if e.get() == "Invalid":
        e.delete(0, END)

    if value == "C":
        e.delete(0, END)
    elif value == "=":
        original = e.get()                   
        expr = original.replace("^", "**")
        try:
            # only allow safe characters before evaluating
            if not all(ch in "0123456789+-*/.() *" for ch in expr):
                raise ValueError
            result = eval(expr)
            e.delete(0, END)
            e.insert(0, str(result))

            # NEW: save to history
            text = f"{original} = {result}"
            last_label.config(text=text)   
        except (ValueError, SyntaxError, ZeroDivisionError):
            e.delete(0, END)
            e.insert(0, "Invalid")
    else:
        e.insert(END, value)

# clears the history
def clear_history():
    last_label.config(text="")

buttons = [
    ("7",1,0),("8",1,1),("9",1,2),("+",1,3),("C",1,4),
    ("6",2,0),("5",2,1),("4",2,2),("-",2,3),("/",2,4),
    ("3",3,0),("2",3,1),("1",3,2),("*",3,3),("^",3,4),
    ("0",4,0),(".",4,1),("(",4,2),(")",4,3),("=",4,4),
]

for text, row, col in buttons:
    Button(root, text=text, padx=20, pady=15,
           command=lambda n=text: click(n)
           ).grid(row=row+1, column=col, sticky="nsew", padx=3, pady=3)  
    
# Clear History button
Button(root, text="Clear History", padx=20, pady=15, command=clear_history
       ).grid(row=6, column=0, columnspan=2, sticky="nsew", padx=3, pady=3)

Button(root, text="Exit", padx=20, pady=15, command=root.destroy
       ).grid(row=6, column=2, columnspan=3, sticky="nsew", padx=3, pady=3)

root.mainloop()