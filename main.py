from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title('Learn To Code at Codemy')
# root.geometry("1000x1000")
root.resizable(width=False, height=False)


rock = ImageTk.PhotoImage(Image.open("C:/Users/Serhat/Documents/GitHub/Rock-Paper-Scissors/Images/rock.png"))
paper = ImageTk.PhotoImage(Image.open("C:/Users/Serhat/Documents/GitHub/Rock-Paper-Scissors/Images/paper.png"))
scissors = ImageTk.PhotoImage(Image.open("C:/Users/Serhat/Documents/GitHub/Rock-Paper-Scissors/Images/scissors.png"))

image_list = [rock, paper, scissors]


myLabel1 = Label(root, text=image_list)


def mix1():
    global myLabel1
    random.shuffle(image_list)
    myLabel1.grid_forget()
    myLabel1.destroy()
    myLabel1 = Label(root, image=image_list[0])
    myLabel1.grid(row=0, column=0)
    text = image_list[0]
    return text


def mix2():
    global myLabel2

    random.shuffle(image_list)
    myLabel2.grid_forget()
    myLabel2.destroy()
    myLabel2 = Label(root, image=image_list[0])
    myLabel2.grid(row=0, column=1)
    mix1()
    text = image_list[0]

    winwin(text)


def winwin(text):
    oyuncu1 = mix1()
    oyuncu2 = text

    w_label = Label(root, text="")
    w_label.grid_forget()
    w_label.destroy()

    print(oyuncu1)

    if oyuncu1 == oyuncu2:
        w_label = Label(root, text="Berabere")
        w_label.grid(row=4, column=1)
    elif oyuncu1 == "pyimage1" and oyuncu2 == "pyimage3":
        w_label = Label(root, text="1. oyuncu kazandı")
        w_label.grid(row=4, column=1)
    elif oyuncu1 == "pyimage1" and oyuncu2 == "pyimage2":
        w_label = Label(root, text="2. oyuncu kazandı")
        w_label.grid(row=4, column=1)
    elif oyuncu1 == "pyimage2" and oyuncu2 == "pyimage3":
        w_label = Label(root, text="2. oyuncu kazandı")
        w_label.grid(row=4, column=1)
    elif oyuncu1 == "pyimage2" and oyuncu2 == "pyimage1":
        w_label = Label(root, text="1. oyuncu kazandı")
        w_label.grid(row=4, column=1)
    elif oyuncu1 == "pyimage3" and oyuncu2 == "pyimage2":
        w_label = Label(root, text="1. oyuncu kazandı")
        w_label.grid(row=4, column=1)
    else:
        print("oyun bitti")


myLabel2 = Label(root, text="user choose field")
myLabel2.grid(row=0, column=1)

# mybutton1 = Button(root, text="1. yi Değiştir", command=mix1)
# mybutton1.grid(row=3, column=0)

mybutton2 = Button(root, text="OYNA", command=mix2)
mybutton2.grid(row=3, column=0)



root.mainloop()