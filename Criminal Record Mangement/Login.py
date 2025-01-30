from tkinter import messagebox as msg

credential = False


def login(usr_name, pas, rootx):
    username = usr_name.get()
    password = pas.get()

    if(username == "HydraShield") and (password == "smit"):
        global credential
        credential = True
        rootx.quit()

    else:
        msg.showinfo("Invalid", "Invalid Credential!\nTry Again")

    usr_name.set("")
    pas.set("")
