from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genrate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list.extend(random.choice(letters) for _ in range(nr_letters))

    password_list.extend(random.choice(numbers) for _ in range(nr_numbers))

    password_list.extend(random.choice(symbols) for _ in range(nr_symbols))

    random.shuffle(password_list)
    password = "".join(password_list)
    pe.delete(0,END)
    pe.insert(0,password)
    pyperclip.copy(password)
    


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():
    if we.get() and ee.get() and pe.get():
        ans = messagebox.askokcancel(title="ALL DONE", message=f"Your mail is {we.get()} \n Your Pass is {pe.get()} \n \n Is the give info correct? ")
        if ans:
            with open ("data.txt","a") as file:
                file.write(f"{we.get()} | {ee.get()} | {pe.get()}\n")
    
            we.delete(0, END)
            pe.delete(0, END)
        else:
            we.delete(0, END)
            pe.delete(0, END)
            
        
    else:
        messagebox.showwarning(title="Missing INFO",message="Add all Perameters PLZZZZZ")
        

    

    
    


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Genrator")
window.config(padx=100,pady=100)

website_label = Label(text="Website: ")
website_label.grid(row=3,column=0,sticky = "e")

we = website_enter = Entry(width=35)
we.focus()
website_enter.grid(row=3,column=1, columnspan=2)

Email_label = Label(text="Email/Username: ")
Email_label.grid(row=4,column=0,sticky = "e")

ee = Email_enter = Entry(width=35)
ee.insert(0,"kyabaathaa@gmail.com")
Email_enter.grid(row=4,column=1,columnspan=2)

password_label = Label(text="Password: ")
password_label.grid(row=5,column=0,sticky = "e")

pe = Pass_enter = Entry(width=21)
Pass_enter.grid(row=5,column=1)

gen_button = Button(width=14,text="Genrate Password",font=("ariel",10,"bold"),command=genrate_pass)
gen_button.grid(row=5,column=2)


add_button = Button(text="ADD",width=36,command=save_pass)
add_button.grid(row=6,column=1,columnspan=2)

canvas = Canvas(width=200,height=189)
lock = PhotoImage(file="/Users/aryanpanwar/Downloads/password-manager-start/logo.png")
canvas.create_image(100,98,image=lock)
canvas.grid(row=1,column=1)






window.mainloop()