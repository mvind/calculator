# !/usr/bin/python3
import tkinter as tk

storeBuffer = ""
n_buttons = []
operators_buttons = []
screen = None
memory = ""

def main():
    global storeBuffer, screen, operators_buttons

    root = tk.Tk()
    screen = tk.Label(root,text=str(storeBuffer), fg='black', font=("Helvetica", 16))
    screen.grid(row=0,column=0,columnspan=5,sticky='e')

    #---Setup numpad---
    n = 1 #counter
    for i in range(2,6):
        for j in range(1,4):
            B = tk.Button(root, text=str(n))
            B.grid(row=i,column=j)
            n_buttons.append(B)
            n+=1

    #Key binding numpad 1-9 + 0 , =
    #Grid
    n_buttons[0].config(command= lambda: click('1'))
    n_buttons[1].config(command= lambda: click('2'))
    n_buttons[2].config(command= lambda: click('3'))
    n_buttons[3].config(command= lambda: click('4'))
    n_buttons[4].config(command= lambda: click('5'))
    n_buttons[5].config(command= lambda: click('6'))
    n_buttons[6].config(command= lambda: click('7'))
    n_buttons[7].config(command= lambda: click('8'))
    n_buttons[8].config(command= lambda: click('9'))

    #Last row
    n_buttons[9].config(text="0", command = lambda: click('0'))
    n_buttons[10].config(text=".", command = lambda: click('.'))
    n_buttons[11].config(text="=", command = result)

    #---Setup operators---
    operators = ['*','/','+','-', 'Clear', 'Save', 'Del']
    for i in range(0,4):
        B = tk.Button(root, text=str(operators[i]))
        B.grid(row=i+1,column=4)
        operators_buttons.append(B)

    for i in range(0,3):
        B = tk.Button(root, text=str(operators[4+i]))
        B.grid(row=1,column=i+1)
        operators_buttons.append(B)

    #Key binding
    #Side bar
    operators_buttons[0].config(command= lambda: click('*'))
    operators_buttons[1].config(command= lambda: click('/'))
    operators_buttons[2].config(command= lambda: click('+'))
    operators_buttons[3].config(command= lambda: click('-'))

    #Top bar
    operators_buttons[4].config(command= clear)
    operators_buttons[5].config(command= save)
    operators_buttons[6].config(command = delete)

    root.mainloop()

def click(msg):
    #This adds button value to screen buffer when clicked
    global storeBuffer, screen
    storeBuffer += msg
    screen.config(text=storeBuffer)

def result():
    #Evaluates the storeBuffer
    global storeBuffer, screen
    if (eval(storeBuffer)):
        storeBuffer = str(eval(storeBuffer))
    else:
        storeBuffer = 'ERROR'
    screen.config(text=storeBuffer)

def clear():
    #Clears storeBuffer
    global storeBuffer, screen
    storeBuffer = ''
    screen.config(text=storeBuffer)

def delete():
    #Deletes the last entry in storeBuffer
    global storeBuffer, screen
    storeBuffer = storeBuffer[0:len(storeBuffer)-1]
    screen.config(text=storeBuffer)

def save():
    #Saves current storeBuffer and clears
    global storeBuffer, screen, memory

    if memory == "":
        memory = storeBuffer
        clear()
    else:
        storeBuffer+= memory
        screen.config(text=storeBuffer)
        memory = "" #Clearing memory

if __name__ == '__main__':
    main()
