height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2, 0)
bmi_str = '{:.0f}'.format(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi_str}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi_str}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi_str}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi_str}, you are obese.")
else:
    print(f"Your BMI is {bmi_str}, you are clinically obese.")
