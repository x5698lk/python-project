from tkinter import *


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

        ##紀錄棋盤陣列
        self.matrix = [[0 for y in range(self.column+1)]for x in range(self.row+1)]
        self.last_step = NONE

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
        self.matrix = [[0 for y in range(self.column+1)]for x in range(self.row+1)]
        self.last_step = NONE
        self.btn_state("start")
        self.is_start = True
        self.is_black = True
        self.board.delete(ALL)
        self.drawmesh()
        self.lablePlayer.config(text="黑方下棋")

    def restart(self):
        self.start()

    ##悔棋功能
    def reget(self):
        if self.last_step == NONE :
            self.lablePlayer.config(text="不能悔棋")
        self.draw_block()
        self.last_step = NONE
        self.is_black = not self.is_black
        text = self.ternary_operator("黑方下棋", "白方下棋")
        self.lablePlayer.config(text=text)
    
    ##悔棋去除棋子
    def draw_block(self):
        x,y = self.last_step
        self.board.create_rectangle(x*self.mesh-self.chess_r,y*self.mesh-self.chess_r,x*self.mesh+self.chess_r,y*self.mesh+self.chess_r, fill = '#CDBA96' , outline = '#CDBA96')
        self.board.create_line(x*self.mesh-self.chess_r,y*self.mesh,x*self.mesh+self.chess_r+0.5,y*self.mesh,width = 2)
        self.board.create_line(x*self.mesh,y*self.mesh-self.chess_r,x*self.mesh,y*self.mesh+self.chess_r+0.5,width = 2)
        self.matrix[x][y] = 0

    def surrender(self):
        self.btn_state("init")
        self.is_start = False
        text = self.ternary_operator("黑方認輸", "白方認輸")
        self.lablePlayer.config(text=text)


    ##畫棋子
    def gamechess(self,event):
        x = int(event.x/self.mesh+0.5)
        y = int(event.y/self.mesh+0.5)
        if x<0.5 or x>(self.row+0.5) or y<0.5 or y>(self.column+0.5) or self.matrix[x][y]!=0 or not self.is_start:
            return
        tag = self.ternary_operator("1","-1")
        self.matrix[x][y] = tag
        self.last_step = [x,y]
        color = self.ternary_operator("black", "white")
        self.drawchess(x*self.mesh, y*self.mesh, color)
        if self.win(x,y,tag):
            self.is_start = False
            self.btn_state("init")
            text = self.ternary_operator("黑方獲勝","白方獲勝")
            self.lablePlayer.config(text = text)
            return
        self.trans_identify()
        
    ##判斷輸贏演算法(先抄)
    def win(self,x,y,tag):
        def direction(i, j, di, dj, row, column, matrix):
            temp = []
            while 0 <= i < row and 0 <= j < column:
                i, j = i + di, j + dj
            i, j = i - di, j - dj
            while 0 <= i < row and 0 <= j < column:
                temp.append(matrix[i][j])
                i, j = i - di, j - dj
            return temp
 
        four_direction = []
        four_direction.append([self.matrix[i][y] for i in range(self.row)])
        four_direction.append([self.matrix[x][j] for j in range(self.column)])
        four_direction.append(direction(x, y, 1, 1, self.row, self.column, self.matrix))
        four_direction.append(direction(x, y, 1, -1, self.row, self.column, self.matrix))
 
        for v_list in four_direction:
            count = 0
            for v in v_list:
                if v == tag:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0
        return False
        
   

if __name__ == '__main__':
    Chess()