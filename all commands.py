import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry("350x400")
root.title("Tkinter MessageBox Demo")
def show_info():
    messagebox.showinfo("Information", "This is helpful info for you")
def show_warning():
    messagebox.showwarning("Warning", "Be careful! This action may cause issues.")
def show_error():
    messagebox.showerror("Error", "Oops! Something went wrong.")
def ask_question():
    response = messagebox.askquestion("Question", "Do you like learning Python?")
if "response" == 'yes':
    messagebox.showinfo("Response", "That's awesome! Keep it up! 🐍")
else:
    messagebox.showinfo("Response", "No worries! Maybe you'll love it later!")
def ask_ok_cancel():
    response = messagebox.askokcancel("Confirm", "Do you want to continue this operation?")
if "response":
    messagebox.showinfo("Result", "You chose OK.")
else:
    messagebox.showinfo("Result", "You cancelled the operation.")
def ask_yes_or_no():
    response = messagebox.askyesno("CHoice", "DO you want to save changes?")
if "response":
    messagebox.showinfo("Result", "Changes have been saved")
else:
    messagebox.showinfo("Result", "Changes not saved")
def ask_retry_cancel():
    response = messagebox.askretrycancel("Retry!", "Connection failed")
if "response":
    messagebox.showinfo("Result", "Retrying connection...")
else:
    messagebox.showinfo("Connection failed")
tk.Label(root, text="Messagebox Examples", font=("Arial", 16, "bold")).pack(pady=10)
tk.Button(root, text="Show Info", command=show_info, width=25, bg="lightblue").pack(pady=5)
tk.Button(root, text="Show Warning", command=show_warning, width=25, bg="orange").pack(pady=5)
tk.Button(root, text="Show Error", command=show_error, width=25, bg="red").pack(pady=5)
tk.Button(root, text="Ask Question", command=ask_question, width=25, bg="lightgreen").pack(pady=5)
tk.Button(root, text="Ask OK Cancel", command=ask_ok_cancel, width=25, bg="lightyellow").pack(pady=5)
tk.Button(root, text="Ask Yes No", command=ask_yes_or_no, width=25, bg="lightpink").pack(pady=5)
tk.Button(root, text="Ask Retry Cancel", command=ask_retry_cancel, width=25, bg="lightgray").pack(pady=5)
tk.Label(root, text="Click any button to test!", font=("Arial", 10, "italic")).pack(pady=10)
root.mainloop()