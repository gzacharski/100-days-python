print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? %"))
number_of_people = int(input("How many people to split the bill? "))

bill_per_person = (total_bill / number_of_people) * (1 + tip / 100)
print(f"Each person should pay: ${str(format(round(bill_per_person, 2), '.2f'))}")
