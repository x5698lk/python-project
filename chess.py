from tkinter import *
from tkinter.messagebox import *


class Chess(object):
    def __init__(self):
    #數值設定
        ##棋盤行列設定
        self.row = 15
        self.column = 15

        ##網格大小
        self.mesh = 40

        ##棋子半徑
        self.chess_r = 15

        ##初始化按鈕狀態
        self.is_start = False

        ##初始化棋子顏色及玩家
        self.is_black = True

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
        self.butStart = Button(self.header,text='開始',font=('Arial', 20),bg = '#f0e68c',width = 8,bd = 10,command = self.start)
        self.butStart.pack(side = LEFT)

        self.butRestart = Button(self.header,text='重新',font=('Arial', 20),bg = '#f0e68c',width = 8,bd = 10,command = self.restart,state = DISABLED)
        self.butRestart.pack(side = LEFT)

        self.lablePlayer = Label(self.header,text='未開始',font=('Arial', 20),bg = '#8fbc8f',width = 8,bd = 10)
        self.lablePlayer.pack(side = LEFT)

        self.butReget = Button(self.header,text='悔棋',font=('Arial', 20),bg = '#f0e68c',width = 8,bd = 10,command = self.reget,state = DISABLED)
        self.butReget.pack(side = LEFT)

        self.butSurrender = Button(self.header,text='認輸',font=('Arial', 20),bg = '#f0e68c',width = 8,bd = 10,command = self.surrender,state = DISABLED)
        self.butSurrender.pack(side = LEFT)

        ##棋盤畫布建立
        self.board = Canvas(self.window,width = (self.column+1)*self.mesh, height = (self.row+1)*self.mesh,bg = '#CDBA96')
        self.drawmesh()
        self.board.bind("<Button-1>",self.gamechess)
        self.board.pack()

        ##執行tkinter迴圈
        self.window.mainloop()

#定義函式
    ##判斷黑白用
    def ternary_operator(self, true, false):
        return true if self.is_black else false


    ##交換棋手
    def trans_identify(self):
        self.is_black = not self.is_black
        text = self.ternary_operator("黑方下棋", "白方下棋")
        self.lablePlayer.config(text=text)

    ##畫網格
    def drawmesh(self):
        for num in range(1,self.row+1):
            self.board.create_line(num*self.mesh,self.mesh,num*self.mesh,(self.column)*self.mesh,width=2)
        for num in range(1,self.column+1):
            self.board.create_line(self.mesh,num*self.mesh,(self.row)*self.mesh,num*self.mesh,width=2)

    ##畫棋子
    def drawchess(self, x, y, color):
        self.board.create_oval(x - self.chess_r, y - self.chess_r, x + self.chess_r, y + self.chess_r,fill=color)

    ##設定按鈕狀態
    def btn_state(self, state):
        if state == "init":
            self.butStart.config(state=NORMAL)
            self.butRestart.config(state=DISABLED)
            self.butReget.config(state=DISABLED)
            self.butSurrender.config(state=DISABLED)
        else :
            self.butStart.config(state=DISABLED)
            self.butRestart.config(state=NORMAL)
            self.butReget.config(state=NORMAL)
            self.butSurrender.config(state=NORMAL)

    ##按鈕功能函式
    def start(self):
        self.btn_state("start")
        self.is_start = True
        self.is_black = True
        self.board.delete(ALL)
        self.drawmesh()
        self.lablePlayer.config(text="黑方下棋")

    def restart(self):
        self.start()

    ##悔棋功能(還沒寫)
    def reget(self):
        self.is_black = not self.is_black
        text = self.ternary_operator("黑方下棋", "白方下棋")
        self.lablePlayer.config(text=text)

    def surrender(self):
        self.btn_state("init")
        self.is_start = False
        text = self.ternary_operator("黑方認輸", "白方認輸")
        self.lablePlayer.config(text=text)

    ##畫棋子(座標化還沒寫)
    def gamechess(self,event):
        if not self.is_start:
            return
        x = event.x
        y = event.y
        color = self.ternary_operator("black", "white")
        self.drawchess(x, y, color)
        self.trans_identify()
    
    ##判斷輸贏演算法(還沒寫)
    def win(self):
        return 0
        
   

if __name__ == '__main__':
    Chess()