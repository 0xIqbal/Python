# Student Grade Calculator

name = input("Enter student name: ")

# Take marks of 3 subjects
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))

# Calculate average
average = (m1 + m2 + m3) / 3

# Display average
print("Student Name:", name)
print("Average Marks:", average)

# Determine grade
if average >= 80:
    print("Grade: A+")
elif average >= 70:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
else:
    print("Grade: C")