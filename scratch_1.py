from tkinter import *

window = Tk()
window.geometry("370x408+360+20")
window.title("Simple Calculator")
window.config(bg="gray11")
window.resizable(False, False)

def close():
    window.destroy()

def clear():
    entry.delete(0, "end")

def back():
    entry.delete(len(entry.get()) - 1)

def press(input):
    length = len(entry.get())
    entry.insert(length, input)

def add(a, b):
    return float(a) + float(b)

def subtract(a, b):
    return float(a) - float(b)

def multiply(a, b):
    return float(a) * float(b)

def divide(a, b):
    if b != 0:
        return float(a) / float(b)
    else:
        return "Error: Division by zero"

def equal():
    expression = entry.get()
    clear()
    try:
        if "+" in expression:
            data = expression.split("+")
            result = add(data[0], data[1])
        elif "-" in expression:
            data = expression.split("-")
            result = subtract(data[0], data[1])
        elif "×" in expression:
            data = expression.split("×")
            result = multiply(data[0], data[1])
        elif "÷" in expression:
            data = expression.split("÷")
            result = divide(data[0], data[1])
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

entry_string = StringVar()
entry = Entry(window, textvariable=entry_string, foreground="white",
              background="gray20", border=0, font=("Bahnschrift SemiBold", 26))
entry.grid(columnspan=4, ipady=15)

font_value = ("Calibari", 18)

btn_clear = Button(window, text="Clear",
                   background="gray5", foreground="cadetblue1",
                   font=font_value, borderwidth=1, relief=SOLID, command=clear)
btn_clear.grid(row=1, columnspan=2, column=0, sticky=E + W, ipady=5)

btn_backspace = Button(window, text="⌫",
                       background="gray5", foreground="cadetblue1", font=font_value,
                       borderwidth=1, relief=SOLID, command=back)
btn_backspace.grid(row=1, columnspan=2, column=2, sticky=E + W, ipady=5)

btn_7 = Button(window, text="7", background="gray11", foreground="cadetblue1",
               font=font_value, borderwidth=1, relief=SOLID, command=lambda: press(7))
btn_7.grid(row=2, column=0, sticky=E + W, ipady=5)

btn_8 = Button(window, text="8", background="gray11",
               foreground="cadetblue1", font=font_value, borderwidth=1,
               relief=SOLID, command=lambda: press(8))
btn_8.grid(row=2, column=1, sticky=E + W, ipady=5)

btn_9 = Button(window, text="9", background="gray11", foreground="cadetblue1",
               font=font_value, borderwidth=1, relief=SOLID, command=lambda: press(9))
btn_9.grid(row=2, column=2, sticky=E + W, ipady=5)

btn_div = Button(window, text="÷",
                 background="gray5", foreground="cadetblue1", font=font_value,
                 borderwidth=1, relief=SOLID, command=lambda: press("÷"))
btn_div.grid(row=2, column=3, sticky=E + W, ipady=5)

btn_4 = Button(window, text="4", background="gray11", foreground="cadetblue1",
               font=font_value, borderwidth=1, relief=SOLID, command=lambda: press(4))
btn_4.grid(row=3, column=0, sticky=E + W, ipady=5)

btn_5 = Button(window, text="5", background="gray11",
               foreground="cadetblue1", font=font_value, borderwidth=1,
               relief=SOLID, command=lambda: press(5))
btn_5.grid(row=3, column=1, sticky=E + W, ipady=5)

btn_6 = Button(window, text="6", background="gray11", foreground="cadetblue1",
               font=font_value, borderwidth=1, relief=SOLID, command=lambda: press(6))
btn_6.grid(row=3, column=2, sticky=E + W, ipady=5)

btn_mult = Button(window, text="×",
                  background="gray5", foreground="cadetblue1", font=font_value,
                  borderwidth=1, relief=SOLID, command=lambda: press("×"))
btn_mult.grid(row=3, column=3, sticky=E + W, ipady=5)

btn_1 = Button(window, text="1", background="gray11", foreground="cadetblue1",
               font=font_value, borderwidth=1, relief=SOLID, command=lambda: press(1))
btn_1.grid(row=4, column=0, sticky=E + W, ipady=5)

btn_2 = Button(window, text="2", background="gray11",
               foreground="cadetblue1", font=font_value, borderwidth=1,
               relief=SOLID, command=lambda: press(2))
btn_2.grid(row=4, column=1, sticky=E + W, ipady=5)

btn_3 = Button(window, text="3", background="gray11", foreground="cadetblue1",
               font=font_value, borderwidth=1, relief=SOLID, command=lambda: press(3))
btn_3.grid(row=4, column=2, sticky=E + W, ipady=5)

btn_sub = Button(window, text="-",
                 background="gray5", foreground="cadetblue1", font=font_value,
                 borderwidth=1, relief=SOLID, command=lambda: press("-"))
btn_sub.grid(row=4, column=3, sticky=E + W, ipady=5)

btn_dot = Button(window, text=".", background="gray11", foreground="cadetblue1",
                 font=font_value, borderwidth=1, relief=SOLID, command=lambda: press("."))
btn_dot.grid(row=5, column=0, sticky=E + W, ipady=5)

btn_0 = Button(window, text="0", background="gray11",
               foreground="cadetblue1", font=font_value, borderwidth=1,
               relief=SOLID, command=lambda: press(0))
btn_0.grid(row=5, column=1, sticky=E + W, ipady=5)

btn_equal = Button(window, text="=", background="cadetblue1", foreground="White",
                   font=font_value, borderwidth=1, relief=SOLID, command=equal)
btn_equal.grid(row=5, column=2, sticky=E + W, ipady=5)

btn_add = Button(window, text="+",
                 background="gray5", foreground="cadetblue1", font=font_value,
                 borderwidth=1, relief=SOLID, command=lambda: press("+"))
btn_add.grid(row=5, column=3, sticky=E + W, ipady=5)

btn_close = Button(window, text="close",
                   background="gray5", foreground="cadetblue1", font=font_value,
                   borderwidth=1, relief=SOLID, command=close)
btn_close.grid(row=6, columnspan=4, sticky=E + W, ipady=5)

mainloop()
