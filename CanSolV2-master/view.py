from tkinter import *


class UI:
    #browses the raw data set.
    def browse(self):
        print("Clicked :::browsing and selecting raw data the UI....")

    #renders the plot( confusion graph) and Accuracy
    def plotConfusion(self):
        print("Clicked :::confusion accuracy % & plotting based on trained deployed data...")

    # renders the plot( confusion graph) and Accuracy
    def plotAccuracy(self):
        print("Clicked :::predicting accuracy % & plotting based on trained deployed data...")

    #renders the Benign Malignant confidence score based on the engine
    def predict(self):
        print("Clicked :::predicting Malignant - Benign confidence score on UI")

    # resets the plot and accuracy
    def reset(self):
        #canvas.delete("all")
        #canvas.create_text(110, 150, fill="darkblue", font="Times 15 italic bold",text="\n Your Plot Accuracy \nwill \ndisplay here",anchor=CENTER,justify=CENTER)
        #canvas.delete("all")
        print("Clicked :::reseting plot and accuracy from UI...")


    def invoke(self):
        master = Tk()
        master.geometry('800x700')
        master.title('CanSol')
        master.configure(background="white")
        label_one = Label(master, text='CanSol', fg='#00004d', bg='white')
        label_one.config(font=("Times", 30, "bold italic"))

        label_one.place(x=220, y=20)
        e1 = Entry(master, bd='2')
        e1.place(x=40, y=100, width=360, height=30)

        e1.insert(0, "Cancer-Usecase DataSet.csv")
        BrowseBtn = Button(master, text='Browse', command=self.browse, bg='#00004d', fg='white')
        BrowseBtn.place(x=410, y=100, width=120, height=30)
        resetBtn = Button(master, text='Reset', command=self.reset, bg='#00004d', fg='white')
        resetBtn.place(x=540, y=100, width=120, height=30)
        PlotAcc = Button(master, text='Plot-Accuracy', command=self.plotAccuracy, bg='#00004d', fg='white')
        PlotAcc.place(x=410, y=150, width=120, height=30)
        confusionBtn = Button(master, text='Confusion Matrix', command=self.plotConfusion, bg='#00004d',fg='white')
        confusionBtn.place(x=540, y=150, width=120, height=30)
        predictBtn = Button(master, text='Predict', command=self.predict, bg='#00004d', fg='white')
        predictBtn.place(x=540, y=540, width=60, height=30)
        canvas1 = Canvas(master, bg='white')

        photo1 = PhotoImage(file='confusion.png')
        
        canvas1.create_image(0, 0, image=photo1, anchor='nw')
        canvas1.grid(row=0, column=0)
        canvas2 = Canvas(master, bg='white')

        photo2 = PhotoImage(file='prediction.png', width=320, height=340)

        canvas1.place(x=40, y=150, width=350, height=380)
        canvas2.place(x=410, y=190, width=320, height=340)
        # canvas2.pack(expand=True, fill="both")
        canvas2.create_image(0, 0, image=photo2, anchor='nw')
        mainloop( )