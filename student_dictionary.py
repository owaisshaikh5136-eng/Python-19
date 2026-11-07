students = {}
def add_student(roll, name, age, grade):
    students[roll] = {"name": name, "age": age, "grade": grade}
def remove_student(roll):
    return students.pop(roll, None)
add_student(1, "Asha", 18, "A")
add_student(2, "Ravi", 19, "B")
print(students)
remove_student(2)
print(students)
