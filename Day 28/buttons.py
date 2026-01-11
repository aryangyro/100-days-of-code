import tkinter

window = tkinter.Tk()
window.title("Using Tkinter")
window.minsize(height=300,width=500)

label = tkinter.Label(text="HEllo Learning here")
label.pack()

def clicked():
    a = inp.get()
    label.config(text=a)

butoon = tkinter.Button(text="click me", command=clicked)
butoon.pack()

inp = tkinter.Entry()
inp.pack()
a = inp.get()



window.mainloop()