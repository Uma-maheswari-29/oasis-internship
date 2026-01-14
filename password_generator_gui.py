import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Main window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Heading
tk.Label(
    root,
    text="Advanced Password Generator",
    font=("Arial", 16, "bold")
).pack(pady=15)

# Length input
tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Generate button
tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    width=20
).pack(pady=15)

# Result field
result_entry = tk.Entry(root, font=("Arial", 12), justify="center")
result_entry.pack(pady=10, fill="x", padx=30)

# Run app
root.mainloop()
