import tkinter
from tkinter import *
from tkinter import messagebox
import time



time.sleep(2)
class MusicPlayer:
    def __init__(self, window ):
        window.geometry('428x80'); window.title('Music Player (v1.0)'); window.resizable(0,0)
        
        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
        Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);Stop.place(x=330,y=20)
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
        
root = Tk()
app= MusicPlayer(root)


l=[]
c=1
def entryError() :

  if insertField.get() == "" :


    messagebox.showerror("Error in input. Please input again")

    return 0

  return 1
def insertTask():
  global c

  value = entryError()
  if (value == 0):
    return
  var=insertField.get()+"\n"
  l.append(var)
  TextArea.insert('end -1 chars', str(c) + "---> " + var)
  c=c+1
  del_tf()
def del_nf() :

  nf.delete(0.0, END)
def del_tf() :
  insertField.delete(0, END)

def delete() :

  global c

  if (len(l)==0):
    messagebox.showerror("There are no tasks")
    return
  number = nf.get(1.0, END)
  if (number=="\n"):
    messagebox.showerror("input error")
    return
  else :
    task_no = int(number)
  del_nf()

  l.pop(task_no - 1)
  c=c-1

  TextArea.delete(1.0, END)
  for i in range(len(l)):
    TextArea.insert('end -1 chars',str(i + 1) + "---> " + l[i])

if (__name__ == "__main__"):
  window = Tk()
  window.configure(background = "white")
  window.title("To-Do List (v1.4)")
  window.resizable(0,0)
  window.geometry("387x300")
  enterTask = Label(window, text = "Please enter your task", bg="white")
  insertField = Entry(window)

  Submit = Button(window, text = "Submit", fg = "Black", bg = "light green", command = insertTask)
  TextArea = Text(window, height = 4, width = 36, font = "arial 13")
  taskNumber = Label(window, text = "Specify below the task number that you want to remove", bg = "white")

  nf = Text(window, height = 1, width = 36, font = "arial 13")

  delete = Button(window, text = "Delete", fg = "Black", bg = "orange", command = delete)

  Exit = Button(window, text = "Do you want to exit?", fg = "Black", bg = "Red", command = exit)
  enterTask.grid(row = 0, column = 2)
  insertField.grid(row = 1, column = 2, ipadx = 50)
  Submit.grid(row = 2, column = 2)
  TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
  taskNumber.grid(row = 4, column = 2, pady = 5)
  nf.grid(row = 5, column = 2)
  delete.grid(row = 6, column = 2, pady = 5)
  Exit.grid(row = 7, column = 2)
  
  

  window.mainloop()
