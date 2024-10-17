

from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

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
    
    if len(website)>0 and len(email_user)>0 and len(password)>0:
        is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/User: {email_user} \nPassword: {password} Is it ok?")

        if is_ok:
            
            with open("data_pas.txt", "a") as data_file:
                data_file.write(f"Website: {website}, Email/User: {email_user}, Pas: {password}\n")
            web_entry.delete(0,END)
            pas_entry.delete(0,END)

    else:
        warning_box=messagebox.showerror(title="Empty Fields", message="Sorry, there are empty files")





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


web_entry=Entry(width=35)
web_entry.grid(column=1,row=1,columnspan=2)
web_entry.focus()
#. email/username

user_label=Label(text="Email/Username: ")
user_label.grid(column=0, row=2)

user_entry=Entry( width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0,"email@gmail.com")

#.Password

pas_label=Label(text="Password: ")
pas_label.grid(column=0, row=3)

pas_entry=Entry(width=21)
pas_entry.grid(column=1,row=3)

#.generate password button

button_generate=Button( text="Generate", command=generate_password)
button_generate.grid(column=2,row=3)


#.Add password button

button_add=Button(width=36, text="Add Password", command=save_data)
button_add.grid(column=1,row=4, columnspan=2)







window.mainloop()