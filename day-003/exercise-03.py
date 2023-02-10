year = int(input("Which year do you want to check? "))

isDividedBy4 = year % 4 == 0
isDividedBy100 = year % 100 == 0
isDividedBy400 = year % 400 == 0
isLeapYear = (isDividedBy4 and not isDividedBy100) or isDividedBy400

if isLeapYear:
    print("Leap year.")
else:
    print("Not leap year.")
