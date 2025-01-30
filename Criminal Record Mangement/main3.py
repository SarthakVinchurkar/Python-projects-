import tkinter
import Authentication
import Login
import Criminal


if __name__ == '__main__':

    root = tkinter.Tk()
    Authentication.Auth(root)

    if Login.credential:
        obj = Criminal.Criminal(root)
        root.mainloop()
