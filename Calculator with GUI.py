import tkinter as tk

def press_key(key):
    current = entry.get()
    if key == 'C':
        entry.delete(0, tk.END)
    elif key == '=':
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, 'Error')
    else:
        entry.insert(tk.END, key)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry field for the calculator
entry = tk.Entry(root, width=25, borderwidth=5, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10) # added ipady for entry height

# Define buttons with text and their corresponding font
button_font = ('Arial', 12)
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Create buttons and assign the press_key function to them
for i, row in enumerate(buttons):
    for j, key in enumerate(row):
        button = tk.Button(root, text=key, padx=20, pady=20, font=button_font, command=lambda key=key: press_key(key))
        button.grid(row=i+1, column=j, padx=5, pady=5)

# Run the main loop
root.mainloop()