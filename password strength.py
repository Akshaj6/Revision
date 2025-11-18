import tkinter as tk
from tkinter import messagebox
def check_password_strength():
    password = password_entry.get()
    password_length = len(password)
    strength_text = ""
    strength_color = "black"
    if password_length <= 5:
        strength_text = "Weak"
        strength_color = "red"
    elif 6 <= password_length <= 8:
        strength_text = "Medium"
        strength_color = "yellow"
    elif 9 <= password_length <= 12:
        strength_text = "Strong"
        strength_color = "light green"
    else:
        strength_text = "Very Strong"
        strength_color = "dark green"
    strength_label.config(text=f"Strength: {strength_text}", fg=strength_color)
app = tk.Tk()
app.title("Password Strength Checker App")
app.geometry("400x400")
password_label = tk.Label(app, text="Enter Password:")
password_label.pack(pady=20)
password_entry = tk.Entry(app, width=40, show="*")
password_entry.pack(pady=10)
check_button = tk.Button(app, text="Check Strength", command=check_password_strength)
check_button.pack(pady=15)
strength_label = tk.Label(app, text="Strength: ", font=("Arial", 14, "bold"))
strength_label.pack(pady=20)
app.mainloop()