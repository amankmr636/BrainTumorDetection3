from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import random

class Register:

    def __init__(self,root):

        self.a=StringVar()
        self.var1=StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = StringVar()


        z = random.randint(1000, 9999)
        self.var1.set(z)


        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("500x420")
        self.root.maxsize(500,420)

        img = Image.open("C:\windowlogo.jpg")
        img = img.resize((700, 520))

        self.photoimg = ImageTk.PhotoImage(img)

        lblimg = Label(self.root, bd=15, relief=RIDGE,
                       image=self.photoimg, padx=2,
                       pady=4, height=500)
        lblimg.place(x=0, y=0, width=700, height=520)

        lbl = Label(lblimg, font=("arial", 12, "bold"), text="PatientID", padx=2,bg="black",fg="white")
        lbl.place(x=10,y=20)

        ent = Entry(lblimg, bd=3, relief=RIDGE, width=20, font=("arial", 12, "bold"),
                          textvariable=self.var1)
        ent.place(x=100,y=20)



        lbl2 = Label(lblimg, font=("arial", 12, "bold"), text="   Name    ", padx=2,bg="black",fg="white")
        lbl2.place(x=10,y=70)


        ent2 = Entry(lblimg, bd=3, relief=RIDGE, width=20, font=("arial", 12, "bold"),
                          textvariable=self.var2)
        ent2.place(x=100,y=70)

        lbl3 = Label(lblimg, font=("arial", 12, "bold"), text="     Age     ", padx=2,bg="black",fg="white")
        lbl3.place(x=10,y=120)


        ent3 = Entry(lblimg, bd=3, relief=RIDGE, width=20, font=("arial", 12, "bold"),
                          textvariable=self.var3)
        ent3.place(x=100,y=120)

        lbl4 = Label(lblimg, font=("arial", 12, "bold"), text="    Sex    ", padx=2,bg="black",fg="white")
        lbl4.place(x=10,y=170)

        combo4 = ttk.Combobox(lblimg, textvariable=self.var4, width=18, font=("arial", 12, "bold"),
                                 state="readonly")
        combo4["values"] = ("Male","Female")
        combo4.place(x=100,y=170)

        lbl5 = Label(lblimg, font=("arial", 12, "bold"), text=" Disease ", padx=2,bg="black",fg="white")
        lbl5.place(x=10,y=220)



        ent5 = Entry(lblimg, bd=3, relief=RIDGE, width=20, font=("arial", 12, "bold"),
                          textvariable=self.var5)
        ent5.place(x=100,y=220)


        Button(lblimg, text="Register", width=15,height=3,font=("arial",12,"bold"),fg="white",relief=RIDGE,command=self.reg, bg="red").place(x=100, y=320)

        Button(lblimg, text="Exit", width=15,height=3,font=("arial",12,"bold"),fg="white",relief=RIDGE,command=root.destroy, bg="black").place(x=260, y=320)



    def reg(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@", database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("insert into register values(%s,%s,%s,%s,%s)", (self.var1.get(), self.var2.get(),self.var3.get(),
                                                                          self.var4.get(),self.var5.get()))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Registered")


if __name__=="__main__":

    root = Tk()
    obj = Register(root)
    root.mainloop()












