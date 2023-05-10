from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from login2dl import Login2DL
from btdetect2 import BTdetect2

class LoginDL:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1599x1000+0+0")

        # ------------------------image-----------------------------------
        img1 = Image.open("C:\lg4.jpg")
        img1 = img1.resize((1320, 920))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        labelphoto = Label(self.root, image=self.photoimg1, borderwidth=0, )
        labelphoto.place(x=0, y=0,relwidth=1, relheight=1)

        # -------------------Frame-------------------------------------
        framelogin = Frame(self.root, bg="white", height=340, width=500).place(x=660, y=150)

        # ------------------------title--------------------------------------------------------------
        title = Label(framelogin, text="Tumor Detector", font=("Impact", 35, "bold"), fg="powder blue", width=15,
                      bg="white").place(x=740, y=150)
        desc = Label(framelogin, text="Login", font=("Goudy old style", 35, "bold"), fg="#d25d17", bg="white",
                     width=15).place(x=700, y=200)
        username = Label(framelogin, text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white",
                         width=15).place(x=670, y=290)
        self.text = Entry(framelogin, font=("times new roman", 30), bg="lightgray")
        self.text.place(x=850, y=290, width=300, height=35)

        password = Label(framelogin, text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white",
                         width=15).place(x=670, y=350)
        self.pss = Entry(framelogin, font=("times new roman", 30), show="*", bg="lightgray")
        self.pss.place(x=850, y=350, width=300, height=35)

        forget = Button(framelogin, text="Forget Password", bg="white", cursor="hand2", border=0, fg="#d25d17",
                        font=("times new roman", 12)).place(x=850, y=400)
        loginbtn = Button(framelogin, command=self.loginfun, text="Login", cursor="hand2", fg="white", bg="#d25d17",
                          font=("times new roman", 20)).place(x=1000, y=400, width=130, height=35)

        register = Button(self.root, command=self.login, text="Register", cursor="hand2", fg="white",
                          bg="#d25d17",
                          font=("times new roman", 20)).place(x=900, y=500, width=130, height=35)




    def loginfun(self):

        with open("credential.txt","r") as f:
            info = f.readlines()
            for e in info:
                u,p=e.split("@")

                if (self.text.get()==u.strip()) and (self.pss.get()== p.strip()):

                    i=1

                    break
                else:
                        i=0

        if i==1:
            messagebox.showinfo("Welcome", f"Welcome {self.text.get()}", parent=self.root)
            self.newfront()
        else:
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)


    def newfront(self):
        self.new_window = Toplevel(self.root)
        self.app = BTdetect2(self.new_window)

    def login(self):
        self.new_window = Toplevel(self.root)
        self.app = Login2DL(self.new_window)


root = Tk()
obj = LoginDL(root)
root.mainloop()