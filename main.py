from tkinter import *
from tkinter import messagebox
from password_manager import generate_password, save, find_password

def handle_generate_password():
    password_entry.delete(0, END)
    password_entry.insert(0, generate_password())

def handle_save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if save(website, email, password):
        website_entry.delete(0, END)
        password_entry.delete(0, END)

def handle_find_password():
    website = website_entry.get()
    data = find_password(website)

    if data:
        email, password = data["email"], data["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

search_button = Button(text="Search", width=13, command=handle_find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=handle_generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=handle_save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
