#Naeemah Davis
import tkinter as tk
from tkinter import *
from tkinter import messagebox

user_pass = {"Naeemah": "davis09", "Ikraam": "sage21", "Atheelah": "vdschyff17"}

root = tk.Tk()
root.geometry("500x400")
root.config(bg="light pink")
root.title("Login")

#labels that appear on the window
username = Label(root, text="Username : ", font="Arial 20", fg="white", bg="light pink")
username.place(x=50, y=50)
password = Label(root, text="Password : ", font="Arial 20", fg="white", bg="light pink")
password.place(x=50, y=100)

#entries where the user can input their usernames and passwords
e_user = Entry(root)
e_user.place(x=250, y=55, width=200, height=28)
e_pass = Entry(root)
e_pass.place(x=250, y=105, width=200, height=28)


def Verify():
    key = e_user.get()
    value = e_pass.get()
    # value = e_pass.get()
    if e_user.get() in user_pass:
        if e_pass.get() == user_pass[e_user.get()]:
            messagebox.showinfo("Verification", "Verification Successful!")
            root.destroy()
            import login
        else:
            messagebox.showinfo("Verification", "Verification Unsuccessful")
    else:
            messagebox.showinfo("Verification", "Verification Unsuccessful")


#button for verification of details
b_verify = Button(root, text="Verify", bg= "pink", font="Arial 20", command= Verify)
b_verify.place(x=70, y=200)

def Clear():
    e_pass.delete(0, END)
    e_user.delete(0, END)

#button to clear all values inserted by the user
b_clear = Button(root, text="Clear", bg= "pink", font="Arial 20", command= Clear)
b_clear.place(x=200, y=200)

def Exit():
    msg =messagebox.askquestion("Exit Application", "Are you sure you want to exit ?")
    if msg == "yes":
        root.destroy()
    else:
        messagebox.showinfo("Return", "You will now return to Login Window")
#button to exit the program
b_exit = Button(root, text="Exit", bg= "red",fg="white", font="Arial 20", command= Exit)
b_exit.place(x=330, y=200, width=100)

root.mainloop()