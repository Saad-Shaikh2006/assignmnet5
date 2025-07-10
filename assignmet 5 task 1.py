# Step 1: Create a dictionary of student marks
student_marks = {
    "Ali": 85,
    "Sara": 92,
    "Rahul": 78,
    "Meena": 88,
    "John": 95
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show an error message
if student_name in student_marks:
    print(f"✅ Marks for {student_name}: {student_marks[student_name]}")
else:
    print(f" Sorry, no record found for '{student_name}'.")

