import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        if weight <= 0 or height_cm <= 0:
            messagebox.showerror("Error", "Values must be greater than zero")
            return

        # Convert cm to meters
        height_m = height_cm / 100

        bmi = weight / (height_m * height_m)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI Value: {bmi}\nCategory: {category}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Main window
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("400x350")
root.resizable(False, False)

# Heading
tk.Label(
    root,
    text="Advanced BMI Calculator",
    font=("Arial", 16, "bold")
).pack(pady=15)

# Weight
tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

# Height in CM
tk.Label(root, text="Height (cm):").pack()
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Button
tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    width=20
).pack(pady=15)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run app
root.mainloop()
