from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title('Learn To Code at Codemy')
root.geometry("600x300")
root.resizable(width=False, height=False)


rock = ImageTk.PhotoImage(Image.open("C:/Users/Serhat/Documents/GitHub/Rock-Paper-Scissors/Images/rock.png"))
paper = ImageTk.PhotoImage(Image.open("C:/Users/Serhat/Documents/GitHub/Rock-Paper-Scissors/Images/paper.png"))
scissors = ImageTk.PhotoImage(Image.open("C:/Users/Serhat/Documents/GitHub/Rock-Paper-Scissors/Images/scissors.png"))

image_list = [rock, paper, scissors]


myLabel1 = Label(root, text=image_list)
mylabel44 = Label(root, text="")
mylabel44.grid(row=0, column=1)

def mix1():
    global myLabel1
    text = random.choice(image_list)
    myLabel1.grid_forget()
    myLabel1.destroy()
    #myLabel1 = Label(root, image=image_list[0])
    myLabel1 = Label(root, image=text)
    myLabel1.grid(row=0, column=0)
    #text = image_list[0]
    return text


def mix2():
    global myLabel2

    user_choice = random.choice(image_list)
    myLabel2.grid_forget()
    myLabel2.destroy()
    #myLabel2 = Label(root, image=image_list[0])
    myLabel2 = Label(root, image=user_choice)
    myLabel2.grid(row=0, column=2)
    mix1()
    #text = image_list[0]

    winwin(user_choice)

w_label = Label(root, text="")


def winwin(text):
    global w_label
    oyuncu1 = mix1()
    oyuncu2 = text


    w_label.grid_forget()
    w_label.destroy()

    # print(oyuncu1)
    # print(oyuncu2)
    # print(image_list[0])
    # print(image_list[1])
    # print(image_list[2])

    if oyuncu1 == oyuncu2:
        w_label = Label(root, text="Draw")
        w_label.grid(row=4, column=1)
        w_label.place(x=250, y=250)
    elif oyuncu1 == image_list[0] and oyuncu2 == image_list[2]:
        w_label = Label(root, text="Player 1 win")
        w_label.grid(row=4, column=1)
        w_label.place(x=250, y=250)
    elif oyuncu1 == image_list[0] and oyuncu2 == image_list[1]:
        w_label = Label(root, text="Player 2 win")
        w_label.grid(row=4, column=1)
        w_label.place(x=250, y=250)
    elif oyuncu1 == image_list[2] and oyuncu2 == image_list[0]:
        w_label = Label(root, text="Player 2 win")
        w_label.grid(row=4, column=1)
        w_label.place(x=250, y=250)
    elif oyuncu1 == image_list[1] and oyuncu2 == image_list[2]:
        w_label = Label(root, text="Player 2 win")
        w_label.grid(row=4, column=1)
        w_label.place(x=250, y=250)
    elif oyuncu1 == image_list[1] and oyuncu2 == image_list[0]:
        w_label = Label(root, text="Player 1 win")
        w_label.grid(row=4, column=1)
        w_label.place(x=250, y=250)
    elif oyuncu1 == image_list[2] and oyuncu2 == image_list[1]:
        w_label = Label(root, text="Player 1 win")
        w_label.grid(row=4, column=1)
        w_label.place(x=250, y=250)
    else:
        print("Game Over")


myLabel2 = Label(root, text="")
myLabel2.grid(row=0, column=1)



mybutton2 = Button(root, text="PLAY", command=mix2)
mybutton2.grid(row=3, column=1 )


mybutton2.place(x=250, y=225)

root.mainloop()