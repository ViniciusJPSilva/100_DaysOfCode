'''
Instructions
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.

The final version of the student_grades dictionary will be checked.

DO NOT modify lines 1-7 to change the existing student_scores dictionary.

DO NOT write any print statements.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"

Expected Output
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'

'''

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.

OUTSTANDING = "Outstanding"
EXCEEDS_EXPECTATIONS = "Exceeds Expectations"
ACCEPTABLE = "Acceptable"
FAIL = "Fail"

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

def get_grade(score: float) -> str:
  if score >= 91:
    return OUTSTANDING
  if score >= 81:
    return EXCEEDS_EXPECTATIONS
  if score >= 71:
    return ACCEPTABLE
  return FAIL

for key in student_scores:
  student_grades[key] = get_grade(student_scores[key])

# 🚨 Don't change the code below 👇
print(student_grades)