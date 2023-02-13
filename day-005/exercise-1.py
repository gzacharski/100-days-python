student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

number = 0
sum_of_height = 0
for height in student_heights:
    number += 1
    sum_of_height += height

print(round(sum_of_height / number))
