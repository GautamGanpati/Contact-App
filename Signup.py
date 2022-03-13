from tkinter import *
root = Tk()


def sign_in():
    root.destroy()
    import main


class Signup:
    def __init__(self,root):
        self.root =root
        self.root.title("Contacts App")
        self.root.geometry("300x600")



        #Title
        title = Label(root, text="Sign Up", font="ar 15 bold").place(x=120, y=50)
        subtitle = Label(root, text="Already have an account?", font="ar 10", fg="grey").place(x=65, y=130)
        signin = Button(root, text="Sign In", bd=0, font="ar 10", fg="#0089D0",command= sign_in).place(x=220, y=130)

        #Email
        lbl_email = Label(root, text="Email", font="ar 10", fg="grey").place(x=60, y=170)
        self.email = Entry(root, font="ar 10", bg="white" )
        self.email.place(x=63, y=200, width=200, height=35)

        #Password
        lbl_password = Label(root, text="Password", font="ar 10", fg="grey").place(x=60, y=250)
        self.password = Entry(root, font="ar 10", bg="white" )
        self.password.place(x=63, y=280, width=200, height=35)

        #Secret
        lbl_secret = Label(root, text="Secret", font="ar 10", fg="grey").place(x=60, y=330)
        self.password = Entry(root, font="ar 10", bg="white")
        self.password.place(x=63, y=360, width=200, height=35)

        def signup():
            root.destroy()
            import main

        #Button
        signup = Button(root, text="Sign Up", font="ar 10", fg="white", bg="#0089D0", command=signup).place(x=60, y=410, width=200, height=33)


obj = Signup(root)
root.mainloop()