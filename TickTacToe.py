import tkinter as Tk
from functools import partial

def clear():
    global numOfTurns
    global gameOver

    for row in range(3):
        for col in range(3):
            inputGrid[row][col].set('')
    numOfTurns = 0
    gameOver = False
    lblStatus.config(text="Player " + str((numOfTurns % 2) + 1) + " turn", bg="blue")


def quit():
    exit(0)


def processUserClick(cell):
    global numOfTurns
    global gameOver

    if gameOver:
        return

    if cell.get() != '':
        lblStatus.config(text="Invalid selection! Player " + str((numOfTurns % 2) + 1) + " try again", bg="red")
        return

    if numOfTurns % 2 == 0:
        cell.set('X')
    else:
        cell.set('O')

    if winnerFound():
        lblStatus.config(text="Player " + str((numOfTurns % 2) + 1) + " WINS!!", bg="green")
        gameOver = True
    elif numOfTurns == 8:
        lblStatus.config(text="Its a TIE!!", bg="green")
        gameOver = True
    else:
        numOfTurns = numOfTurns + 1
        lblStatus.config(text="Player " + str((numOfTurns % 2) + 1) + " turn", bg="blue")


def winnerFound():
    global numOfTurns
    global output

    # Check rows
    for row in range(3):
        if (checkLine(inputGrid[row][0], inputGrid[row][1], inputGrid[row][2])):
            return True

    # Check columns
    for col in range(3):
        if (checkLine(inputGrid[0][col], inputGrid[1][col], inputGrid[2][col])):
            return True

    # Check diagonals
    if (checkLine(inputGrid[0][0], inputGrid[1][1], inputGrid[2][2]) or
            checkLine(inputGrid[2][0], inputGrid[1][1], inputGrid[0][2])):
        return True

    return False


def checkLine(cell1, cell2, cell3):
    if (cell1.get() == 'X' or cell1.get() == 'O') and (cell1.get() == cell2.get() == cell3.get()):
        return True
    else:
        return False


##
# Execution starts from here
##
app = Tk.Tk()
app.title("Tic Tac Toe")

numOfTurns = 0
gameOver = False

inputGrid = []
for row in range(3):
    cols = []
    for col in range(3):
        cols.append(Tk.StringVar())
    inputGrid.append(cols)

btnArray = []
for row in range(3):
    record = []
    for col in range(3):
        button = Tk.Button(app, width=10, height=5,
                           command=partial(processUserClick, inputGrid[row][col]),
                           textvariable=inputGrid[row][col])
        button.grid(row=row, column=col*2, columnspan=2)
        record.append(button)
    btnArray.append(record)

button = Tk.Button(app, width=10, height=3,
                   command=clear,
                   text="New Game")
button.grid(row=3, column=0, columnspan=3, pady=5)

button = Tk.Button(app, width=10, height=3,
                   command=quit,
                   text="Quit Game")
button.grid(row=3, column=3, columnspan=3, pady=5)

lblStatus = Tk.Label(app, height=3, fg="white", bg="blue")
lblStatus.grid(row=4, columnspan=6, sticky='NSEW')
clear()

app.mainloop()
