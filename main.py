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


def num_input_validation(prompt_string, ls):
    num = input(prompt_string).strip()
    if num.isnumeric():
        if ls and int(num) in range(1, len(ls) + 1):
            return int(num) - 1
        elif not ls:
            return int(num)

    print("Please put a valid number")
    return num_input_validation(prompt_string, ls)


def select_again(prompt_string):
    selection = input(f"{prompt_string} If yes type Y otherwise hit enter to continue: ").strip().lower()
    if selection == "y":
        return True
    return False


students = []


def add_student():
    name = name_validation("Enter student name")
    if name in students:
        print(f"The student's name: {name} you have entered already is in the record ")
    return name


def view_students():
    print(f"Total students is: {len(students)}")
    for index, student in enumerate(students):
        print(f"{index + 1} - {student}")


def search_student():
    name = name_validation("Enter student name")
    if name in students:
        print(f"The student {name} is in the record")
    else:
        print(f"The student {name} is not in the record ")
        if select_again("Would you like to add the student to the record? "):
            add_student()


def remove_student():
    name = name_validation("Enter student name to remove: ")
    if name in students:
        return name
    else:
        print(f"The student {name} is not in the record ")
        return False


while True:
    options = ["Add student", "View Students", "Search Student", "Remove Student"]
    for i in range(len(options)):
        print(f"{i + 1}) {options[i]}")
    choice = num_input_validation("Select a number from the list: ", ls=options)

    if choice == 0:
        new_student = add_student()
        students.append(new_student)
        print(f"You have added a new student: {new_student} to your record")
        continue
    if choice == 1:
        view_students()
        continue
    if choice == 2:
        search_student()
        continue
    if choice == 4:
        removed_student = remove_student()
        if removed_student:
            print(f"You have removed the student: {removed_student} from your record")
        continue
