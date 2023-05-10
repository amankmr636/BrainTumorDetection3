from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class ChatbotDL:
    def __init__(self,root):
        self.root=root
        self.root.title("Chatbot")
        self.root.geometry("730x620+0+0")

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        img_chat=Image.open("C:\logo2.jpg")
        img_chat=img_chat.resize((150,70))

        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,width=730,compound=LEFT,
                          image=self.photoimg,text="MistrBoT",font=("arial",30,"bold"),padx=10,fg="green",bg="white")
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),
                        yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bd=4,bg='white',width=1030)
        btn_frame.pack(fill=X)

        label=Label(btn_frame,text="Type Something",font=("arial",14,"bold"),fg="green",bg="white")
        label.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=ttk.Entry(btn_frame,width=30,font=("times new roman",17,"bold"))
        self.entry.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send",command=self.send,font=("arial",13,"bold"),width=8,bg="red",fg="white")
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear = Button(btn_frame, text="Clear Data",command=self.cler ,font=("arial", 13, "bold"), width=8,fg="white", bg="green")
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        self.msg=''
        self.label1 = Label(btn_frame, text=self.msg, font=("arial", 14, "bold"), fg="green", bg="white")
        self.label1.grid(row=1, column=1, padx=5, sticky=W)

    #==========================Function Declaration=========================

    def send(self):
        send='\t\t\t\t\t'+'You: '+ self.entry.get()
        self.text.insert(END,'\n'+send)

        if (self.entry.get()==''):
            self.msg="Please Enter Some Input"

            self.label1.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.label1.config(text=self.msg,fg='red')

        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'BoT: Hello User')

        elif (self.entry.get() == 'hi'):
            self.text.insert(END,'\n\n' + 'BoT: Hello User'+"\n")

        elif "rexha" in self.entry.get():
            self.text.insert(END,'\n\n'+'BoT: Click on the Voice Assistant logo at the top of the pharmacy page'+"\n")

        elif (self.entry.get() == 'who are you'):
            self.text.insert(END, '\n\n' + 'BoT: I am MistrBoT and I can help you understanding this app'+"\n")

        elif "report" in self.entry.get():
            self.text.insert(END,'\n\n'+'BoT: Enter your Report No in the Report '
                                        'ID field and click on Predict.'+'\n'+
                                        '     You can also use voice assistant by clicking on Report ID button directly.'+"\n")


        elif "patient" in self.entry.get():
            self.text.insert(END,'\n\n'+'BoT: Enter your Patient ID in the Patient '
                                        'ID field and click on Search.'+'\n'+
                                        '     You can also use voice assistant by clicking on Patient ID button directly.'+"\n")

        elif "reportid" in self.entry.get():
            self.text.insert(END,'\n\n'+'BoT: Enter your Report No in the Report '
                                        'ID field and click on Predict.'+'\n'+
                                        '     You can also use voice assistant by clicking on Report ID button directly.'+"\n")


        elif "patientid" in self.entry.get():
            self.text.insert(END,'\n\n'+'BoT: Enter your Patient ID in the Patient '
                                        'ID field and click on Search.'+'\n'+
                                        '     You can also use voice assistant by clicking on Patient ID button directly.'+"\n")

        elif (self.entry.get() == ''):
            self.text.insert(END,'')


        else:
            self.text.insert(END,'\n\nBot: Sorry I did not get it'+"\n")

        self.entry.delete(0,END)
    def cler(self):
        self.text.delete('0.0',END)



if __name__=="__main__":

    root=Tk()
    obj=ChatbotDL(root)
    root.mainloop()
