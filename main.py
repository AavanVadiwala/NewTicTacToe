import time
import tkinter as Tk
from functools import partial

root = Tk.Tk()

numofclicks = 0
output = 0


def winnerWindow():
    tlWinnerWindow = Tk.Toplevel(root, bg='green')
    lblWinner = Tk.Label(tlWinnerWindow, text="Winner is " + output, font=('Arial', 25), bg="green")
    lblWinner.grid(column=0, row=0)
    tlWinnerWindow.mainloop()

def tieWindow():
    tltieWindow = Tk.Toplevel(root, bg='gray')
    lbltie = Tk.Label(tltieWindow, text= output, font=('Arial', 25), bg="grey")
    lbltie.grid(column=0, row=0)
    tlWinnerWindow.mainloop()

def checkWinner():
    global numofclicks
    global output
    if ((a1.get() == 'X' or a1.get() == "O") and (a1.get() == a2.get() == a3.get())) or \
            ((b1.get() == 'X' or b1.get() == "O") and (b1.get() == b2.get() == b3.get())) or \
            ((c1.get() == 'X' or c1.get() == "O") and (c1.get() == c2.get() == c3.get())) or \
            ((a1.get() == 'X' or a1.get() == "O") and (a1.get() == b1.get() == c1.get())) or \
            ((a2.get() == 'X' or a2.get() == "O") and (a2.get() == b2.get() == c2.get())) or \
            ((a3.get() == 'X' or a3.get() == "O") and (a3.get() == b3.get() == c3.get())) or \
            ((a1.get() == 'X' or a1.get() == "O") and (a1.get() == b2.get() == c3.get())) or \
            ((a3.get() == 'X' or a3.get() == "O") and (a3.get() == b2.get() == c1.get())):
        winnerWindow()

    elif (numofclicks == 9):
        output = " Tie "
        tieWindow()


def clear():
    a1.set('')
    a2.set('')
    a3.set('')
    b1.set('')
    b2.set('')
    b3.set('')
    c1.set('')
    c2.set('')
    c3.set('')


def symtiktactoe(txtVar):
    global numofclicks
    global output
    if numofclicks % 2 == 0:
        output = 'X'
    else:
        output = 'O'
    numofclicks = numofclicks + 1
    txtVar.set(output)
    checkWinner()




a1 = Tk.StringVar()
a2 = Tk.StringVar()
a3 = Tk.StringVar()
b1 = Tk.StringVar()
b2 = Tk.StringVar()
b3 = Tk.StringVar()
c1 = Tk.StringVar()
c2 = Tk.StringVar()
c3 = Tk.StringVar()


def play():
    btnA1 = Tk.Button(root, width=10, height=10, command=partial(symtiktactoe, a1), textvariable=a1)
    btnA1.grid(row=0, column=0)
    btnA2 = Tk.Button(root, width=10, height=10, command=partial(symtiktactoe, a2), textvariable=a2)
    btnA2.grid(row=0, column=1)
    btnA3 = Tk.Button(root, width=10, height=10, command=partial(symtiktactoe, a3), textvariable=a3)
    btnA3.grid(row=0, column=2)

    btnB1 = Tk.Button(root, width=10, height=10, command=partial(symtiktactoe, b1), textvariable=b1)
    btnB1.grid(row=1, column=0)
    btnB2 = Tk.Button(root, width=10, height=10, command=partial(symtiktactoe, b2), textvariable=b2)
    btnB2.grid(row=1, column=1)
    btnB3 = Tk.Button(root, width=10, height=10, command=partial(symtiktactoe, b3), textvariable=b3)
    btnB3.grid(row=1, column=2)

    btnC1 = Tk.Button(root, width=10, height=10, command=partial(symtiktactoe, c1), textvariable=c1)
    btnC1.grid(row=2, column=0)
    btnC2 = Tk.Button(root, width=10, height=10, command=partial(symtiktactoe, c2), textvariable=c2)
    btnC2.grid(row=2, column=1)
    btnC3 = Tk.Button(root, width=10, height=10, command=partial(symtiktactoe, c3), textvariable=c3)
    btnC3.grid(row=2, column=2)



play()

root.mainloop()
