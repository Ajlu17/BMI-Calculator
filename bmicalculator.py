import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    feet = float(feet_entry.get())
    inches = float(inches_entry.get())

    total_inches = feet * 12 + inches
    bmi = (weight / total_inches ** 2) * 703

    result_label.config(
        text = f"Your BMI is {bmi:1f}"
    )

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