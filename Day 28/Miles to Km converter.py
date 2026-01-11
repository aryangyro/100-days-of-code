import tkinter

window = tkinter.Tk()
window.title("Miles To Km Converter")
window.minsize(height=300,width=600)
window.config(padx=200,pady=200)

def clicked():
    a = int(inp.get())
    a *= 1.60934
    label3.config(text=a)
    
    
    label3.config(text=a)

label = tkinter.Label(text="Miles")
label.grid(row=0,column=5)

label2 = tkinter.Label(text="Km")
label2.grid(row=1,column=5)

label3 = tkinter.Label(text="0")
label3.grid(row=1,column=4)

label4 = tkinter.Label(text="Is Equals To  -> ")
label4.grid(row=1,column=3)

inp = tkinter.Entry(width=7,justify="center")
inp.grid(row=0,column=4)


butoon = tkinter.Button(text="click me", command=clicked)
butoon.grid(row=2,column=4)








window.mainloop()