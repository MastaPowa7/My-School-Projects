print('Enter the amount of students you are grading:')
student_amount = int(input())

total_grade = 0
#this is a list that will be used to store each student's grades
result_grades = []

for student_number in range(1, student_amount + 1):
     print(f"Enter student {student_number}'s grade:")
     student_grade = float(input())
     while student_grade < 0 or student_grade > 100:
          print('Error: Grade must be greater than 0 and no more than 100. Please enter again.')
          print(f"Enter student {student_number}'s grade:")
          student_grade = float(input())
     total_grade += student_grade
     #for each valid, results_grades.append will store the inputs here into the results_grade list
     result_grades.append(f"Student {student_number}'s grade: {student_grade}")
average_grade = total_grade / student_amount

#this for loop is used to grab the content inside result_grades, which came from result_grades.append storing them into it, and will print each out on a new line
for grade_list in result_grades:
     print(grade_list)
print(f'Average grade: {average_grade}')
