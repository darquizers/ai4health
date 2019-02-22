from tkinter import *
#import pandas as pd
class UI:
    #browses the raw data set.
    def browse(self):
        print("Clicked :::browsing and selecting raw data the UI....")

    #renders the plot( confusion graph) and Accuracy
    def plotAccuracy(self):
        print("Clicked :::predicting accuracy % & plotting based on trained deployed data...")

     #renders the Benign Malignant confidence score based on the engine
    def predict(self):
        print("Clicked :::predicting Malignant - Benign confidence score on UI")

    # resets the plot and accuracy
    def reset(self):
        print("Clicked :::reseting plot and accuracy from UI...")

    def confusionmatrix(self):
        print("Clicked :::confusion plot and accuracy from UI...")


    def invoke(self):
        master = Tk()
        master.geometry('1920x1080')
        master.title('CanSol')
        master.configure(background="white")
        label_one = Label(master, text = 'CanSol',fg='#00004d',bg='white')
        label_one.config(font=("Times", 30,"bold italic"))

        label_one.place(x=500,y=20)
        e1 = Entry(master,bd='3')
        e1.place(x=40,y=100,width=360,height=30)

        e1.insert(0, "Cancer-Usecase DataSet.csv")
        BrowseBtn=Button(master, text='Browse',command=self.browse,bg='#00004d',fg='white')
        BrowseBtn.place(x=410,y=100,width=120,height=30)
        resetBtn = Button(master, text='Reset', command=self.reset ,bg='#00004d', fg='white')
        resetBtn.place(x=540, y=100, width=120, height=30)
        PlotAcc=Button(master, text='Plot-Accuracy', command=self.plotAccuracy,bg='#00004d',fg='white')
        PlotAcc.place(x=800, y=100, width=120,height=30)
        confusionBtn=Button(master, text='Confusion Matrix',command=self.confusionmatrix,bg='#00004d',fg='white')
        confusionBtn.place(x=540, y=100, width=120,height=30)
        predictBtn=Button(master, text='Predict', command=self.predict,bg='#00004d',fg='white')
        predictBtn.place(x=670, y=100, width=120, height=30)

        canvas1 = Canvas(master,bg='white')
        photo1 = PhotoImage(file='asis.png',width=320,height=340)
        canvas1.create_image(0, 0, image=photo1,anchor='nw')
        canvas1.grid(row=0, column=0)
        canvas1.place(x=40, y=150, width=350, height=380)

        canvas2 = Canvas(master, bg='white')
        photo2 = PhotoImage(file='confusion.png',width=320,height=340)
        canvas2.place(x=410, y=150, width=350, height=380)
        canvas2.create_image(0, 0, image=photo2,anchor='nw')

        canvas3 = Canvas(master, bg='white')
        photo3 = PhotoImage(file='prediction.png', width=320, height=340)
        canvas3.create_image(0, 0, image=photo3, anchor='nw')
        canvas3.grid(row=0, column=0)
        canvas3.place(x=800, y=150, width=350, height=380)


        #canvas.delete("all")
        #canvas.create_text(110, 150, fill="darkblue", font="Times 15 italic bold",text="\n Your Plot Accuracy \nwill \ndisplay here",anchor=CENTER,justify=CENTER)

        #canvas.delete("all")

        #for i in range(900):
        #    for j in range(4):
        #        l = Label(text='%d.%d' % (i, j), relief=RIDGE)
        #       l.grid(row=i, column=j, sticky=NSEW)
        #canvas.create_text(40, 120, text=var, font=("Courier New", 5))
        #text = Label(text="Text")  # included to show background color

        mainloop()

a=UI()
a.invoke()