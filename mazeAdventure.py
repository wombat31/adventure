#Brief: create an adventure game that utilises a Tkinter interface
#and a simple maze
#you use simple commands for input
#you collect items (including a map)
#keys open doors
#you interact with people
from tkinter import *
#Set up the Dictionary with Locations
locations = {
    1:{
        "name":"location1",
        "east":2
    },
    2:{
        "name":"location2",
        "west":1,
        "east":3
    },
    3:{
        "name":"location3",
        "west":2,
        "north":6
    },
    4:{
        "name":"location4",
        "east":5,
        "north":7
    },
    5:{
        "name":"location5",
        "west":4,
        "north":8
    },
    6:{
        "name":"location6",
        "north":9,
        "south":3
    },
    7:{
        "name":"location7",
        "south":4
    },
    8:{
        "name":"location8",
        "south":5,
        "east":9
    },
    9:{
        "name":"location9",
        "west":8,
        "south":6
    }
}

#Define the message
currentLocation = 2
message = "You are in " + str(currentLocation) + locations[currentLocation]["name"] + "\nWhat do you want to do?"

#Define the interface
window = Tk()
window.title("Adventure")
window.geometry("480x308")

for i in range(8):
    window.columnconfigure(i,minsize=60)
for x in range(11):
    window.rowconfigure(x,minsize=28)

#Set the size of the window
back = Frame(window, width=360, height=308,bg="black",bd=2,relief="solid")
back.grid(row=1,column=1)

for backi in range(6):
    back.columnconfigure(backi,minsize=60)
for backx in range(9):
    back.rowconfigure(backx,minsize=28)
#contentHolder.columnconfigure(0,minsize=80)
#contentHolder.grid(row=1,column=1,columnspan=6, rowspan=9)

mazeLabel = Label(back,text="Maze Adventure",bd=2,relief="solid")
imageSpace = Canvas(back,bg="white",bd=2,relief="solid")
textBox = Label(back,text=message,bg="blue",bd=2,relief="solid")
textEntry = Entry(back,bg="blue",bd=2,relief="solid")

mazeLabel.grid(row=0,column=0,columnspan=6,sticky=E+W+N+S)
imageSpace.grid(row=1,column=0,columnspan=3,rowspan=6)
textBox.grid(column=3,row=1,columnspan=3,rowspan=3,sticky=E+W+N+S)
textEntry.grid(column=0,row=7,rowspan=2,columnspan=6,sticky=E+W+N+S)

#Main game details
textEntry.delete(0,END)
textEntry.insert(0,"Please input your choice")


window.mainloop()