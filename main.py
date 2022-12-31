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
