from tkinter import *
import random

colours = ["Red", "Yellow", "Green", "Blue", "White", "Black", "Brown", "Purple"]

score = 0
time = 30

def startGame(event):

    if time == 30:
        countdown()

    nextColour()


def nextColour():

    global score
    global time

    if time > 0:

        colourEntry.focus_set()

        if colourEntry.get().lower()==colours[1].lower():
            score += 1

        colourEntry.delete(0, END)

        random.shuffle(colours)

        colour.config(fg=str(colours[1]), text = str(colours[0]))
        scoreLabel.config(text="Score: "+str(score))
    
def countdown():

    global time

    if time > 0:

        time -= 1
        timeLabel.config(text = "Time left: "+str(time))
        timeLabel.after(1000, countdown)

if __name__ == '__main__':
    
    root = Tk()

    root.title('Colour Game')
    root.geometry('500x300')
    
    instruction = Label(root, text = 'Type the colour of the word, and not the text!!\nhit ENTER to start', font = ("Helvetica", 15))
    instruction.pack()

    scoreLabel = Label(root, text = 'Score :'+ str(score), font = ("Helvetica", 15))
    scoreLabel.pack()

    timeLabel = Label(root, text = 'Time Left :'+ str(time), font = ("Helvetica", 15))
    timeLabel.pack()

    colour = Label(font = ("Helvetica", 17,"bold"))
    colour.pack()

    colourEntry = Entry(root, bd= "3px", font=("Helvetica", 15))
    colourEntry.focus_set()
    root.bind('<Return>', startGame)
    colourEntry.pack()

    root.mainloop()