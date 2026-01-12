from tkinter import * 
from tkinter import messagebox
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
checkmark = ""
LONG_BREAK_MIN = 20
reps = 0
timer_id = None

# ---------------------------- TIMER RESET ------------------------------- # 
    
def reset():
    global reps, checkmark, timer_id
    reps = 0 
    checkmark = ""
    
    if timer_id:
        window.after_cancel(timer_id)
        timer_id = None
    
    canvas.itemconfig(timer_text,text = "00:00")
    timer.config(text="TIMER")
    
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    if reps % 10 == 0:
        # Long break after 5 work sessions
        count_down(LONG_BREAK_MIN * 1)
        timer.config(text="LONG BREAK", fg=RED)

    elif reps % 2 == 0:
        # Short break
        count_down(SHORT_BREAK_MIN * 1)
        timer.config(text="BREAK", fg=PINK)

    else:
        # Work session
        count_down(WORK_MIN * 1)
        timer.config(text="WORK", fg=GREEN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global checkmark,timer_id
    minutes = count // 60
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds:02d}")
    if count == 10:
        messagebox.showinfo(
            title="Almost Done!",
            message="⏰ 10 seconds left!"
        )

    if count > 0:
        timer_id = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 1:  
            checkmark += "✓"
            check.config(text=checkmark)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomogranate Festival")
window.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=203,height=228,bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file="/Users/aryanpanwar/Downloads/pomodoro-start/tomato.png")
canvas.create_image(103,115,image = tomato)
timer_text = canvas.create_text(103,140,text="00:00",font=(FONT_NAME,25,"bold"),fill="white")
canvas.grid(row=1,column=1)

timer = Label()
timer.config(text="TIMER",font=(FONT_NAME,45,"bold"),fg=GREEN,bg=YELLOW)
timer.grid(row=0,column=1)

check = Label()
check.config(text="",font=(FONT_NAME,45,"bold"),fg=GREEN,bg=YELLOW)
check.grid(row=4,column=1)

start_button = Button(text="Start",bg=YELLOW,activebackground=YELLOW,activeforeground="black",highlightbackground=YELLOW,highlightcolor=YELLOW,fg="black",highlightthickness=0,bd=0,relief=FLAT,command=start_timer)
start_button.grid(row=2,column=0)
reset_button = Button(text="Reset",bg=YELLOW,activebackground=YELLOW,activeforeground="black",highlightbackground=YELLOW,highlightcolor=YELLOW,fg="black",highlightthickness=0,bd=0,relief=FLAT,command=reset)
reset_button.grid(row=2,column=2)
















window.mainloop()

