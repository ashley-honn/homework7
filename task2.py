#Use the DataFrame of Python’s pandas package to calculate and print the required output
#Calculate the grade for each student according to the following rules:
#Calculate the class GPA with two decimal places according to the following rule:
#Print the GPA for each student and the whole class

import pandas as pd

scores = pd.read_csv('scores.csv', header=0, index_col = 0)

#Define the letter grades based on students score
def letter_grade(score):
    if score >= 90:
        gpa = 4.00
    elif score >= 80:
        gpa = 3.00
    elif score >= 70:
        gpa = 2.00
    elif score >= 60:
        gpa = 1.00
    else: 
        gpa = 0.00
    
    return gpa


#GPA of students
total_gpa = 0.0
total_num = len(scores.index)
total_col = len(scores.columns)
student_gpa = 0.0

#Assigning the gpa 
for i in scores.columns:
    print(i, end = ' ')
    total = 0.0
    for j in scores[i]:
        gpa = letter_grade(j)        
        total += gpa
        student_gpa = total / total_num #equation for student gpa
    print(f'{(student_gpa):.3}')
    total_gpa += student_gpa

#print the gpa for class
print(f'GPA for the class is: {(total_gpa / total_col):.2}')
