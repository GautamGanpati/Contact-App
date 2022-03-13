from tkinter import *

root = Tk()


def sign_up():
    root.destroy()
    import Signup


class Signin:
    def __init__(self,root):
        self.root =root
        self.root.title("Contacts App")
        self.root.geometry("300x600")



        #Title
        title = Label(root, text="Sign In", font="ar 15 bold").place(x=120, y=50)
        subtitle = Label(root, text="Don't have an account?", font="ar 10", fg="grey").place(x=80, y=130)
        signup = Button(root ,text="Sign Up", bd=0, font="ar 10", fg="#0089D0", command =sign_up).place(x=220, y=130)

        #Email
        lbl_email = Label(root, text="Email", font="ar 10", fg="grey").place(x=60, y=170)
        self.email = Entry(root, font="ar 10", bg="white" )
        self.email.place(x=63, y=200, width=200, height=35)

        #Password
        lbl_password = Label(root, text="Password", font="ar 10", fg="grey").place(x=60, y=250)
        self.password = Entry(root, font="ar 10", bg="white" )
        self.password.place(x=63, y=280, width=200, height=35)

        def signin():
            root.destroy()
            import Contact_FnL

        #Button
        forget = Button(root, text="Forget your password?",bd=0, font="ar 9", fg="#0089D0").place(x=130, y=320)
        signin = Button(root, text="Sign In", font="ar 10", fg="white", bg="#0089D0", command=signin).place(x=60, y=360, width=200, height=33)


obj = Signin(root)
root.mainloop()
