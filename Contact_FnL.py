from tkinter import *
from tkinter import ttk

root = Tk()


class AddContact:
    def __init__(self, root):
        self.root =root
        self.root.title("Contacts App")
        self.root.geometry("300x600")

        def save():
            n=self.name.get()
            y_coord = 420
            Label(text=n, font="ar 10").place(x=0, y=y_coord)
            self.name.delete(0, END)
            Label(text=self.phno.get(), font="ar 10").place(x=100, y=y_coord)
            self.phno.delete(0, END)
            Label(text=self.email.get(), font="ar 10").place(x=200, y=y_coord)
            self.email.delete(0, END)
            y_coord += 30

        # Title
        title = Label(root, text="Add Contacts", font="ar 15").place(x=100, y=50)

        # Name
        lbl_name = Label(root, text="Name", font="ar 10").place(x=15, y=100)
        self.name = Entry(root, font="ar 10", bg="white")
        self.name.place(x=60, y=100, width=200, height=25)

        # Ph No
        lbl_phno = Label(root, text="Ph No", font="ar 10").place(x=15, y=150)
        self.phno = Entry(root, font="ar 10", bg="white")
        self.phno.place(x=60, y=150, width=200, height=25)

        # Email
        lbl_email = Label(root, text="Email", font="ar 10").place(x=15, y=200)
        self.email = Entry(root, font="ar 10", bg="white")
        self.email.place(x=60, y=200, width=200, height=25)

        # Button
        save = Button(root, text="Save", font="ar 10", bg="#0089D0", command = save).place(x=160, y=250, width=100, height=33)


        # Title
        title = Label(root, text="My Contacts", font="ar 15").place(x=100, y=320)
        lbl_name = Label(root, text="Name", font="ar 10", fg="white", bg="grey").place(x=0, y=370, width=100, height=50)
        lbl_phno = Label(root, text="Ph No", font="ar 10", fg="white", bg="grey").place(x=100, y=370, width=100, height=50)
        lbl_email = Label(root, text="Email", font="ar 10", fg="white", bg="grey").place(x=200, y=370, width=100, height=50)




obj = AddContact(root)
root.mainloop()