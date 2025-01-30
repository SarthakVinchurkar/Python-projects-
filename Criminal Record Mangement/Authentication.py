from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import Login


def Auth(rootx):
    rootx.geometry("1080x540")
    rootx.title("Authenticating")

    usr_name = StringVar()
    pas = StringVar()

    # Upper Frame
    frm_upr = LabelFrame(rootx, bd=2, relief=RIDGE, text="Authentication",
                         font=('times new roman', 50, 'bold'), bg='grey', fg='black')
    frm_upr.place(x=10, y=10, width=1060, height=520)

    # Image
    img = Image.open('Images/back1.jpg')
    img = img.resize((1045, 500), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(img)

    lbl_img = Label(frm_upr, image=photo1)
    lbl_img.place(x=5, y=190, width=1045, height=245)

    # Label Entry
    xp = 15
    y = 40

    # Username
    username = Label(frm_upr, text="Username :", font=('arial', y, 'bold'), bg='grey')
    username.grid(row=0, column=0, padx=50, pady=xp)

    usernameEntry = ttk.Entry(frm_upr, width=20, font=('arial', y, 'bold'), textvar=usr_name)
    usernameEntry.grid(row=0, column=1, padx=0, pady=xp)

    # password
    password = Label(frm_upr, text="Password :", font=('arial', y, 'bold'), bg='grey')
    password.grid(row=1, column=0, padx=2, pady=xp)

    passwordEntry = ttk.Entry(frm_upr,show='*', width=20, font=('arial', y, 'bold'), textvar=pas)
    passwordEntry.grid(row=1, column=1, padx=0, pady=xp)

    btn_login = Button(frm_upr, text='Login', font=('arial', 25, 'bold'),
                       bg='red', fg='white', width=20, command=lambda: Login.login(usr_name, pas, rootx))
    btn_login.grid(row=2, column=1, padx=2, pady=15)

    rootx.mainloop()
