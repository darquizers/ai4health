from tkinter import *

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

    def invoke(self):
        master = Tk()
        master.title('CanSol')
        e1 = Entry(master)
        e1.grid(row=0, column=1)
        e1.insert(0, "Cancer-Usecase DataSet.csv")
        Button(master, text='Browse',command=self.browse).grid(  row=0,    column=7,   sticky=W,   pady=5)
        Button(master, text='Plot-Accuracy', command=self.plotAccuracy).grid(   row=1,    column=3,   sticky=W,   pady=10)
        Button(master, text='Reset',command=self.reset).grid(row=1,      column=5,   sticky=W,   pady=10)
        Button(master, text='Predict', command=self.predict).grid(row=1, column=7, sticky=W, pady=10)
        canvas = Canvas(width=1000, height=700, bg='white')
        canvas.pack()
        mainloop( )