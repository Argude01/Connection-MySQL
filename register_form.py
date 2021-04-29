from tkinter import *
from tkinter import ttk
import mydatabase

window = Tk()
frame_app = Frame(window, width=400, height=600, bg="red")
frame_app.pack()

email = StringVar()
pwd = StringVar()
age = StringVar()

def register():
    email = entry_email.get()
    pwd = entry_pwd.get()
    age = entry_age.get()
    
    redsocial_db = mydatabase.MyDatabase()
    redsocial_db.insert_db(email, pwd, age)

# Widgets dentro del contender APP
frame_navbar = Frame(frame_app, width=400, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=150)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=500)
frame_options.grid(row=2, column=0)

# Widgets dentro del contender OPTIONS
frame_food = Frame(frame_options, width=350, height=450, bg="#d48df0")
frame_food.place(x=25, y=30)
label_email = Label(frame_food, 
              text="Correo:",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_email.place(x=20, y=60)
entry_email = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_email.place(x=20, y=100)
label_pwd = Label(frame_food, 
              text="Contraseña:",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_pwd.place(x=20, y=130)
entry_pwd = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"), show="*")
entry_pwd.place(x=20, y=170)
label_age = Label(frame_food, 
              text="Edad:",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_age.place(x=20, y=200)
entry_age = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_age.place(x=20, y=240)

button_register = Button(frame_food, text="Registrarme", 
font=("Calibri", "14", "bold"), command=show_data)
button_register.place(x=20, y=300)

# Widgets dentro del contender NAVBAR
title = Label(frame_navbar, 
              text="Menú",
              font=("Calibri", "14"))
title.place(x=320, y=40)

# Widgets dentro del contender TITLE
title1 = Label(frame_title, 
              text="¡Bienvenido(a)!", 
              font=("Calibri", "22", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title, 
              text="¿Quieres ser parte de nuestra \ncomunidad?", 
              font=("Calibri", "18"),
              justify=LEFT)
title2.place(x=25, y=50)

window.mainloop()