from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import pyttsx3
import wikipedia
from tkinter import messagebox
import speech_recognition as sr
from tkvideo import tkvideo
import cv2
from keras.models import load_model
from PIL import Image
import numpy as np


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(text):

    engine.say(text)
    engine.runAndWait()  #makes voice audible to user

class BTdetect2:
       def __init__(self,root):

           self.pid = StringVar()
           self.var01 = StringVar()
           self.var02 = StringVar()
           self.var03= StringVar()
           self.var04 = StringVar()
           self.var05 = StringVar()

           self.root=root
           self.root.title("phaREXHA")
           self.root.geometry("1550x800+0+0")
           self.root.attributes("-alpha", 1)
           lbltitle=Label(self.root, text="Tumor Detector", bd=10, relief=RIDGE,
                            bg='black', fg="darkgreen", font=("times new roman", 50, "bold"),padx=2, pady=4)
           lbltitle.pack(side=TOP, fill=X)


           img = Image.open("C:\w1.jpg")
           img = img.resize((880, 420))

           self.photoimg = ImageTk.PhotoImage(img)

           lbltitle2 = Label(self.root, bd=10, relief=RIDGE,
                            bg='black', fg="darkgreen", font=("times new roman", 50, "bold"), image=self.photoimg,padx=2, pady=4,height=500)
           lbltitle2.place(x=0, y=104, width=423, height=301)



           lbltitle3 = Label(self.root, bd=10, relief=RIDGE,
                            bg='black', fg="darkgreen", font=("times new roman", 50, "bold"),padx=2, pady=4,height=500)
           lbltitle3.place(x=423, y=104, width=176, height=401)


           lbltitle4 = Label(self.root, bd=10, relief=RIDGE,
                            bg='black', fg="darkgreen", font=("times new roman", 50, "bold"),padx=2, pady=4,height=500)
           lbltitle4.place(x=0, y=405, width=423, height=100)

           imgrx = Image.open("C:\call.jpg")
           imgrx = imgrx.resize((400, 350))

           self.photoimgrx = ImageTk.PhotoImage(imgrx)

           self.rexha = Label(self.root, bd=10, relief=RIDGE,
                            bg='black', fg="darkgreen",image=self.photoimgrx, font=("times new roman", 50, "bold"),padx=2, pady=4,height=500)
           self.rexha.place(x=599, y=104, width=280, height=401)

           self.video = Label(self.root, bd=10, relief=RIDGE,
                            bg='black', fg="darkgreen", font=("times new roman", 50, "bold"),padx=2, pady=4,height=500)
           self.video.place(x=881, y=105, width=400, height=400)

           self.player = tkvideo("C:\V11.mp4", self.video, loop=1000, size=(380, 400))
           self.player.play()

           DetailFrame = Frame(self.root, bd=10, relief=RIDGE,bg="black")
           DetailFrame.place(x=0, y=505, width=880, height=150)

           Result = Label(self.root, bd=10, relief=RIDGE,text="Result",bg="black",fg="gray",
                          font=("times new roman", 38, "bold italic"),anchor="c")
           Result.place(x=880, y=505, width=401, height=150)

           btnask = Button(self.rexha, text="Ask", borderwidth=0, font=("times new roman", 10, "bold italic"),bg="black",fg="darkgreen",command=self.clicked1,width=280)
           btnask.pack(side=BOTTOM)
           btnrep = Button(self.rexha, text="ReportID",  font=("times new roman", 10, "bold italic"),borderwidth=0,bg="red",fg="darkgreen",command=self.clicked2,width=280)
           btnrep.pack(side=BOTTOM)
           btnpat = Button(self.rexha, text="PatientID", font=("times new roman", 10, "bold italic"), borderwidth=0,bg="yellow",fg="darkgreen",command=self.clicked3,width=280)
           btnpat.pack(side=BOTTOM)

           btnref = Button(self.video, text="Refresh", font=("times new roman", 10, "bold italic"), borderwidth=0,bg="black",fg="black",width=280,command=self.refresh)
           btnref.pack(side=BOTTOM)


           self.entryrid = Entry(lbltitle2,bg="black",fg="green",font=("HELVETICA", 15, " italic"), width=15,textvariable=self.var01)
           self.entryrid.place(x=20,y=25)

           self.entrypid = Entry(lbltitle2,bg="black",fg="green",font=("HELVETICA", 15, " italic"), width=15,textvariable=self.var02)
           self.entrypid.place(x=220,y=25)


           self.entrydate = Entry(lbltitle2 ,bg="black",fg="green",font=("HELVETICA", 15, " italic"), width=15,textvariable=self.var03)
           self.entrydate.place(x=20,y=75)


           self.entryage = Entry(lbltitle2, bg="black",fg="green",font=("HELVETICA", 15, " italic"), width=15,textvariable=self.var04)
           self.entryage.place(x=220,y=75)

           self.entryres = Entry(lbltitle2, bg="black",fg="green",font=("HELVETICA", 15, " italic"), width=33,textvariable=self.var05)
           self.entryres.place(x=20,y=125)

           self.text1 = Text(lbltitle2, height=5, width=41, bg="black", fg="gray")
           self.text1.config(font=("HELVETICA", 12, "italic"))
           self.text1.place(x=20, y=175)

           self.entryage.insert(0,"DoctorID")
           self.entryrid.insert(0,"ReportID")
           self.entrypid.insert(0,"PatientID")
           self.entrydate.insert(0,"Date")
           self.entryres.insert(0, "Tumor/No Tumor")
           self.text1.insert(END, "***Enter Reportno in ReportID field and "
                                "click on predict to get the result***"
                                "*Enter PatientID and click on Search to get all the "
                                "past reports***")

           btnres= Button(lbltitle4, bg="black", height=1, width=15, text="Predict", fg="red",
                           font=("Helvetica", 15, "bold italic"),command=self.result)
           btnres.place(x=0, y=0,height=80,width=200)


           btnres2= Button(lbltitle4, bg="black",height=1, width=15, text="Read", fg="red",
                           font=("Helvetica", 15, "bold italic"),command=self.find)
           btnres2.place(x=201, y=0,height=80,width=200)

           btnsave= Button(lbltitle3, bg="darkgreen", height=1, width=10, text="Save", fg="white",
                           font=("Helvetica", 15, "bold italic"),command=self.save)
           btnsave.place(x=0, y=0,height=80,width=155)

           btnplot= Button(lbltitle3, bg="purple", height=1, width=10, text="Plot", fg="white",
                           font=("Helvetica", 15, "bold italic"),command=self.plot)
           btnplot.place(x=0, y=81,height=80,width=155)

           btnclr= Button(lbltitle3, bg="brown", height=1, width=10, text="Clear", fg="white",
                           font=("Helvetica", 15, "bold italic"),command=self.clear)
           btnclr.place(x=0, y=161,height=80,width=155)

           btndoc= Button(lbltitle3, bg="blue",fg="white", height=1, width=10, text="Search",
                           font=("Helvetica", 15, "bold italic"),command=self.search)
           btndoc.place(x=0, y=241,height=80,width=155)

           btnexit= Button(lbltitle3, bg="black",  width=10, text="Exit", fg="white",
                           font=("Helvetica", 15, "bold italic"),command=self.root.destroy)
           btnexit.place(x=0, y=321,height=60,width=155)










           #=========================DetailFrameDetails=========================================================================
           ScrollX = ttk.Scrollbar(DetailFrame, orient=HORIZONTAL)
           ScrollY = ttk.Scrollbar(DetailFrame, orient=VERTICAL)

           ScrollY.pack(side=RIGHT, fill=Y)


           self.rtable = ttk.Treeview(DetailFrame, column=("ReportID",
           "PatientID", "Date", "DoctorID", "Tumor"),yscrollcommand=ScrollY)
           style = ttk.Style(root)
           style.theme_use("clam")
           style.configure("Treeview", background="black",
                           fieldbackground="black", foreground="green")


           ScrollX.config(command=self.rtable.xview)
           ScrollY.config(command=self.rtable.yview)

           self.rtable.heading("ReportID", text="ReportID")
           self.rtable.heading("PatientID", text="PatientID")
           self.rtable.heading("Date", text="Date")
           self.rtable.heading("DoctorID", text="DoctorID")
           self.rtable.heading("Tumor", text="Tumor")

           self.rtable.column("ReportID", width=100)
           self.rtable.column("PatientID", width=100)
           self.rtable.column("Date", width=100)
           self.rtable.column("DoctorID", width=100)
           self.rtable.column("Tumor", width=100)

           self.rtable.pack(fill=BOTH, expand=1)
           self.FetchData()




       def refresh(self):
           
           self.player = tkvideo("C:\V11.mp4", self.video, loop=1000, size=(380, 400))
 
           self.player.play()

           self.rexha = Label(self.root, bd=10, relief=RIDGE,
                            bg='black', fg="darkgreen",image=self.photoimgrx, font=("times new roman", 50, "bold"),padx=2, pady=4,height=500)
           self.rexha.place(x=599, y=104, width=280, height=401)

           btnask = Button(self.rexha, text="Ask", borderwidth=0, font=("times new roman", 10, "bold italic"),bg="black",fg="darkgreen",command=self.clicked1,width=280)
           btnask.pack(side=BOTTOM)
           btnrep = Button(self.rexha, text="ReportID",  font=("times new roman", 10, "bold italic"),borderwidth=0,bg="red",fg="darkgreen",command=self.clicked2,width=280)
           btnrep.pack(side=BOTTOM)
           btnpat = Button(self.rexha, text="PatientID", font=("times new roman", 10, "bold italic"), borderwidth=0,bg="yellow",fg="darkgreen",command=self.clicked3,width=280)
           btnpat.pack(side=BOTTOM)




       def save(self):

           conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",database="pharma")
           mycursor = conn.cursor()
           mycursor.execute("insert into tumordetection(ReportID,PatientID,Date,DoctorID,Tumor) values(%s,%s,%s,%s,%s)", (self.var01.get(),
                                                                                                                     self.var02.get(),
                                                                                                            self.var03.get(),
                                                                                                                     self.var04.get(),
                                                                                                                     self.var05.get(),))
           conn.commit()

           conn.close()
           messagebox.showinfo("Success","Data Updated")

       def plot(self):
           import cv2
           import os
           from PIL import Image
           import numpy as np
           from sklearn.model_selection import train_test_split
           from keras.layers import Conv2D, MaxPooling2D
           from keras.layers import Activation, Dropout, Flatten, Dense
           from keras.utils import normalize
           from keras.utils import to_categorical

           image_directory = "datasets/"

           no_tumor_images = os.listdir(image_directory + 'no/')
           yes_tumor_images = os.listdir(image_directory + 'yes/')

           dataset = []
           label = []

           INPUT_SIZE = 64

           print(no_tumor_images)

           for i, image_name in enumerate(no_tumor_images):
               if (image_name.split('.')[1] == 'jpg'):
                   image = cv2.imread(image_directory + 'no/' + image_name)
                   image = Image.fromarray(image, 'RGB')
                   image = image.resize((INPUT_SIZE, INPUT_SIZE))  # we are resizing images
                   dataset.append(np.array(image))
                   label.append(0)

           for i, image_name in enumerate(yes_tumor_images):
               if (image_name.split('.')[1] == 'jpg'):
                   image = cv2.imread(image_directory + 'yes/' + image_name)
                   image = Image.fromarray(image, 'RGB')
                   image = image.resize((INPUT_SIZE, INPUT_SIZE))  # we are resizing images
                   dataset.append(np.array(image))
                   label.append(1)

           dataset = np.array(dataset)
           label = np.array(label)

           x_train, x_test, y_train, y_test = train_test_split(dataset, label, test_size=0.2, train_size=0.8
                                                               , random_state=0)
           print(x_train.shape)
           print(y_train.shape)

           print(x_test.shape)
           print(y_test.shape)

           x_train = normalize(x_train, axis=1)
           x_test = normalize(x_train, axis=1)

           y_train = to_categorical(y_train, num_classes=2)
           y_test = to_categorical(y_test, num_classes=2)

           from keras.engine.sequential import Sequential

           model = Sequential()  # Initialising CNN
           model.add(Conv2D(32, (3, 3), input_shape=(INPUT_SIZE, INPUT_SIZE, 3)))  # step -1 Convolution
           model.add(Activation('relu'))
           model.add(MaxPooling2D(pool_size=(2, 2)))  # step -2  Pooling

           model.add(Conv2D(32, (3, 3), kernel_initializer='he_uniform'))
           model.add(Activation('relu'))
           model.add(MaxPooling2D(pool_size=(2, 2)))

           model.add(Conv2D(64, (3, 3), kernel_initializer='he_uniform'))
           model.add(Activation('relu'))
           model.add(MaxPooling2D(pool_size=(2, 2)))

           model.add(Flatten())
           model.add(Dense(64))  #
           model.add(Activation('relu'))
           model.add(Dropout(0.5))
           model.add(Dense(2))
           model.add(Activation('sigmoid'))

           model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
           res = model.fit(np.array(x_train), np.array(y_train), verbose=1, epochs=10,
                           shuffle=False)

           import matplotlib.pyplot as plt

           print(res.history.keys())

           plt.plot(res.history['loss'])
           plt.title('model loss')
           plt.ylabel('loss')
           plt.xlabel('epoch')
           plt.show()

           print("Training accuracy")

           plt.plot(res.history['accuracy'])
           plt.title('Model Accuracy')
           plt.legend(['Training Accuracy'])
           plt.ylabel('Accuracy')
           plt.xlabel('Epoch')
           plt.show()

       def clear(self):
           self.var01.set("")
           self.var02.set("")
           self.var03.set("")
           self.var04.set("")
           self.var05.set("")

       def find(self):
           import webbrowser
           webbrowser.open("https://en.wikipedia.org/wiki/Brain_tumor")

       def search(self):
           conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                        database="pharma")
           mycursor = conn.cursor()
           mycursor.execute("SELECT * FROM tumordetection WHERE PatientID=%s",(self.var02.get(),))

           row = mycursor.fetchall()
           if len(row) != 0:
               self.rtable.delete(*self.rtable.get_children())
               for i in row:
                   self.rtable.insert("", END, values=i)
               conn.commit()
           conn.close()



       def clicked1(self):
           query = self.takecommand().lower()

           if 'youtube' in query:
               speak("opening youtube")

           elif 'wikipedia' in query:
               speak('Searching Wikipedia...')
               query = query.replace("wikipedia", "")
               results = wikipedia.summary(query, sentences=2)
               speak("According to wikipedia")
               speak(results)

               self.rexha = Label(self.root, bd=10, relief=RIDGE,
                                  bg='black', fg="white",
                                  font=("times new roman", 50, "bold"), padx=2, pady=4, height=500)
               self.rexha.place(x=599, y=104, width=280, height=401)

               self.text2 = Text(self.rexha, height=30, width=41, bg="black", fg="white")
               self.text2.config(font=("HELVETICA", 12, "italic"))
               self.text2.pack(side=TOP, fill=X)
               self.text2.insert(END,results)

       def clicked2(self):
           query = self.takecommand().lower()

           imgbrn = Image.open(
               "C:/" + "Users/Aman Kumar/PycharmProjects/pythonProject/pred/" + self.var01.get() + ".jpg")
           imgbrn = imgbrn.resize((220, 400))

           self.photoimgbrn = ImageTk.PhotoImage(imgbrn)
           self.video = Label(self.root, bd=10, relief=RIDGE,
                              bg='black', fg="darkgreen", font=("times new roman", 50, "bold"), image=self.photoimgbrn,
                              padx=2, pady=4, height=500)
           self.video.place(x=880, y=104, width=401, height=401)
           btnref = Button(self.video, text="Refresh", font=("times new roman", 10, "bold italic"), borderwidth=0,bg="black",fg="black",width=280,command=self.refresh)
           btnref.pack(side=BOTTOM)

           import cv2
           from keras.models import load_model
           import numpy as np

           model = load_model('BrainAman.h5')

           image = cv2.imread(
               "C:/" + "Users/Aman Kumar/PycharmProjects/pythonProject/pred/" + self.var01.get() + ".jpg")

           img = Image.fromarray(image)
           img = img.resize((64, 64))
           img = np.array(img)

           input_img = np.expand_dims(img, axis=0)
           predict_x = model.predict(input_img)
           result = np.argmax(predict_x, axis=1)

           if result[0] == 1:
               self.var05.set("Tumor")
               Result = Label(self.root, bd=10, relief=RIDGE, text="Tumor", bg="black", fg="red",
                              font=("times new roman", 38, "bold italic"), anchor="c")
               Result.place(x=881, y=505, width=400, height=150)

           else:
               self.var05.set("No Tumor")
               Result = Label(self.root, bd=10, relief=RIDGE, text="No Tumor", bg="black", fg="red",
                              font=("times new roman", 38, "bold italic"), anchor="c")
               Result.place(x=881, y=505, width=400, height=150)


       def clicked3(self):
           query = self.takecommand().lower()
           conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                        database="pharma")
           mycursor = conn.cursor()
           print(query)
           type(query)
           mycursor.execute("SELECT * FROM tumordetection WHERE PatientID=%s",(query,))

           row = mycursor.fetchall()
           if len(row) != 0:
               self.rtable.delete(*self.rtable.get_children())
               for i in row:
                   self.rtable.insert("", END, values=i)
               conn.commit()
           conn.close()




       def takecommand(self):

           r = sr.Recognizer()
           with sr.Microphone() as source:
               speak("Go Ahead I am Listening")
               audio = r.listen(source)
           try:
               speak("Recognizing")
               query = r.recognize_google(audio, language='en-in')

           except Exception as e:
               speak("Sorry!!Say that again please")
               query = ''

           return query


       def result(self):

           imgbrn = Image.open("C:/"+"Users/Aman Kumar/PycharmProjects/pythonProject/pred/"+self.var01.get() +".jpg")
           imgbrn = imgbrn.resize((220, 400))

           self.photoimgbrn = ImageTk.PhotoImage(imgbrn)
           self.video = Label(self.root, bd=10, relief=RIDGE,
                            bg='black', fg="darkgreen", font=("times new roman", 50, "bold"),image=self.photoimgbrn,
                              padx=2, pady=4,height=500)
           self.video.place(x=880, y=104, width=401, height=401)
           btnref = Button(self.video, text="Refresh", font=("times new roman", 10, "bold italic"), borderwidth=0,bg="black",fg="black",width=280,command=self.refresh)
           btnref.pack(side=BOTTOM)

           import cv2
           from keras.models import load_model
           import numpy as np

           model = load_model('BrainAman.h5')

           image = cv2.imread("C:/"+"Users/Aman Kumar/PycharmProjects/pythonProject/pred/"+self.var01.get() +".jpg")

           img = Image.fromarray(image)
           img = img.resize((64, 64))
           img = np.array(img)

           input_img = np.expand_dims(img, axis=0)
           predict_x = model.predict(input_img)
           result = np.argmax(predict_x, axis=1)

           print(result)

           if result[0]==1:
               self.var05.set("Tumor")
               Result = Label(self.root, bd=10, relief=RIDGE, text="Tumor", bg="black", fg="red",
                              font=("times new roman", 38, "bold italic"), anchor="c")
               Result.place(x=881, y=505, width=400, height=150)

           else:
               self.var05.set("No Tumor")
               Result = Label(self.root, bd=10, relief=RIDGE, text="No Tumor", bg="black", fg="red",
                              font=("times new roman", 38, "bold italic"), anchor="c")
               Result.place(x=881, y=505, width=400, height=150)


       def FetchData(self):

           conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                        database="pharma")
           mycursor = conn.cursor()
           mycursor.execute("SELECT * FROM tumordetection WHERE ReportID=%s",(self.pid.get(),))


           row = mycursor.fetchall()
           if len(row) != 0:
               self.rtable.delete(*self.rtable.get_children())
               for i in row:
                   self.rtable.insert("", END, values=i)
               conn.commit()
           conn.close()


if __name__=="__main__":
    root=Tk()
    obj=BTdetect2(root)
    root.mainloop()
