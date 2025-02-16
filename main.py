
from tkinter import *
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady=50)


def save():
    website = website_input.get()  
    email = email_input.get()
    password = password_input.get()
    with open("data.txt", "a") as data_file: 
        data_file.write(f"{website} | {email} | {password}")  
        website_input.delete(0,END)
        email_input.delete(0,END)
        password_input.delete(0,END)
        
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row = 0, column = 1)

website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)
email_label = Label(text = "Email/Username:")
email_label.grid(column = 0, row = 2)
password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)


website_input = Entry(width = 35)
website_input.grid(column = 1, row = 1, columnspan = 2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column = 1, row = 2, columnspan = 2)
email_input.insert(0,"guri@example.com")

password_input = Entry(width = 16)
password_input.grid(column = 1, row = 3)

password_button = Button(text = "Generate Password", width=15)
password_button.grid(row = 3, column = 2)
add_button = Button(text = "Add", width = 30, command=save)
add_button.grid(row = 4, column = 1, columnspan = 2)
























window.mainloop()
