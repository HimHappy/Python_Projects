# tkinter - used for GUI
import tkinter as tk
from tkinter import filedialog,messagebox

# opening new file and making sure that previous file is removed/deleted
def new_file():
     text.delete(1.0,tk.END)

# open file fn nd make sure only .txt file open ho
def open_file():
    file_url = filedialog.askopenfilename(defaultextension='.txt',filetypes=[("Text Files","*.txt")])
    if file_url:
        with open(file_url,'r')as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END,file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path,'w')as file:
            file.write(text.get(1.0,tk.END))
            messagebox.showinfo('Info','File Saved Successfully')

window = tk.Tk()
window.title('Personal NotePad')
window.geometry("800x600")

menu = tk.Menu(window)
window.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=window.quit)

text = tk.Text(window, wrap = tk.WORD,font=("Helvetica",12),fg='blue')
text.pack(expand=tk.YES, fill=tk.BOTH)

window.mainloop()