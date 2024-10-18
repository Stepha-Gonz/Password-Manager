

from os import close
from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pas_entry.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10)) ]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4)) ]
    password_numbers= [choice(numbers) for _ in range(randint(2, 4)) ]

    password_list=password_letters+password_numbers+password_symbols
    shuffle(password_list)


    password = "".join(password_list)
    pas_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website=web_entry.get()
    email_user=user_entry.get()
    password=pas_entry.get()
    new_data={
        website:{
            "email":email_user,
            "password":password
        }
    }
    if len(website)==0 or len(email_user)==0 or len(password)==0:
        warning_box=messagebox.showerror(title="Empty Fields", message="Sorry, there are empty files")
        
    else:    
        try:
            with open("data_pas.jason", "r") as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
            with open("data_pas.jason", "w") as data_file:
                json.dump(new_data,data_file, indent=4)
        else:
            data.update(new_data)
            with open("data_pas.jason", "w") as data_file:
                json.dump(data,data_file, indent=4)
        finally:
            web_entry.delete(0,END)
            pas_entry.delete(0,END)

    
# ---------------------------- search for website ------------------------------- #        
def search():
    website=web_entry.get()
    try:
        with open("data_pas.jason") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="You have not created any password yet")
    else:
        if website in data:
            email=data[website]["email"]
            pas=data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {pas}")
                    
        else:
            messagebox.showinfo(title="Not Found", message="website not found")   
                




# ---------------------------- UI SETUP ------------------------------- #



window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)





#* Components
canvas=Canvas(width=200, height=200)
app_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=app_image)
canvas.grid(column=1, row=0)


#. Website
web_label=Label(text="Website: ")
web_label.grid(column=0,row=1)


web_entry=Entry(width=30)
web_entry.grid(column=1,row=1,sticky="w")
web_entry.focus()
#. email/username

user_label=Label(text="Username: ")
user_label.grid(column=0, row=2)

user_entry=Entry( width=30)
user_entry.grid(column=1, row=2, columnspan=2, sticky="w")
user_entry.insert(0,"email@gmail.com")

#.Password

pas_label=Label(text="Password: ")
pas_label.grid(column=0, row=3)

pas_entry=Entry(width=30)
pas_entry.grid(column=1,row=3,sticky="w")

#.generate password button

button_generate=Button( text="Generate", command=generate_password)
button_generate.grid(column=2,row=3)

#.search button

search_button=Button(text="search", width=7, command=search)
search_button.grid(column=2, row=1)
#.Add password button

button_add=Button(width=36, text="Add Password", command=save_data)
button_add.grid(column=1,row=4, columnspan=2)







window.mainloop()