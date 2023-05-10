from tkinter import *
from tkinter import messagebox

class Login2DL:
    def __init__(self, root):

        self.root = root
        self.root.title("Register")
        self.root.configure(bg="sky blue")
        self.root.geometry("600x220")
        self.root.maxsize(600,220)

        reguser = Label(self.root, text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white",
                        width=15).place(x=10, y=10)
        self.regtext = Entry(self.root, font=("times new roman", 30), bg="lightgray")
        self.regtext.place(x=200, y=10, width=300, height=35)

        regpass = Label(self.root, text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white",
                        width=15).place(x=10, y=60)
        self.regpss = Entry(self.root, font=("times new roman", 30), show="*", bg="lightgray")
        self.regpss.place(x=200, y=60, width=300, height=35)

        regbtn = Button(self.root, text="Sign in", command=self.check, cursor="hand2", fg="white", bg="#d25d17",
                        font=("times new roman", 20)).place(x=170, y=120)


    def check(self):
        if (self.regtext.get() == "") or (self.regpss.get() == ""):
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)

        else:

            with open("credential.txt","a") as f:
                f.write(self.regtext.get()+"@"+self.regpss.get()+"\n")
                messagebox.showinfo("Welcome","You are registered successfully")


if __name__=="__main__":
    root = Tk()
    obj = Login2DL(root)
    root.mainloop()

