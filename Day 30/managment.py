BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from tkinter import messagebox
import csv

window = Tk()
window.title("Management System")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ---------------- LOGIN ---------------- #
def login():
    user_id = inp1.get()
    user_pass = inp2.get()

    try:
        with open("data.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row == [user_id, user_pass]:
                    messagebox.showinfo(title="LOGGED IN", message="You are logged in")
                    return
            messagebox.showerror(title="Error", message="Invalid ID or Password")

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No users found. Create account first.")

# ---------------- CREATE ACCOUNT ---------------- #
def cr8_acc():
    user_id = inp1.get()
    user_pass = inp2.get()

    if not user_id or not user_pass:
        messagebox.showerror(title="Error", message="Fields cannot be empty")
        return

    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([user_id, user_pass])

    messagebox.showinfo(title="Success", message="Account created successfully")
    inp1.delete(0, END)
    inp2.delete(0, END)

# ---------------- UI ---------------- #
Label(text="ID", bg=BACKGROUND_COLOR,highlightthickness=0,highlightbackground=BACKGROUND_COLOR).grid(row=0, column=0)
Label(text="Pass", bg=BACKGROUND_COLOR,highlightthickness=0,highlightbackground=BACKGROUND_COLOR).grid(row=1, column=0)

inp1 = Entry(highlightthickness=0,highlightbackground=BACKGROUND_COLOR)
inp1.grid(row=0, column=1)

inp2 = Entry(show="*",highlightthickness=0,highlightbackground=BACKGROUND_COLOR)
inp2.grid(row=1, column=1)

Button(text="LOG IN", command=login,highlightthickness=0,highlightbackground=BACKGROUND_COLOR).grid(row=2, column=1)
Button(text="Create Account", command=cr8_acc,highlightthickness=0,highlightbackground=BACKGROUND_COLOR).grid(row=3, column=1)

window.mainloop()