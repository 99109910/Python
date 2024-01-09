from tkinter import *
window = Tk()
window.title("Calculator")
window.geometry("270x250+300+100")
window.resizable(FALSE,FALSE)

warehouse = ""

def calculate(button):
    global warehouse
    if button in "0123456789":
        screen.insert(END,button)
        warehouse += button
        
    if button in "+-/*":
        screen.insert(END,button)
        warehouse += button
        
    if button =="=":
        screen.delete(0,END)
        calculation = eval(warehouse, {"__builtins__":None},{})
        warehouse = str(calculation)
        screen.insert(END,warehouse)
        
    if button == "C":
        screen.delete(0,END)
        warehouse = ""
    
    

screen = Entry(width=40, justify=RIGHT)
screen.grid(row=0,column=0,columnspan=3,ipady=4)

list = ["1","2","3","4","5","6","7","8","9","0","+","-","/","*","=","C"]

line = 1
Column = 0

for i in list:
    commmand = lambda x=i : calculate(x)
    Button(text=i, font="verdana 8  bold",bg="#FFFACD",width=10,height=2, relief=GROOVE,command=commmand).grid(row=line,column=Column)
    Column += 1
    if Column >2:
        Column = 0
        line += 1
        
mainloop()
