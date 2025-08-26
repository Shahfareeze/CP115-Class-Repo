# Exercise 4
student_course = 5

grade1, grade2, grade3, grade4, grade5 = 78,85,92,67,88
fullmark = 100
total_fullmark = 500

total_mark = grade1 + grade2 + grade3 + grade4 + grade5
print(total_mark)

average_score = total_mark / student_course
print(average_score)

#Seacrh pencentage for each grade contribute to 100%

percentage_grade1 = (grade1 / total_fullmark) * 100
percentage_grade2 = (grade2 / total_fullmark) * 100
percentage_grade3 = (grade3 / total_fullmark) * 100
percentage_grade4 = (grade4 / total_fullmark) * 100
percentage_grade5 = (grade5 / total_fullmark) * 100
print(f"Percentage Grade 1 = {percentage_grade1}")
print(f"Percentage Grade 2 = {percentage_grade2}")
print(f"Percentage Grade 3 = {percentage_grade3}")
print(f"Percentage Grade 4 = {percentage_grade4}")
print(f"Percentage Grade 5 = {percentage_grade5}")


total_percentage = (total_mark / total_fullmark) * 100
print(total_percentage)


