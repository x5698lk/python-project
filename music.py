import pygame
from tkinter import*

class music():
    def __init__(self):
        self.state = True
        self.song_name = NONE
        self.volume = 1.0
        self.window = Tk()
        self.window.title("音樂播放器")
        self.window.resizable(width=False, height=False)

        self.lable = Label(self.window)
        self.lable.pack(side = TOP,fill = BOTH)
        self.butStart = Button(self.lable,text='音樂播放',command= self.start_pause,font=('Arial', 20))
        self.butStart.pack(side = LEFT)
        self.butReplay = Button(self.lable,text='重新播放',command = self.replay,font=('Arial', 20))
        self.butReplay.pack(side = LEFT)
        self.butloud = Button(self.lable,text='大聲',command = self.loud,font=('Arial', 20))
        self.butloud.pack(side = LEFT)
        self.butlow = Button(self.lable,text='小聲',command = self.low,font=('Arial', 20))
        self.butlow.pack(side = LEFT)

        self.entry_hint = Label(self.window,font=('Arial',15),text = 'Enter music position below',bg = 'orange')
        self.entry_hint.pack(side = TOP,fill = BOTH)

        self.enter_songname = Button(self.window,text = 'Enter',command = self.music_set,font=('Arial',15),bg = 'yellow')
        self.enter_songname.pack(side = LEFT,fill = BOTH)
        self.entry = Entry(self.window,font=('Arial',25),bg = 'gray')
        self.entry.pack(side = RIGHT,fill = BOTH)

        self.window.mainloop()

    def music_set(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.load('Anchor-Iris.mp3')
        pygame.mixer.music.play()

    def start_pause(self):
        if self.state ==False:
            self.state = True
            pygame.mixer.music.unpause()
            return
        elif self.state == True:
            self.state = False
            pygame.mixer.music.pause()
            return

    def replay(self):
        pygame.mixer.music.load('Anchor-Iris.mp3')
        pygame.mixer.music.play()
        
    def loud(self):
        self.volume = self.volume+0.05
        if self.volume>1.0:
            self.volume = 1.0
        pygame.mixer.music.set_volume(self.volume)

    def low(self):
        self.volume = self.volume-0.05
        if self.volume<0.0:
            self.volume = 0.0
        pygame.mixer.music.set_volume(self.volume)

if __name__ == '__main__':
    music()

