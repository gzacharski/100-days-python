import math


def paint_calc(height, width, cover=5):
    area = height * width
    ratio = area / cover
    cans = int(math.ceil(ratio))
    print(f"You'll need {cans} cans of paint.")


# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
