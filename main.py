from tkinter import *

global num1, num2


def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))


def add():
    global num1
    num1 = e.get()
    e.delete(0, END)


def eq():
    global num2
    global num1
    try:
        num2 = e.get()
        e.delete(0, END)
        sume = int(num1) + int(num2)
        e.insert(0, str(sume))
    except NameError:
        return None


def clear():
    e.delete(0, END)


def bk():
    x = e.get()
    e.delete(len(x) - 1)


# create window

root = Tk()
root.title('Calculator')
root.iconbitmap(r'')
root.configure(pady=20, padx=20, bg='#CA4E79')

e = Entry(root, borderwidth=5, border=5, width=23, font=('Georgia 16'), justify='center',)
e.grid(row=0, column=0, columnspan=3, pady=(0, 10), ipady=8)

b7 = Button(root, text='7', padx=40, pady=20, command=lambda: click(7)).grid(row=1, column=0)
b8 = Button(root, text='8', padx=40, pady=20, command=lambda: click(8)).grid(row=1, column=1)
b9 = Button(root, text='9', padx=40, pady=20, command=lambda: click(9)).grid(row=1, column=2)
b4 = Button(root, text='4', padx=40, pady=20, command=lambda: click(4)).grid(row=2, column=0)
b5 = Button(root, text='5', padx=40, pady=20, command=lambda: click(5)).grid(row=2, column=1)
b6 = Button(root, text='6', padx=40, pady=20, command=lambda: click(6)).grid(row=2, column=2)
b1 = Button(root, text='1', padx=40, pady=20, command=lambda: click(1)).grid(row=3, column=0)
b2 = Button(root, text='2', padx=40, pady=20, command=lambda: click(2)).grid(row=3, column=1)
b3 = Button(root, text='3', padx=40, pady=20, command=lambda: click(3)).grid(row=3, column=2)
b0 = Button(root, text='0', padx=40, pady=20, command=lambda: click(0)).grid(row=4, column=1)
bc = Button(root, text='clear ', padx=29, pady=20, command=clear).grid(row=4, column=0)
bb = Button(root, text='<-', padx=37, pady=20, command=bk).grid(row=4, column=2)
ba = Button(root, text='+', padx=39, pady=20, command=add).grid(row=5, column=0)
be = Button(root, text='=', padx=91, pady=20, command=eq).grid(row=5, column=1, columnspan=2)

root.mainloop()
