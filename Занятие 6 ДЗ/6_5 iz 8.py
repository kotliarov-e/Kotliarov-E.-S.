# -- coding: utf-8 --
from tkinter import *
from tkinter import messagebox

def f1():
    res = []
    N = int(txt.get())
    k = 1
    while k**2 <= N:
        res.append(str(k**2))
        k += 1
        lbl1.configure(text=res)

def f2():
    N = int(txt2.get())
    d = 2
    while N % d != 0:
        d += 1
        res2 = d
    lbl2.configure(text=res2)

def f3():
    N = int(txt3.get())
    i = 1
    k = 0
    while i <= (N // 2):
        i *= 2
        k += 1
        res3 = k, i
    lbl3.configure(text=res3)

def f4():
    x = int(txt4.get())
    y = int(txt41.get())
    k = 0
    while x <= y:
        x *= 1.10
        k += 1
        res4 = k + 1
    lbl4.configure(text=res4)


def f5():
    n = str(txt5.get())
    a = n[0:n.find("0")]
    k = len(a)
    lbl5.configure(text=k)

def f6():
    k = 0
    s = 0
    n = int(txt6.get())
    while n != 0:
        s += n
        k += 1
        n = int(txt6.get())
    res6 = s / k
    lbl6.configure(text=res6)

window = Tk()
window.title("Практика 6")
window.geometry('400x250')

lbl = Label(window, text="№1")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
btn = Button(window, text="Нажми!", command=f1)
btn.grid(column=2, row=0)
lbl1 = Label(window, text="")
lbl1.grid(column=3, row=0)

lbl2 = Label(window, text="№2")
lbl2.grid(column=0, row=1)
txt2 = Entry(window, width=10)
txt2.grid(column=1, row=1)
btn2 = Button(window, text="Нажми!", command=f2)
btn2.grid(column=2, row=1)
lbl2 = Label(window, text=" ")
lbl2.grid(column=3, row=1)

lbl3 = Label(window, text="№3")
lbl3.grid(column=0, row=2)
txt3 = Entry(window, width=10)
txt3.grid(column=1, row=2)
btn3 = Button(window, text="Нажми!", command=f3)
btn3.grid(column=2, row=2)
lbl3 = Label(window, text=" ")
lbl3.grid(column=3, row=2)

lbl4 = Label(window, text="№4")
lbl4.grid(column=0, row=3)
txt4 = Entry(window, width=10)
txt4.grid(column=1, row=3)
txt41 = Entry(window, width=10)
txt41.grid(column=2, row=3)
btn4 = Button(window, text="Нажми!", command=f4)
btn4.grid(column=3, row=3)
lbl4 = Label(window, text=" ")
lbl4.grid(column=4, row=3)

lbl5 = Label(window, text="№5")
lbl5.grid(column=0, row=4)
txt5 = Entry(window, width=10)
txt5.grid(column=1, row=4)
btn5 = Button(window, text="Нажми!", command=f5)
btn5.grid(column=2, row=4)
lbl5 = Label(window, text=" ")
lbl5.grid(column=3, row=4)

lbl6 = Label(window, text="№5")
lbl6.grid(column=0, row=5)
txt6 = Entry(window, width=10)
txt6.grid(column=1, row=5)
btn6 = Button(window, text="Нажми!", command=f6)
btn6.grid(column=2, row=5)
lbl6 = Label(window, text=" ")
lbl6.grid(column=3, row=5)


window.mainloop()
