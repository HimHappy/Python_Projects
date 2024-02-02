import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def check_winner():
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            # result = simpledialog.askstring("Tic-Toc-Toe", f"Player {buttons[combo[0]]['text']} wins!\nDo you want to play more? Enter 'yes' or 'no':")
            messagebox.showinfo("Tic-Toc-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            result = messagebox.askyesno("Again ","Do You Want To Play Again")
            if result:
                reset_game()
            else:
                window.quit()
    if all(button['text'] != '' for button in buttons):
        messagebox.showinfo("Tic-Toc-Toe", "It's a Draw!")
        result = messagebox.askyesno("Again ", "Do You Want To Play Again")
        if result:
            reset_game()
        else:
            window.quit()
            
def button_click(index):
    global winner
    if buttons[index]['text'] == '' and not winner:
        buttons[index]['text'] = current_player 
        check_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

def reset_game():
    global winner
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")
    winner = False
    label.config(text=f"Player {current_player}'s turn")

window = tk.Tk()
window.title("Tic-Toc-Toe")

buttons = [tk.Button(window, text="", font=('normal', 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "X"
winner = False
label = tk.Label(window, text=f"Player {current_player}'s turn", font=('normal', 16))
label.grid(row=3, column=0, columnspan=3)

window.mainloop()
