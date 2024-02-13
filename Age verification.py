import tkinter as tk
from tkinter import messagebox

def check_age():
    name = name_entry.get()
    try:
        age = int(age_entry.get())
        if age >= 18:
            messagebox.showinfo("Access Granted", f"Welcome, {name}! You are old enough to access the content.")
        else:
            messagebox.showerror("Access Denied", "Sorry, you are not old enough to access the content.")
    except ValueError:
        messagebox.showerror("Invalid Age", "Please enter a valid age.")

# Create the main window
root = tk.Tk()
root.title("Age Verification")

# Create labels and entry fields
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a button to check age
check_button = tk.Button(root, text="Check Age", command=check_age)
check_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the event loop
root.mainloop()
