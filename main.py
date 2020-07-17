from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title('Learn To Code at Codemy')
root.geometry("600x300")
root.resizable(width=False, height=False)


rock = ImageTk.PhotoImage(Image.open("rock.png"))
paper = ImageTk.PhotoImage(Image.open("paper.png"))
scissors = ImageTk.PhotoImage(Image.open("scissors.png"))

image_list = [rock, paper, scissors]


myLabel1 = Label(root, text=image_list)
mylabel44 = Label(root, text="")
mylabel44.grid(row=0, column=1)

def mix1():
    global myLabel1
    text = random.choice(image_list)
    myLabel1.grid_forget()
    myLabel1.destroy()
    myLabel1 = Label(root, image=text)
    myLabel1.grid(row=0, column=0)
    return text


def mix2():
    global myLabel2

    user_choice = random.choice(image_list)
    myLabel2.grid_forget()
    myLabel2.destroy()
    myLabel2 = Label(root, image=user_choice)
    myLabel2.grid(row=0, column=2)
    mix1()

    winwin(user_choice)

score1 = 0
score2 = 0
w_label = Label(root, text="")
user1_score = Label(root, text=score1)
user2_score = Label(root, text=score2)


def winwin(text):
    global w_label
    global score1
    global score2
    global user1_score
    global user2_score
    oyuncu1 = mix1()
    oyuncu2 = text


    w_label.grid_forget()
    w_label.destroy()


    if oyuncu1 == oyuncu2:
        w_label = Label(root, text="Draw")
        w_label.grid(row=4, column=1)
        w_label.place(x=250, y=250)
    elif oyuncu1 == image_list[0] and oyuncu2 == image_list[2]:
        w_label = Label(root, text="Player 1 win")
        w_label.grid(row=4, column=1)
        w_label.place(x=250, y=250)
        score1 += 1
        user1_score = Label(root, text=score1)
        user1_score.grid(row=5, column=0)
    elif oyuncu1 == image_list[0] and oyuncu2 == image_list[1]:
        w_label = Label(root, text="Player 2 win")
        w_label.grid(row=4, column=1)
        w_label.place(x=250, y=250)
        score2 += 1
        user2_score = Label(root, text=score2)
        user2_score.grid(row=5, column=2)
    elif oyuncu1 == image_list[2] and oyuncu2 == image_list[0]:
        w_label = Label(root, text="Player 2 win")
        w_label.grid(row=4, column=1)
        w_label.place(x=250, y=250)
        score2 += 1
        user2_score = Label(root, text=score2)
        user2_score.grid(row=5, column=2)
    elif oyuncu1 == image_list[1] and oyuncu2 == image_list[2]:
        w_label = Label(root, text="Player 2 win")
        w_label.grid(row=4, column=1)
        w_label.place(x=250, y=250)
        score2 += 1
        user2_score = Label(root, text=score2)
        user2_score.grid(row=5, column=2)
    elif oyuncu1 == image_list[1] and oyuncu2 == image_list[0]:
        w_label = Label(root, text="Player 1 win")
        w_label.grid(row=4, column=1)
        w_label.place(x=250, y=250)
        score1 += 1
        user1_score = Label(root, text=score1)
        user1_score.grid(row=5, column=0)
    elif oyuncu1 == image_list[2] and oyuncu2 == image_list[1]:
        w_label = Label(root, text="Player 1 win")
        w_label.grid(row=4, column=1)
        w_label.place(x=250, y=250)
        score1 += 1
        user1_score = Label(root, text=score1)
        user1_score.grid(row=5, column=0)
    else:
        print("Game Over")




myLabel2 = Label(root, text="")
myLabel2.grid(row=0, column=1)




def play():

    global score1
    global score2
    restartButton = Button(root, text="RESTART", command=play)
    #startButton.grid_forget()
    startButton.destroy()       
    restartButton.grid_forget()
    restartButton.destroy()

    for i in range(0,100):

        mybutton2 = Button(root, text="PLAY", command=mix2)
        #mybutton2.grid(row=3, column=1)
        #mybutton2.place(x=250, y=225)

        mybutton2.invoke()

        if score1 == 10:
            print("Game Over")
            score1 = 0
            score2 = 0
            restartButton = Button(root, text="RESTART", command=play)
            restartButton.grid(row=3, column=1)
            restartButton.place(x=250, y=225)
            break
        elif score2 == 10:
            print("Game Over")
            score1 = 0   
            score2 = 0   
            restartButton = Button(root, text="RESTART", command=play)
            restartButton.grid(row=3, column=1)
            restartButton.place(x=250, y=225)
            break
        else:
            continue



startButton = Button(root, text="START", command=play)
startButton.grid(row=3, column=1)
startButton.place(x=250, y=225)

root.mainloop()