from tkinter import *

root = Tk()
root.minsize(400,450)
root.maxsize(400,450)
root.title("Calculator")

def click(event):
    text = event.widget.cget("text")
    if text == "C":
        output.set("")
        outval.update()
    elif text == "^":
        if output.get().isdigit():
            value = int(outval.get()) * int(outval.get())
            output.set(value)
            outval.update()
        else:
            value = eval(outval.get())
            output.set(value*value)
            outval.update()
    elif text == "x":
        current_text = outval.get()
        output.set(current_text[:-1])
    elif text == "=":
        if outval.get().isdigit():
            value = int(outval.get())
        else:
            try:
                value = eval(outval.get())
                output.set(value)
                outval.update()
            except Exception as e:
                output.set("Error")
                outval.update()
    else: 
        var = output.get()
        if var == "Error" or var == "Erro" or var == "Err" or var == "Er" or var == "E":
            output.set("")
            output.set(output.get()+text)
            outval.update()
        else:
            output.set(output.get()+text)
            outval.update()
        

output = StringVar()
output.set("")
outval = Entry(root, textvariable=output,font="Times 30 bold")
outval.pack(padx=5,pady=15)
f=Frame(root,bg="grey",padx=15,pady=15)

b=Button(f,text="9",font="cursive 15 bold",padx=15)
b.grid(row=1,column=0)
b.bind("<Button-1>",click)
b=Button(f,text="8",font="cursive 15 bold",padx=15)
b.grid(row=1,column=1)
b.bind("<Button-1>",click)
b=Button(f,text="7",font="cursive 15 bold",padx=15)
b.grid(row=1,column=2)
b.bind("<Button-1>",click)
b=Button(f,text="+",font="cursive 15 bold",padx=15)
b.grid(row=1,column=3)
b.bind("<Button-1>",click)

b=Button(f,text="6",font="cursive 15 bold",padx=15)
b.grid(row=2,column=0)
b.bind("<Button-1>",click)
b=Button(f,text="5",font="cursive 15 bold",padx=15)
b.grid(row=2,column=1)
b.bind("<Button-1>",click)
b=Button(f,text="4",font="cursive 15 bold",padx=15)
b.grid(row=2,column=2)
b.bind("<Button-1>",click)
b=Button(f,text="-",font="cursive 15 bold",padx=17)
b.grid(row=2,column=3)
b.bind("<Button-1>",click)

b=Button(f,text="3",font="cursive 15 bold",padx=15)
b.grid(row=3,column=0)
b.bind("<Button-1>",click)
b=Button(f,text="2",font="cursive 15 bold",padx=15)
b.grid(row=3,column=1)
b.bind("<Button-1>",click)
b=Button(f,text="1",font="cursive 15 bold",padx=15)
b.grid(row=3,column=2)
b.bind("<Button-1>",click)
b=Button(f,text="*",font="cursive 15 bold",padx=17)
b.grid(row=3,column=3)
b.bind("<Button-1>",click)

b=Button(f,text="C",font="cursive 15 bold",padx=13)
b.grid(row=4,column=0)
b.bind("<Button-1>",click)
b=Button(f,text="0",font="cursive 15 bold",padx=15)
b.grid(row=4,column=1)
b.bind("<Button-1>",click)
b=Button(f,text="x",font="cursive 15 bold",padx=15)
b.grid(row=4,column=2)
b.bind("<Button-1>",click)
b=Button(f,text="/",font="cursive 15 bold",padx=18)
b.grid(row=4,column=3)
b.bind("<Button-1>",click)


b=Button(f,text=".",font="cursive 15 bold",padx=17)
b.grid(row=6,column=0)
b.bind("<Button-1>",click)
b=Button(f,text="00",font="cursive 15 bold",padx=10)
b.grid(row=6,column=1)
b.bind("<Button-1>",click)
b=Button(f,text="^",font="cursive 15 bold",padx=15)
b.grid(row=6,column=2)
b.bind("<Button-1>",click)
b=Button(f,text="=",font="cursive 15 bold",bg="blue",fg="white",padx=15)
b.grid(row=6,column=3)
b.bind("<Button-1>",click)

f.pack()


root.mainloop()