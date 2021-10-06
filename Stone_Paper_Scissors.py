from tkinter import *
from tkinter import font,ttk
import random
from tkinter import messagebox

#creating main window here
root = Tk()
root.title("Coding Ninjas Rock Paper Scissors")
root.geometry("800x300")

number_of_times= StringVar()

clicked = StringVar()

n = number_of_times.get()


#function for placing main game labels by destroying intial labels
def game_start():
    global n
    n_label.after(1, n_label.destroy())
    n_submit.destroy()
    n_entry.destroy()
    n = number_of_times.get()

    pl.place(x=10, y= 70 )
    bot.place(x=650, y= 70)
    
    player_score.place(x= 60, y = 100)
    bot_score.place(x= 700, y= 100 )

    turn_display = Label(root, text=n, font = ("Arial", 10))
    No_Of_Turns.place(x = 300, y = 70)
    turn_display.place(x = 370, y =100)
    
    drop_list.place(x = 350, y = 150)
    submit.place(x= 350, y = 190)

options = ["Rock", "Paper", "Scissor"]


#making of initial labels
sps_label = Label(root, text="Rock Paper Scissor", font=("Arial", 30, "bold"))
sps_label.place(x= 200, y=0)

n_label = Label(root, text="Enter the number of rounds you want to play:", font=("Arial", 10))
n_label.place(x=200, y= 50)

n_entry = Entry(root, textvariable= number_of_times, font=("Arial", 10))
n_entry.place(x= 500, y=50 )

n_submit = Button(root, text= "Submit", font=("Arial", 10), height=1, width=5, command=lambda: game_start() )
n_submit.place(x = 500, y= 75)


#making of main game labels 
pl = Label(root, text="Player Score", font=("Arial", 20))
bot = Label(root, text="Bot Score",font=("Arial", 20) )

player_score = Label(root, text="0", font=("Arial", 10))
bot_score = Label(root, text="0", font=("Arial", 10) )

No_Of_Turns = Label(root, text="Number of turns chosen",  font = ("Arial", 20))
turn_display = Label(root, text=n, font = ("Arial", 10))


drop_list = ttk.Combobox(root, value= ("Rock", "Paper", "Scissor"))                     #using ttk to create dropdown list for selection of option for user
arial15 = font.Font(family="Arial", size=15)
drop_list.config(font = arial15)
drop_list.current(0)

submit = Button(root, text="Submit", font = ("Arial", 10) , height= 1, width= 5, command= lambda: game_run() )

choice = 0
count = 0
botg = 0
palyerg = 0


#making of main function for running the function
def game_run():
    global count
    y = int(n)
    global botg 
    global palyerg, c
    
    #checking user input
    if drop_list.get() == "Rock":
            choice = 0
    elif drop_list.get() == "Paper":
            choice = 1
    elif drop_list.get() == "Scissor":
            choice = 2
    
       
        
    #Taking computer's choice    
    bot_choice = random.randint(0,2)

    #conditions for checking game round result and adding scores to respective labels
    if choice == 0 and bot_choice == 1:
            final_message = Label(root, text="Bot wins this round.", font = ("Arial", 15))
            final_message.place(x = 350, y = 240)
            botg+=1
            v = str(botg)
            bot_score.config(text=v)

    elif choice == 1 and bot_choice == 2:
            final_message = Label(root, text="Bot wins this round.", font = ("Arial", 15))
            final_message.place(x = 350, y = 240)
            botg+=1
            v = str(botg)
            bot_score.config(text=v)

    elif choice == 2 and bot_choice == 0:
            final_message = Label(root, text="Bot wins this round.", font = ("Arial", 15))
            final_message.place(x = 350, y = 240)
            botg+=1
            v = str(botg)
            bot_score.config(text=v)

    elif bot_choice == 0 and choice == 1:
            final_message = Label(root, text="Player wins this round.", font = ("Arial", 15))
            final_message.place(x = 350, y = 240)
            palyerg+=1
            v = str(palyerg)
            player_score.config(text=v)

    elif bot_choice == 1 and choice == 2:
            final_message = Label(root, text="Player wins this round.", font = ("Arial", 15))
            final_message.place(x = 350, y = 240)
            palyerg+=1
            v = str(palyerg)
            player_score.config(text=v)

    elif bot_choice == 2 and choice == 0:
            final_message = Label(root, text="Player wins this round.", font = ("Arial", 15))
            final_message.place(x = 350, y = 240)
            palyerg+=1
            v = str(palyerg)
            player_score.config(text=v)
    elif bot_choice == choice:
        final_message = Label(root, text="This is a tie round", font = ("Arial", 15))
        final_message.place(x = 350, y = 240)

 
    
    
    count+=1
    
    #checking for game end by checking number of rounds done and showing the message for result
    if count == y:
        submit.config(state=DISABLED)
        if botg> palyerg:
            messagebox.showinfo("Game Over", "Bot wins!!!")
        elif palyerg>botg:
            messagebox.showinfo("Game Over", "You win!!!")
        elif botg == palyerg:
            messagebox.showinfo("Game Over", "This game was a draw.")
    else:
        pass


root.mainloop()

