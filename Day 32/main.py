BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

data = pandas.read_csv("/Users/aryanpanwar/Downloads/flash-card-project-start/data/11.csv")
to_learn = data.to_dict(orient="records")

current_card = {}

def change_card():
    global current_card, flip_timer
    if current_card:
        to_learn.remove(current_card)
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)  
    canvas.itemconfig(card_background,image = card_front)
    canvas.itemconfig(card_title,text="German",fill = "black")
    canvas.itemconfig(card_word,text=current_card["german"],fill = "black")
    flip_timer = window.after(3000,flip_card)
    
      
def flip_card():
    global current_card
    with open ("broke.csv","a") as file:
        file.write(f"{current_card['german']},{current_card['english']}\n")
    canvas.config(bg=BACKGROUND_COLOR)
    canvas.itemconfig(card_background,image = card_back)
    canvas.itemconfig(card_title,text="English",fill = "white")
    canvas.itemconfig(card_word,text=current_card["english"],fill = "white")
    

window = Tk()
window.title("Flash Card For German")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,flip_card)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263 ,image = card_front)
card_title = canvas.create_text(400,131,text="TiTLE",font=("Arial",20,"italic"))
card_word = canvas.create_text(400,263,text="Word",font=("Arial",40,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

card_wrong = PhotoImage(file="images/wrong.png")
card_right = PhotoImage(file="images/right.png")

wrong = Button(image=card_wrong,highlightthickness=0,highlightcolor=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,command=flip_card)
wrong.grid(row=1,column=0)

right = Button(image=card_right,highlightthickness=0,highlightcolor=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,command=change_card)
right.grid(row=1,column=1)


change_card()

































window.mainloop()



