from tkinter import *

class UI:
    def browse(self):
        print("Clicked :::browsing and selecting raw data the UI....")

    def train(self):
        print("Clicked :::training data using Scikit....")

    def accuracy(self):
        print("Clicked :::rendering accuracy/ploting based on trained deployed data....")

    def predict(self):
        print("Clicked :::predicting/plotting based on trained deployed data...")

    def invoke(self):
        master = Tk()
        master.title='Cansol'
        e1 = Entry(master)
        e1.grid(row=0, column=1)
        e1.insert(0, "Cancer-Usecase DataSet.csv")
        Button(master, text='Browse',command=self.browse).grid(row=0, column=2, sticky=W, pady=2)
        Button(master, text='Train', command=self.train).grid(row=1, column=0, sticky=W, pady=2)
        Button(master, text='Deploy',command=self.accuracy).grid(row=1, column=1, sticky=W, pady=2)
        mainloop( )