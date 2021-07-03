from tkinter import *
from tkinter import messagebox
import random
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen_pass():
    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_nums = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = password_letter + password_nums + password_symbols

    random.shuffle(password_list)
    password = "".join(password_list)
    entry_pass.insert(0, password)


def saving():
    website = entry_w.get()
    email = entry_email.get()
    password_entry = entry_pass.get()
    new_data = {website: {
        "email": email,
        "password": password_entry
    }}
    if len(website) == 0 or len(password_entry) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"Are you sure to save data?")
        if is_okay:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                entry_pass.delete(0, END)
                entry_w.delete(0, END)


def search():
    website = entry_w.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error",
                            message="File not found")
    else:
        if website in data:
            result = data[website]
            messagebox.showinfo(title="Search Result",
                                message=f"Email: {result['email']} \nPassword: {result['password']}")
        else:
            messagebox.showinfo(title="Search Result",
                                message="There is no such password")


# UI setup
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
img = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# labels
label_w = Label(text="Website:")
label_w.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_pass = Label(text="Password:")
label_pass.grid(column=0, row=3)

# entries
entry_w = Entry(width=21)
entry_w.grid(column=1, row=1)
entry_w.focus()

entry_email = Entry(width=40)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "example@gmail.com")

entry_pass = Entry(width=21)
entry_pass.grid(column=1, row=3)


# buttons
button_pass = Button(text="Generate Password", width=15, command=gen_pass)
button_pass.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=saving)
button_add.grid(column=1, row=4, columnspan=2)

button_search = Button(text="Search", width=15, command=search)
button_search.grid(column=2, row=1)

window.mainloop()
