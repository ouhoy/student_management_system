def name_validation(prompt_string):
    name = input(prompt_string).lower().strip()
    if len(name) > 512:
        print("name too long")
        return name_validation(prompt_string)
    if len(name) < 3:
        print("name too short")
        return name_validation(prompt_string)
    if not name.replace(" ", "").isalpha():
        print("Make sure that your name does not contain any numbers or symbols.")
        return name_validation(prompt_string)
    return name


students = []

user_choice = input("What's your choice: ").strip().lower()

if user_choice == "add":
    student_name = name_validation("Please enter the name of the student: ")
    students.append(student_name)
if user_choice == "remove":
    student_name = name_validation("Please enter the name of the student: ")
    students.remove(student_name)
if user_choice == "remove":
    student_name = name_validation("Please enter the name of the student: ")
    students.remove(student_name)
if user_choice == "search":
    student_name = name_validation("Please enter the name of the student: ")
    try:
        students.index(student_name)
    except:
        print("This student does not exist")
