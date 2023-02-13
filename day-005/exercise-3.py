total = 0
for number in range(1, 101):
    total += number if number % 2 == 0 else 0

print(total)

total = 0
for number in range(0, 101, 2):
    total += number

print(total)
