from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
from tkinter import *
from PIL import Image,ImageTk
import pyttsx3 as pp

class Mlbot:
    def __init__(self,root):
        self.root = root
        self.root.title("Smartbot")

        self.root.geometry("500x650")

        self.engine=pp.init()
        self.voice=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voice[1].id)

        self.chatbot = ChatBot("REXHA")

        self.query = StringVar()

        self.img = Image.open("logo2.png")
        self.img = self.img.resize((150, 70))
        self.photoimg = ImageTk.PhotoImage(self.img)

        self.photolabel = Label(self.root, image=self.photoimg).pack()

        self.conversation = ["Hello",
                        "Hi there!",
                        "How are you doing?",
                        "I'm doing great",
                        "That is good to hear",
                        "Thank You",
                        "What is your name?",
                        "My name is MistrBotML",
                        "You are welcome",
                        "Who created you?",
                        "Aman Kumar"]

        self.conversation2=["How to know about tumor",
                            "Click on Read Button"]

        self.conversation3=["How can I save my data",
                            "Enter all your details in the fields of first window and ckick on save"]

        self.frame = Frame(self.root)
        self.sc = Scrollbar(self.frame)
        self.messages = Listbox(self.frame, width=80, height=20)
        self.sc.pack(side=RIGHT, fill=Y)
        self.messages.pack(side=LEFT, fill=BOTH, pady=10)
        self.frame.pack()

        self.text1 = Entry(self.root, font=("Verdana", 20,), textvariable=self.query).pack(fill=X, pady=10)
        self.btn = Button(self.root, text="Ask", command=self.askbot, font=("Verdana", 20), bg="red").pack()

        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer2=ListTrainer(self.chatbot)
        trainer2.train(self.conversation)

        trainer2.train(self.conversation2)
        trainer2.train(self.conversation3)
        trainer2.train(self.conversation4)

        trainer.train("chatterbot.corpus.english.greetings")

    def speak(self,word):
        self.engine.say(word)
        self.engine.runAndWait()



    def askbot(self):
        self.query2=self.query.get()
        self.answer=self.chatbot.get_response(self.query2)
        ans=str(self.answer)
        self.messages.insert(END,"you:"+ str(self.query2))
        self.messages.insert(END,"bot:"+ ans)
        self.speak(self.answer)



if __name__=="__main__":

    root=Tk()
    obj=Mlbot(root)
    root.mainloop()
