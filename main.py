import tkinter as tk

calculation = ''


def adding(symbol):
    global calculation
    calculation += str(symbol)
    results.delete(1.0, "end")
    results.insert(1.0, calculation)


def evaluation():
    global calculation
    try:
        calculation = str(eval(calculation))
        results.delete(1.0, "end")
        results.insert(1.0, calculation)

    except:
        clear_function()
        results.insert(1.0, "ERROR")


def clear_function():
    global calculation
    calculation = ""
    results.delete(1.0, "end")


root = tk.Tk()
root.geometry("550x400")

results = tk.Text(root, height=3, width=40, font=("Arial", 24))
results.grid(columnspan=5)

"""
temp = 1
temp1 = 1
button_list = []
for index in range(1, 10):
    button = tk.Button(root, text=str(index), command=lambda: adding(index), width=5, height=3, font=("Arial", 14))
    print(index)
    if index <= 3:
        button.grid(row=2, column=index)
    elif index <= 6:
        button.grid(row=3, column=temp)
        temp+=1
        print("temp=", temp)
    if index > 6:

        button.grid(row=4, column=temp1)
        temp1+=1
        """
button0 = tk.Button(root, text="0", command=lambda: adding(0), width=5, height=3, font=("Arial", 14))
button0.grid(row=5, column=2)
button1 = tk.Button(root, text="1", command=lambda: adding(1), width=5, height=3, font=("Arial", 14))
button1.grid(row=2, column=1)
button2 = tk.Button(root, text="2", command=lambda: adding(2), width=5, height=3, font=("Arial", 14))
button2.grid(row=2, column=2)
button3 = tk.Button(root, text="3", command=lambda: adding(3), width=5, height=3, font=("Arial", 14))
button3.grid(row=2, column=3)
button4 = tk.Button(root, text="4", command=lambda: adding(4), width=5, height=3, font=("Arial", 14))
button4.grid(row=3, column=1)
button5 = tk.Button(root, text="5", command=lambda: adding(5), width=5, height=3, font=("Arial", 14))
button5.grid(row=3, column=2)
button6 = tk.Button(root, text="6", command=lambda: adding(6), width=5, height=3, font=("Arial", 14))
button6.grid(row=3, column=3)
button7 = tk.Button(root, text="7", command=lambda: adding(7), width=5, height=3, font=("Arial", 14))
button7.grid(row=4, column=1)
button8 = tk.Button(root, text="8", command=lambda: adding(8), width=5, height=3, font=("Arial", 14))
button8.grid(row=4, column=2)
button9 = tk.Button(root, text="9", command=lambda: adding(9), width=5, height=3, font=("Arial", 14))
button9.grid(row=4, column=3)

"""-----------------------------------------------------------------------------------------------------------"""

button_plus = tk.Button(root, text="+", command=lambda: adding("+"), width=5, height=3, font=("Arial", 14))
button_plus.grid(row=2, column=4)

button_minus = tk.Button(root, text="-", command=lambda: adding("-"), width=5, height=3, font=("Arial", 14))
button_minus.grid(row=3, column=4)

button_times = tk.Button(root, text="x", command=lambda: adding("*"), width=5, height=3, font=("Arial", 14))
button_times.grid(row=4, column=4)

button_division = tk.Button(root, text="/", command=lambda: adding("/"), width=5, height=3, font=("Arial", 14))
button_division.grid(row=5, column=4)

button_open = tk.Button(root, text="(", command=lambda: adding("("), width=5, height=3, font=("Arial", 14))
button_open.grid(row=5, column=1)
button_close = tk.Button(root, text=")", command=lambda: adding(")"), width=5, height=3, font=("Arial", 14))
button_close.grid(row=5, column=3)

button_complete = tk.Button(root, text="=", command=evaluation, width=22, height=3, font=("Arial", 14))
button_complete.grid(column=1, row=6, columnspan=2)

button_clear = tk.Button(root, text="C", command=clear_function, width=22, height=3, font=("Arial", 14))
button_clear.grid(column=3, row=6, columnspan=3)

root.mainloop()
