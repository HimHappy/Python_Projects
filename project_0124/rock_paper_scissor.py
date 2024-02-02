'''
cases:
Rock-Rock = tie
Rock-Paper = Paper win
Rock-Scissor = Rock Win
Paper-Paper = tie
Paper-Rock = Paper win
Paper-Scissor =  Scissor win
Scissor-Scissor = tie
Scissor-Paper = Scissor win
Scissors-Rock = Rock win
'''

# import random
# items_list = ["Rock","Paper","Scissor"] 
# user_choice = input("It's Your Turn choose - Rock/Paper/Scissor ")
# comp_choice = random.choice(items_list)
# print ("You choose ", user_choice," and Computer choose ", comp_choice)
# if (user_choice == comp_choice):
#     print("Shit! It's a tie. Both choose ",user_choice)
# elif(user_choice=='Rock'):
#     if(comp_choice=='Paper'):
#         print("Oh Noooo! Paper Cover Rock => Computer Win") 
#     else:
#         print("Hurrey! Rock Crushes Scissor => You Win")    
# elif(user_choice=='Paper'):
#     if(comp_choice=='Rock'):
#         print("Oh Noooo! Rock covers Paper => Computer Win")    
#     else:
#         print("Yeah!! Paper Covers Scissor => You Win")    
# elif user_choice == 'Scissor':
#         if comp_choice=='Rock':
#             print('Nooo!!! Rock Crushes Scissor => Computer Win')  
#         else:
#             print('Bummer!! Paper gets Cut by Scissor => You Win')

# adding GUI
import tkinter as tk

window = tk.Tk()
window.title("Rock Paper Scissor")
window.geometry('300x300')
window.config(bg="Sky Blue")
frame = tk.Frame(window, bg='Blue', height=200, width=200)
frame.pack()
label1 = tk.Label(frame, text="User Choice", font=("Arial Bold", 15), fg="Black")
label1.grid(row=0, column=0, padx=5, pady=5)
v1 = tk.StringVar()
options = ["Rock", "Paper", "Scissor"]
drop1 = tk.OptionMenu(frame, v1, *options)
drop1.configure(fg="White", bg="green", activeforeground="Red")
drop1.grid(row=0, column=1, padx=5, pady=5)

def check():
    uc = v1.get()
    import random
    cc = random.choice(options)
    label1.config(text=f"{uc} vs {cc}")
    if (uc == cc):
        result = "It's a Tie!"
    elif (uc == "Rock" and cc == "Scissor") or \
            (uc == "Paper" and cc == "Rock") or \
            (uc == "Scissor" and cc == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    rl = tk.Label(frame, text=result, font=("Helvetica", 18))
    rl.grid(row=1, column=0, columnspan=2)

    # Add Play Again button
    # play_again_button = tk.Button(frame, text="Play Again", command=play_again)
    # play_again_button.grid(row=2, column=0, columnspan=2, pady=10)
def play_again():
    # Destroy previous labels
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Re-create initial UI elements
    label1 = tk.Label(frame, text="User Choice", font=("Arial Bold", 15), fg="Black")
    label1.grid(row=0, column=0, padx=5, pady=5)
    
    v1.set("")  # Reset the OptionMenu selection
    
    drop1 = tk.OptionMenu(frame, v1, *options)
    drop1.configure(fg="White", bg="green", activeforeground="Red")
    drop1.grid(row=0, column=1, padx=5, pady=5)
    
    # Add Play Again button
    play_again_button = tk.Button(frame, text="Play Again", command=play_again)
    play_again_button.grid(row=2, column=0, columnspan=2, pady=10)

button = tk.Button(frame, text="Check", command=check)
button.grid(row=2, column=0, sticky="w")
window.mainloop()