from tkinter import *
from PIL import Image, ImageTk
from random import randint

def open_main_window():
    play_window.destroy()  # Destroy the play window
    # main window
    root = Tk()
    root.title("rock paper scissor")
    root.configure(background="#7171C6")
    root.geometry("940x400")

    # pictures
    rock_image = ImageTk.PhotoImage(Image.open(r"C:\Users\kazim\Downloads\rock-user.png"))
    paper_image = ImageTk.PhotoImage(Image.open(r"C:\Users\kazim\Downloads\paper-user.png"))
    scissor_image = ImageTk.PhotoImage(Image.open(r"C:\Users\kazim\Downloads\scissors-user.png"))
    rock_image_comp = ImageTk.PhotoImage(Image.open(r"C:\Users\kazim\Downloads\rock.png"))
    paper_image_comp = ImageTk.PhotoImage(Image.open(r"C:\Users\kazim\Downloads\paper.png"))
    scissor_image_comp = ImageTk.PhotoImage(Image.open(r"C:\Users\kazim\Downloads\scissors.png"))

    # insert picture
    user_label = Label(root, image=scissor_image, bg="#7171C6")
    comp_label = Label(root, image=scissor_image_comp, bg="#7171C6")
    comp_label.grid(row=1, column=0)
    user_label.grid(row=1, column=4)

    # scores
    userscore = Label(root, text=0, font=("Helvetica", 20, "bold"), bg="#7171C6", fg="white")
    compscore = Label(root, text=0, font=("Helvetica", 20, "bold"), bg="#7171C6", fg="white")
    compscore.grid(row=1, column=1)
    userscore.grid(row=1, column=3)

    # indicators
    user_indicator = (Label(root, text="USER", font=("Helvetica", 20, "bold"), bg="#7171C6", fg="white")
                      .grid(row=0, column=3))
    comp_indicator = (Label(root, font=("Helvetica", 20, "bold"), text="COMPUTER", bg="#7171C6", fg="white")
                      .grid(row=0, column=1))

    # messages
    msg = (Label(root, font=50, bg="#7171C6", fg="white"))
    msg.grid(row=3, column=2)

    # update message
    def updatemessage(x):
        msg['text'] = x
        msg.config(text=x, font=("Helvetica", 14, "bold"))

    # update user score
    def updateuserscore():
        score = int(userscore["text"])
        score += 1
        userscore["text"] = str(score)

    def updatecompscore():
        score = int(compscore["text"])
        score += 1
        compscore["text"] = str(score)

    # check winner
    def checkwin(player, computer):
        if player == computer:
            updatemessage("It's a Tie!!!")
        elif player == "rock":
            if computer == "paper":
                updatemessage("You Loose!!!")
                updatecompscore()
            else:
                updatemessage("You Win!!!")
                updateuserscore()
        elif player == "paper":
            if computer == "scissor":
                updatemessage("You Loose!!!")
                updatecompscore()
            else:
                updatemessage("You Win!!!")
                updateuserscore()
        elif player == "scissor":
            if computer == "rock":
                updatemessage("You Loose!!!")
                updatecompscore()
            else:
                updatemessage("You Win!!!")
                updateuserscore()
        else:
            pass

    # update choices
    choices = ("rock", "paper", "scissor")

    def updatechoice(x):
        # for computer
        compchoice = choices[randint(0, 2)]
        if compchoice == "rock":
            comp_label.configure(image=rock_image_comp)
        elif compchoice == "paper":
            comp_label.configure(image=paper_image_comp)
        else:
            comp_label.configure(image=scissor_image_comp)
        # for user
        if x == "rock":
            user_label.configure(image=rock_image)
        elif x == "paper":
            user_label.configure(image=paper_image)
        else:
            user_label.configure(image=scissor_image)

        checkwin(x, compchoice)

    # buttons
    rock = (Button(root, width=20, height=2, font=("Helvetica", 10, "bold"), text="ROCK", bg="#FF3E4D",
                   fg="white", command=lambda: updatechoice("rock")).grid(row=2, column=1))
    paper = (Button(root, width=20, height=2, text="PAPER", font=("Helvetica", 10, "bold"), bg="#FFD700",
                    fg="white", command=lambda: updatechoice("paper")).grid(row=2, column=2))
    scissor = (Button(root, width=20, height=2, text="SCISSOR", font=("Helvetica", 10, "bold"), bg="#00FFFF",
                      fg="white", command=lambda: updatechoice("scissor")).grid(row=2, column=3))


# Play window
play_window = Tk()
play_window.title("Rock Paper Scissor")
play_window.configure(background="#7171C6")

# Play button
play_button = Button(play_window, text="Play", font=("Helvetica", 20, "bold"), width=10, height=1, bg="#473C8B",
                     fg="white", command=open_main_window)
play_button.pack()
play_button.place(relx=0.5, rely=0.7, anchor=CENTER)  # Place the button at the center of the window

title_label = Label(play_window, text="Rock Paper Scissors", font=("Rupee Foradian", 24, "bold"), bg="#7171C6",
                    fg="white")
title_label.place(relx=0.5, rely=0.3, anchor=CENTER)
play_window.geometry("940x400")  # Set the size of the play window same as root window

play_window.mainloop()
