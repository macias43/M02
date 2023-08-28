# Author: Mariana Macias 
# File Name: StudentQualification.py
# Description: App accepts student names and GPA's and determines if they qualify for the Dean's List or the Honor Roll.

# Setting empty list to store student information
students = []

# Asking for student's last name 
while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    
# Checking if user want's to Quit
    if last_name == 'ZZZ':
        break

# Asking for student's first name
    first_name = input("Enter student's first name: ")

# Asking for student's GPA as a float    
    while True:
        gpa_input = input("Enter student's GPA: ")
        try:
            gpa = float(gpa_input)
            break
        except ValueError:
            print("Invalid GPA. Enter a numeric value.")

# Appending student's information 
    students.append((first_name, last_name, gpa))

for student in students:
    first_name, last_name, gpa = student

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} does not qualify for any honors.")


