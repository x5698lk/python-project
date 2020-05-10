from requests import*
from bs4 import*
from tkinter import*

class Reptile(object):
    def __init__(self):
        self.window = Tk()
        self.window.geometry('800x800')
        self.window.title('爬蟲')
        self.frame1 = Frame(self.window)
        self.frame1.pack(side = TOP)
        self.enter_lable = Label(self.frame1,text = '輸入網址')
        self.enter_lable.pack(side =LEFT,fill = BOTH)
        self.scanner1 = Entry(self.frame1)
        self.scanner1.pack(side = LEFT,fill = BOTH)
        self.frame2 = Frame(self.window)
        self.frame2.pack(side = TOP)
        self.enter_lable2 = Label(self.frame2,text = '篩選內容')
        self.enter_lable2.pack(side =LEFT,fill = BOTH)
        self.scanner2 = Entry(self.frame2)
        self.scanner2.pack(side = LEFT,fill = BOTH)
        self.button = Button(text = '開始爬蟲')
        
        self.window.mainloop()


if __name__ == '__main__':
    Reptile()