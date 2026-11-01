# BMI Calculator

A graphical BMI calculator built with Python and Tkinter. It calculates BMI
from imperial measurements and displays an age-appropriate BMI category.

## Requirements

- Python 3
- Tkinter (included with most Python installations)

Keep `cdc_bmi_for_age.csv` in the same directory as the program. It provides
the CDC reference data used for users ages 2 through 19.

## Usage

Run the program from this directory:

```bash
python bmicalculator.py
```

Enter:

- Weight in pounds
- Height in whole feet
- Additional inches from 0 through 11
- Age in whole years
- Sex for the CDC growth chart when the user is under 20

Click **Calculate BMI** to display the BMI and category. The calculator
supports users age 2 and older. Adults use standard BMI ranges, while users
ages 2 through 19 use CDC age- and sex-specific reference data.

The calculator uses the standard BMI formula for measurements in pounds and inches:

```text
BMI = (weight / height²) × 703
```

The program validates required fields, numeric input, height ranges, weight,
age, and finite values before calculating.

## Tests

Run the unit tests from this directory:

```bash
python -m unittest -v
```

BMI is a screening tool, not a medical diagnosis.
