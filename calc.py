import tkinter as tk
import math

def click(x):
    entry.insert(tk.INSERT,x)

def click_func(func):
    entry.insert(tk.END, func + "()")
    entry.icursor(len(entry.get()) - 1)   # move cursor inside ()

def clear():
    entry.delete(0, tk.END)

def calc():
    try:
        expr = entry.get()

        # percentage
        expr = expr.replace("%", "/100")

        # trig functions (degrees → radians)
        expr = expr.replace("sin(", "math.sin(math.radians(")
        expr = expr.replace("cos(", "math.cos(math.radians(")
        expr = expr.replace("tan(", "math.tan(math.radians(")

        # close extra brackets
        count_open = expr.count("math.radians(")
        expr += ")" * count_open

        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(0, round(result, 6))

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("calculator")
root.configure(bg="#FF7F7F")
root.resizable(0, 0)

entry = tk.Entry(
    root,
    font=("Arial", 20),
    bg="purple",
    fg="white",
    bd=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipadx=5, ipady=5)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

r = 1
c = 0
for b in buttons:
    cmd = calc if b == "=" else lambda x=b: click(x)
    tk.Button(
        root,
        text=b,
        command=cmd,
        font=("Arial", 20),
        bg="LightBlue" if b in "+-*/=" else "#FFCCCB",
        fg="white",
        bd=0
    ).grid(row=r, column=c, padx=3, pady=3, ipady=5)

    c += 1
    if c == 4:
        c = 0
        r += 1

# Trigonometric & Percentage Buttons
tk.Button(root, text="sin", command=lambda: click_func("sin"),
          font=("Arial", 16), bg="#ADD8E6", fg="black", bd=0).grid(row=r, column=0, padx=3, pady=3)

tk.Button(root, text="cos", command=lambda: click_func("cos"),
          font=("Arial", 16), bg="#ADD8E6", fg="black", bd=0).grid(row=r, column=1, padx=3, pady=3)

tk.Button(root, text="tan", command=lambda: click_func("tan"),
          font=("Arial", 16), bg="#ADD8E6", fg="black", bd=0).grid(row=r, column=2, padx=3, pady=3)

tk.Button(root, text="%", command=lambda: click("%"),
          font=("Arial", 16), bg="#ADD8E6", fg="black", bd=0).grid(row=r, column=3, padx=3, pady=3)

r += 1

tk.Button(
    root,
    text='c',
    command=clear,
    font=("Arial", 20),
    bg="violet",
    fg="white",
    bd=0,
    width=20,
    height=2
).grid(row=r, column=0, columnspan=4)

root.mainloop()
