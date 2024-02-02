import tkinter as tk
from time import strftime

window =  tk.Tk()
window.title("Digital Clock")
window.config(bg="blue")

def time():
    string = strftime("%I:%M:%S %p\n %D")
    label.config(text=string)
    label.after(1000,time)#calling itself every sec=1000ms

label = tk.Label(window,font=("calibry",50,'bold'),bg="yellow",foreground='black')
label.pack(anchor="center")

time()
window.mainloop()
# mainloop user input ka wait krta hai and gui run krta rahta hai