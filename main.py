from tkinter import Tk, Canvas, Label, Button, Entry, END, Toplevel, PhotoImage, messagebox
from random import choice, randint, shuffle
import pyperclip

#PASSWORD GENERATOR

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# SAVE PASSWORD 
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

#DELETE PASSWORD
def delete_password(selected_password):
    try:
        with open("data.txt", "r") as data_file:
            lines = data_file.readlines()

        with open("data.txt", "w") as data_file:
            for line in lines:
                if line.strip("\n") != selected_password:
                    data_file.write(line)
        messagebox.showinfo(title="Success", message="Password deleted successfully!")
        show_passwords()
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")

# SHOW SAVED PASSWORDS
def show_passwords():
    try:
        with open("data.txt", "r") as data_file:
            saved_passwords = data_file.readlines()
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        # Create a new window to display passwords
        password_window = Toplevel(window)
        password_window.title("Saved Passwords")
        password_window.config(padx=20, pady=20)

        # label for instructions
        Label(password_window, text="Select a password to delete:", font=("Arial", 10)).grid(row=0, column=0)

        #delete button
        row_index = 1
        for password in saved_passwords:
            password_label = Label(password_window, text=password.strip(), font=("Arial", 10))
            password_label.grid(row=row_index, column=0, pady=5)
            
            # Delete button for each password
            delete_button = Button(password_window, text="Delete", command=lambda pw=password: delete_password(pw.strip()))
            delete_button.grid(row=row_index, column=1, pady=5)

            row_index += 1

#UI_SETUP

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "areeba@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Button to open the new window showing saved passwords
show_passwords_button = Button(text="Show Saved Passwords", width=36, command=show_passwords)
show_passwords_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
