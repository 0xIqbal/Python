# Student Record Management System
students = {}
# Input 5 students
for i in range(5):
    print(f"\nEnter details for student {i+1}")

    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    cgpa = input("Enter CGPA: ")
    # Store in dictionary
    students[roll] = {
        "name": name,
        "age": age,
        "cgpa": cgpa
    }
# Save to file
file = open("students.txt", "w")
for roll, info in students.items():
    file.write(f"{roll},{info['name']},{info['age']},{info['cgpa']}\n")

file.close()
print("\nData saved to file successfully!")

# Read from file
print("\nReading from file...\n")

file = open("students.txt", "r")
data = file.readlines()
file.close()

# Display all students
for line in data:
    roll, name, age, cgpa = line.strip().split(",")

    print("Roll:", roll)
    print("Name:", name)
    print("Age:", age)
    print("CGPA:", cgpa)
