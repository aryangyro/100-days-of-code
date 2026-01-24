BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

window = Tk()
window.title("Flash Card For German")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263 ,image = card_front)
canvas.create_text(400,131,text="TiTLE",font=("Arial",20,"italic"))
canvas.create_text(400,263,text="Word",font=("Arial",40,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

card_wrong = PhotoImage(file="images/wrong.png")
card_right = PhotoImage(file="images/right.png")

wrong = Button(image=card_wrong,highlightthickness=0,highlightcolor=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR)
wrong.grid(row=1,column=0)

right = Button(image=card_right,highlightthickness=0,highlightcolor=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR)
right.grid(row=1,column=1)


































window.mainloop()



