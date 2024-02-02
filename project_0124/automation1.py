import tkinter as tk
import webbrowser as wb
from tkinter import Button,Label,Entry

# main window
window = tk.Tk()
window.title("My Automation.one")
window.config(bg="steelblue")

# automate youtube search
def youtube():
    query = entry.get()
    url = f"https://www.youtube.com/results?search_query={query}"
    wb.open(url)

# automate google search
def google():
    query = entry.get()
    url = f"https://www.google.com/search?q={query}"
    wb.open(url)

# automate instagram search
def instagram():
    username = entry.get().replace('@','')
    url = f"https://www.instagram.com/{username}/"
    wb.open(url)

# create inout field
Label(window,text="Enter your command:").pack(pady=10) #label ko window me pack krne k liye pack use kiye hai
# paddy => label k upr niche 10 pixel ka gap
entry = Entry(window,width=70)
entry.pack(pady=10)
Button(window, text="Search on Youtube",command=youtube).pack(pady=5)
Button(window, text="Search on Google",command=google).pack(pady=5)
Button(window, text="Search on Instagram",command=instagram).pack(pady=5)

# run gui 
window.mainloop()
