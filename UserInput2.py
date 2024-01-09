from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("User Input")
window.geometry("300x200")

s_user_name = "admin"
s_password= "12345"

def control():
    entered_name = str(name.get())
    entered_password = str(password.get())
    if entered_name == s_user_name and entered_password == s_password:
        window2 = Toplevel()
        name.delete(0,END)
        password.delete(0,END)
    else:
        messagebox.showerror("Error","The informations you entered are incorrect.\nCheck the informations please ")
        name.delete(0,END)
        password.delete(0,END)
        

def sign_in():
    global name,password,user_name,user_password,button
    user_name = Label(text="User Name")
    user_name.grid(row=0,column=0)
    user_password = Label(text="Password")
    user_password.grid(row=1,column=0)
    name = Entry()
    name.grid(row=0,column=1)
    password = Entry()
    password.grid(row=1,column=1)
    button = Button(text="Sign in",width=15,command=control)
    button.grid(row=2,column=1)
    
sign_in()

mainloop()