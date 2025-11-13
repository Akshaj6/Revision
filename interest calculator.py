import tkinter as tk
from tkinter import messagebox
def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())
        si = (principal * time * rate) / 100
        ci = principal * ((1 + rate / 100) ** time) - principal
        si_result_label.config(text=f"Simple Interest (SI): {si:.2f}")
        ci_result_label.config(text=f"Compound Interest (CI): {ci:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for all fields.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
app = tk.Tk()
app.title("Interest Calculator")
app.geometry("400x400")
principal_label = tk.Label(app, text="Principal Amount:")
principal_label.pack(pady=5)
principal_entry = tk.Entry(app, width=30)
principal_entry.pack(pady=5)
time_label = tk.Label(app, text="Time Period (Years):")
time_label.pack(pady=5)
time_entry = tk.Entry(app, width=30)
time_entry.pack(pady=5)
rate_label = tk.Label(app, text="Rate of Interest (%):")
rate_label.pack(pady=5)
rate_entry = tk.Entry(app, width=30)
rate_entry.pack(pady=5)
calculate_button = tk.Button(app, text="Calculate Interest", command=calculate_interest)
calculate_button.pack(pady=20)
si_result_label = tk.Label(app, text="Simple Interest (SI): ")
si_result_label.pack(pady=5)
ci_result_label = tk.Label(app, text="Compound Interest (CI): ")
ci_result_label.pack(pady=5)
app.mainloop()