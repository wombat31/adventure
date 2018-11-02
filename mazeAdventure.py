#Brief: create an adventure game that utilises a Tkinter interface
#and a simple maze
#you use simple commands for input
#you collect items (including a map)
#keys open doors
#you interact with people
from tkinter import *

#Define the interface
window = Tk()
window.title("Adventure")
#Set the size of the window
back = Frame(window, width=480, height=333,bg="black")
back.grid()

contentHolder = Frame(back,width=360,height=311,bg="grey")
contentHolder.grid(row=1,column=1,columnspan=6, rowspan=9)

mazeLabel = Label(contentHolder,text="Maze Adventure")
mazeLabel.grid(row=0,column=0,columnspan=6)

imageSpace = Canvas(contentHolder,bg="white")
imageSpace.grid(row=1,column=0,columnspan=3,rowspan=6)

inputBox = Entry(contentHolder,bg="blue")
inputBox.grid(column=4,row=1,columnspan=3,rowspan=3)


window.mainloop()