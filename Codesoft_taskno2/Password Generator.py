from tkinter import *
import random
import string

root = Tk()
root.geometry("464x354")
root.maxsize(500,400)
root.title("Password Generator")

Label(text = "Password Generator",
                   fg = "blue",font=("Times",20,"bold",UNDERLINE),
                   padx=10,pady=20).grid(row=0,column=1)

def grp(length):
    characters = string.digits + string.ascii_letters + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def getvals():
    name = nameentry.get()
    length = int(lengthentry.get())
    if len(name) == 0:
        Label(text = "Enter username!").grid(row = 8, column=1)
    else:
        if len(name) > 2:
            if length > 0:
                password = grp(length)
                outputentry.config(state=NORMAL)  # Enable the output entry field
                outputentry.delete(0, END)  # Clear any previous value
                outputentry.insert(0, password)  # Set the generated password
                Label(text = "Your Requirnment are Fulfiled").grid(row = 8, column=1)
            else:
                Label(text = "Length should be greater then 0!").grid(row = 8, column=1)
        else:
            Label(text = "Enter a Correct username!").grid(row = 8, column=1)
    
def accept():
    Label(text = "Thanks for using Password Generator!").grid(row = 8, column=1)
def reset():
    root.destroy()



name = Label(root , text="Enter Username : ",pady=10,font=("Times",12))
length = Label(root , text="Enter Length : ",pady=10,font=("Times",12))
output = Label(root , text="Generated Password : ",pady=10,font=("Times",12))

name.grid(row=1,column=0)
length.grid(row=2,column=0)
output.grid(row=3,column=0)

nameval = StringVar()
lengthval = IntVar()
outputval = StringVar()

nameentry = Entry(root,textvariable="nameval",borderwidth=2,relief="solid")
lengthentry = Entry(root,textvariable="lengthval",borderwidth=2,relief="solid")
outputentry = Entry(root,textvariable="outputval",borderwidth=2,relief="solid",fg="Green")

nameentry.grid(row=1,column=1)
lengthentry.grid(row =2 ,column = 1)
outputentry.grid(row =3 ,column = 1)

Button(text = "Generate Password",command=getvals,padx=1,pady=1,
       font=("times 13 bold"),bg="blue",fg="white",borderwidth=2, relief="solid").grid(row=4,column=1)
Button(text = "Accept",command=accept,padx=1,pady=5,bg = "White", fg="blue",borderwidth=1,width=15, relief="solid").grid(row=5,column=1)
Button(text = "Reset",command=reset,padx=1,pady=10,borderwidth=1,width=15,bg = "White", fg="blue", relief="solid").grid(row=6,column=1)

root.mainloop()