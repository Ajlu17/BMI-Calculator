import math
import tkinter as tk

def calculate_bmi():
    # Clear the previous result before validating a new calculation.
    result_label.config(text="", fg="red", wraplength=360)
    values = [weight_entry.get().strip(), feet_entry.get().strip(),
              inches_entry.get().strip()]

    if any(value == "" for value in values):
        result_label.config(text="Please fill in all fields. Use 0 for no additional inches.")
        return

    try:
        weight, feet, inches = [float(value) for value in values]
    except ValueError:
        result_label.config(text="Please enter numbers only, such as 150 or 5.5.")
        return

    if not all(math.isfinite(value) for value in (weight, feet, inches)):
        result_label.config(text="Please enter finite numbers only.")
        return

    if weight <= 0:
        result_label.config(text="Weight must be greater than 0.")
        return

    if feet < 0:
        result_label.config(text="Feet cannot be negative.")
        return

    if not 0 <= inches < 12:
        result_label.config(text="Additional inches must be at least 0 and less than 12.")
        return

    total_inches = feet * 12 + inches
    if total_inches <= 0:
        result_label.config(text="Total height must be greater than 0.")
        return

    # Divide in steps to avoid overflowing when squaring a very large height.
    bmi = weight / total_inches / total_inches * 703
    if not math.isfinite(total_inches) or not math.isfinite(bmi) or bmi <= 0:
        result_label.config(text="These values are outside the supported calculation range.")
        return

    result_label.config(text=f"Your BMI is {bmi:.2f}", fg="black")


window = tk.Tk()
window.title("My BMI Calculator")
window.geometry("400x300")

weight_label = tk.Label(window, text="Weight in lb:")
weight_label.pack()

weight_entry = tk.Entry(window)
weight_entry.pack()

feet_label = tk.Label(window, text="Height: feet")
feet_label.pack()

feet_entry = tk.Entry(window)
feet_entry.pack()

inches_label = tk.Label(window, text="Additional inches:")
inches_label.pack()

inches_entry = tk.Entry(window)
inches_entry.pack()

calculate_button = tk.Button(
    window,
    text="Calculate BMI",
    command=calculate_bmi
)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()