from tkinter import*

class Chess(object):
    def __init__(self,row = None,column = None,mesh = None):
        self.row = row
        self.column = column
        self.mesh = mesh

    #GUI
        ##視窗建立
        self.window = Tk()
        self.window.title = ("五子棋小遊戲")
        self.window.resizable(width=False, height=False)
        self.window.configure(background='#4682b4')

        ##設定按鈕區塊(LABLE)
        self.header = Label(self.window,font=('Arial',25),bg = '#8fbc8f')
        self.header.pack(fill = BOTH)

        ##按鈕建立
        self.butStart = Button(self.header,text='開始',font=('Arial', 20),bg = '#f0e68c',width = 8,bd = 10)
        self.butStart.pack(side = LEFT)

        self.butRestart = Button(self.header,text='重新',font=('Arial', 20),bg = '#f0e68c',width = 8,bd = 10)
        self.butRestart.pack(side = LEFT)

        self.lablePlayer = Label(self.header,text='未開始',font=('Arial', 20),bg = '#8fbc8f',width = 8,bd = 10)
        self.lablePlayer.pack(side = LEFT)

        self.butReget = Button(self.header,text='悔棋',font=('Arial', 20),bg = '#f0e68c',width = 8,bd = 10)
        self.butReget.pack(side = LEFT)

        self.butSurrender = Button(self.header,text='認輸',font=('Arial', 20),bg = '#f0e68c',width = 8,bd = 10)
        self.butSurrender.pack(side = LEFT)
        board(15,15,40)
        ##執行tkinter迴圈
        self.window.mainloop()

class board(Chess):
    def __init__(self,row,column,mesh):
        self.row = row
        self.column = column
        self.mesh = mesh
        self.window = Tk()
        self.board = Canvas(self.window,width = (self.column+1)*self.mesh, height = (self.row+1)*self.mesh,bg = '#CDBA96')
        self.board.pack()


if __name__ == '__main__':
    Chess()