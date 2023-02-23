student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
# TODO-2: Write your code below to add the grades to student_grades.👇

student_grades = {}


def map_to_grade(score):
    if 91 <= score < 100:
        return "Outstanding"
    elif 81 <= score <= 90:
        return "Exceeds Expectations"
    elif 71 <= score <= 80:
        return "Acceptable"
    else:
        return "Fail"


for key in student_scores.keys():
    student_grades[key] = map_to_grade(student_scores[key])

# 🚨 Don't change the code below 👇
print(student_grades)
