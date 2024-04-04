from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Global variables
rounds_played = 0
user_wins = 0
comp_wins = 0
userscore = None
compscore = None


def open_main_window():
    global rounds_played, user_wins, comp_wins, userscore, compscore
    play_window.destroy()  # Destroy the play window
    # main window
    root = Tk()
    root.title("rock paper scissor")
    root.configure(background="#38B6FF")
    root.geometry("940x400")

    # Centering the main window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # Rounds
    rounds_label = Label(root, text=f"Rounds: {rounds_played}/10", font=("Helvetica", 12, "bold"), bg="#38B6FF",
                         fg="white")
    rounds_label.grid(row=0, column=1, columnspan=3)

    # pictures
    rock_image = ImageTk.PhotoImage(Image.open(r"C:\Users\kazim\Downloads\WhatsApp_Image_2024-04-04_at_7.40.41_PM-removebg-preview.png"))
    paper_image = ImageTk.PhotoImage(Image.open(r"C:\Users\kazim\Downloads\WhatsApp_Image_2024-04-04_at_7.41.20_PM-removebg-preview.png"))
    scissor_image = ImageTk.PhotoImage(Image.open(r"C:\Users\kazim\Downloads\WhatsApp_Image_2024-04-04_at_7.41.20_PM__1_-removebg-preview.png"))
    rock_image_comp = ImageTk.PhotoImage(Image.open(r"C:\Users\kazim\Downloads\WhatsApp_Image_2024-04-04_at_7.40.41_PM-removebg-preview.png"))
    paper_image_comp = ImageTk.PhotoImage(Image.open(r"C:\Users\kazim\Downloads\WhatsApp_Image_2024-04-04_at_7.41.20_PM-removebg-preview.png"))
    scissor_image_comp = ImageTk.PhotoImage(Image.open(r"C:\Users\kazim\Downloads\WhatsApp_Image_2024-04-04_at_7.41.20_PM__1_-removebg-preview.png"))

    # insert picture
    user_label = Label(root, image=scissor_image, bg="#38B6FF")
    comp_label = Label(root, image=scissor_image_comp, bg="#38B6FF")
    comp_label.grid(row=1, column=0)
    user_label.grid(row=1, column=4)

    # scores
    userscore = Label(root, text="0", font=("Helvetica", 20, "bold"), bg="#38B6FF", fg="white")
    compscore = Label(root, text="0", font=("Helvetica", 20, "bold"), bg="#38B6FF", fg="white")
    compscore.grid(row=1, column=1)
    userscore.grid(row=1, column=3)

    # indicators
    user_indicator = (Label(root, text="USER", font=("Helvetica", 20, "bold"), bg="#38B6FF", fg="white")
                      .grid(row=0, column=3))
    comp_indicator = (Label(root, font=("Helvetica", 20, "bold"), text="COMPUTER", bg="#38B6FF", fg="white")
                      .grid(row=0, column=1))

    # messages
    msg = (Label(root, font=50, bg="#38B6FF", fg="white"))
    msg.grid(row=3, column=2)

    # update message
    def updatemessage(x):
        msg['text'] = x
        msg.config(text=x, font=("Helvetica", 14, "bold"))

    # update user score
    def updateuserscore():
        global user_wins
        user_wins += 1
        userscore.config(text=str(user_wins))

    def updatecompscore():
        global comp_wins
        comp_wins += 1
        compscore.config(text=str(comp_wins))

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
        global rounds_played
        rounds_played += 1
        rounds_label.config(text=f"Rounds: {rounds_played}/10")

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

        if rounds_played == 10:
            end_game_window(root)

    # buttons
    rock = (Button(root, width=20, height=2, font=("Helvetica", 10, "bold"), text="ROCK", bg="#104E8B",
                   fg="white", command=lambda: updatechoice("rock")).grid(row=2, column=1))
    paper = (Button(root, width=20, height=2, text="PAPER", font=("Helvetica", 10, "bold"), bg="#104E8B",
                    fg="white", command=lambda: updatechoice("paper")).grid(row=2, column=2))
    scissor = (Button(root, width=20, height=2, text="SCISSOR", font=("Helvetica", 10, "bold"), bg="#104E8B",
                      fg="white", command=lambda: updatechoice("scissor")).grid(row=2, column=3))

def end_game_window(root):
    global end_window  # Declare end_window as global
    end_window = Toplevel(root)
    end_window.title("Game Over")
    end_window.configure(background="#38B6FF")

    result_label = Label(end_window, text="Game Over!", font=("Helvetica", 20, "bold"), bg="#38B6FF", fg="white")
    result_label.pack(pady=20)

    if user_wins > comp_wins:
        message = "Congratulations! You won the game!"
    elif user_wins < comp_wins:
        message = "Sorry! You lost the game!"
    else:
        message = "It's a tie!"

    message_label = Label(end_window, text=message, font=("Helvetica", 14), bg="#38B6FF", fg="white")
    message_label.pack(pady=10)

    play_again_button = Button(end_window, text="Play Again", font=("Helvetica", 12), bg="#104E8B", fg="white", command=restart_game)
    play_again_button.pack(pady=10)

    exit_button = Button(end_window, text="Exit", font=("Helvetica", 12), bg="#104E8B", fg="white", command=root.destroy)
    exit_button.pack(pady=10)

    # Centering the end game window
    end_window.update_idletasks()
    width = end_window.winfo_width()
    height = end_window.winfo_height()
    x = (end_window.winfo_screenwidth() // 2) - (width // 2)
    y = (end_window.winfo_screenheight() // 2) - (height // 2)
    end_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    root.mainloop()

def restart_game():
    global rounds_played, user_wins, comp_wins
    if end_window:
        end_window.destroy()  # Destroy the end game window
    userscore.config(text="0")  # Reset user score label to 0
    compscore.config(text="0")  # Reset computer score label to 0
    rounds_played = 0
    user_wins = 0
    comp_wins = 0
    open_main_window()


# Play window
play_window = Tk()
play_window.title("Rock Paper Scissor")
play_bg_image = Image.open(r"C:\Users\kazim\Downloads\Rock Paper Scissors.png")
play_bg_photo = ImageTk.PhotoImage(play_bg_image)

# Create canvas to put the background image
play_canvas = Canvas(play_window, width=play_window.winfo_screenwidth(), height=play_window.winfo_screenheight())
play_canvas.pack(fill=BOTH, expand=True)
play_canvas.create_image(0, 0, image=play_bg_photo, anchor=NW)

# Play button
play_button = Button(play_window, text="Play", font=("Helvetica", 20, "bold"), width=10, height=1, bg="#104E8B",
                     fg="white", command=open_main_window)
play_button.pack()
play_button.place(relx=0.5, rely=0.7, anchor=CENTER)  # Place the button at the center of the window
play_window.geometry("940x400")  # Set the size of the play window same as root window

# Centering the play window
play_window.update_idletasks()
width = play_window.winfo_width()
height = play_window.winfo_height()
x = (play_window.winfo_screenwidth() // 2) - (width // 2)
y = (play_window.winfo_screenheight() // 2) - (height // 2)
play_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

play_window.mainloop()
