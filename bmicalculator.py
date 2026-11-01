import csv
import math
from pathlib import Path
from tkinter import ttk
import tkinter as tk

def get_bmi_category(bmi, age_months, sex):
    if age_months < 24:
        raise ValueError("This calculator supports ages 2 years and older.")
    if age_months >= 240:
        if bmi < 18.5:
            return "Underweight"
        if bmi < 25:
            return "Healthy weight"
        if bmi < 30:
            return "Overweight"
        return "Obesity"

    sex_code = {"Male": "1", "Female": "2"}.get(sex)
    if sex_code is None:
        raise ValueError("Select the sex used for the CDC growth chart.")
    data_path = Path(__file__).with_name("cdc_bmi_for_age.csv")
    try:
        with data_path.open(newline="", encoding="utf-8-sig") as data_file:
            for row in csv.DictReader(data_file):
                if row["Sex"].strip() == sex_code and float(row["Agemos"]) == age_months + 0.5:
                    p5, p85, p95 = (float(row[key]) for key in ("P5", "P85", "P95"))
                    if bmi < p5:
                        return "Underweight"
                    if bmi < p85:
                        return "Healthy weight"
                    if bmi < p95:
                        return "Overweight"
                    if bmi >= min(1.2 * p95, 35):
                        return "Severe obesity"
                    return "Obesity"
    except (OSError, KeyError, ValueError, csv.Error) as error:
        raise ValueError("Cannot read the CDC chart. Keep cdc_bmi_for_age.csv beside this program.") from error
    raise ValueError("No CDC reference found for this age and sex.")


def calculate_bmi(weight, feet, inches):
    """Return BMI for weight in pounds and height in feet and inches."""
    if not all(math.isfinite(value) for value in (weight, feet, inches)):
        raise ValueError("Please enter finite numbers only.")
    if weight <= 0:
        raise ValueError("Weight must be greater than 0.")
    if feet < 0:
        raise ValueError("Feet cannot be negative.")
    if not 0 <= inches < 12:
        raise ValueError("Additional inches must be at least 0 and less than 12.")

    total_inches = feet * 12 + inches
    if total_inches <= 0:
        raise ValueError("Total height must be greater than 0.")

    bmi = weight / total_inches / total_inches * 703
    if not math.isfinite(bmi) or bmi <= 0:
        raise ValueError("These values are outside the supported calculation range.")
    return bmi


def calculate_button_click():
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

    try:
        bmi = calculate_bmi(weight, feet, inches)
    except ValueError as error:
        result_label.config(text=str(error))
        return

    try:
        years = int(age_years_entry.get().strip())
    except ValueError:
        result_label.config(text="Enter age in whole years.")
        return

    if years < 0:
        result_label.config(text="Age cannot be negative.")
        return

    try:
        category = get_bmi_category(bmi, years * 12, sex_var.get())
    except ValueError as error:
        result_label.config(text=str(error))
        return

    basis = "CDC age/sex growth chart" if years < 20 else "CDC adult ranges"
    result_label.config(
        text=f"Your BMI is {bmi:.2f}\nCategory: {category}\n({basis})",
        fg="black"
    )


def main():
    global age_years_entry, feet_entry, inches_entry
    global result_label, sex_var, weight_entry

    window = tk.Tk()
    window.title("My BMI Calculator")
    window.geometry("440x520")

    tk.Label(window, text="Weight in lb:").pack()
    weight_entry = tk.Entry(window)
    weight_entry.pack()

    tk.Label(window, text="Height: feet").pack()
    feet_entry = tk.Entry(window)
    feet_entry.pack()

    tk.Label(window, text="Additional inches:").pack()
    inches_entry = tk.Entry(window)
    inches_entry.pack()

    tk.Label(window, text="Age: completed years (2 or older)").pack(pady=(12, 0))
    age_years_entry = tk.Entry(window)
    age_years_entry.pack()

    tk.Label(window, text="Sex for CDC growth chart (ages 2-19 only)").pack()
    sex_var = tk.StringVar(value="")
    ttk.Combobox(
        window, textvariable=sex_var, values=("Male", "Female"), state="readonly"
    ).pack(pady=(0, 12))

    tk.Button(
        window,
        text="Calculate BMI",
        command=calculate_button_click
    ).pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    tk.Label(window, text="BMI is a screening tool, not a diagnosis.", wraplength=400).pack(pady=12)
    window.mainloop()


if __name__ == "__main__":
    main()
