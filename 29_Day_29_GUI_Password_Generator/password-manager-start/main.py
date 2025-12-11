from tkinter import *
import random
from tkinter import messagebox
import pyperclip

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
special = "!@#$%^&*()_+"
FONT = ("Consolas", 12, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    password_entry.insert(0, "".join(random.choices(alpha + num + special, k=12)))
    pyperclip.copy(password_entry.get())
    messagebox.showinfo(title="Password Generator", message="Password copied to clipboard")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

        # Creamos la ventana
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=30, bg="#005461")

        # Creamos el canvas# Añadimos un canvas

canvas = Canvas(width=200, height=200, highlightthickness=0,bg="#005461")
logo_img = PhotoImage(file=r"C:\Users\danielortega\OneDrive - HOTELERA YALKUITO SA DE CV\Desktop\No Borrar Daniel\32 Web Development\02 Python\29_Day_29_GUI_Password_Generator\password-manager-start\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

        # Creamos los labels de la primera columna

website_label = Label(text="Website:", font=FONT, bg="#005461", fg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=FONT, bg="#005461", fg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=FONT, bg="#005461", fg="white")
password_label.grid(row=3, column=0)

        # Creamos los entry de la segunda columna

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew", pady=5)
website_entry.focus()

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", pady=5)
email_entry.insert(0, "grrddn@hotmail.com")

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="ew", pady=5)

        # Creamos los botones

generate_password_button = Button(text="Generate", font=FONT, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="ew", padx=10)

add_button = Button(text="Add", font=FONT, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew", padx=10, pady=5)


window.mainloop()