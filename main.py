import os
from difflib import SequenceMatcher

students = []
id_count = 0

options = ["Add student", "View Students", "Search Student", "Remove Student", "Exit"]


# ------- SUPPORT FUNCTIONS -------
class Bcolors:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Clear console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def name_validation(prompt_string: str) -> str:
    name = input(prompt_string).lower().strip()

    # Check if name is empty
    if not name:
        print(f"{Bcolors.WARNING}Please enter a valid name{Bcolors.END}")
        return name_validation(prompt_string)

    # Check if name includes alphabetical characters only
    if not name.replace(" ", "").isalpha():
        print(f"{Bcolors.WARNING}Make sure that your name does not contain any numbers or symbols.{Bcolors.END}")
        return name_validation(prompt_string)

    # Check the length of the name
    if len(name) > 64:
        print(
            f"{Bcolors.WARNING}The entered name is too long, please enter a valid name that doe not exceed 64 "
            f"characters in count.{Bcolors.END}")
        return name_validation(prompt_string)
    if len(name) < 1:
        print(
            f"{Bcolors.WARNING}The entered name is too short, please enter a valid name that doe not go under 1 "
            f"character in count.{Bcolors.END}")
        return name_validation(prompt_string)

    return name


def num_input_validation(prompt_string: str, ls: range or list) -> int:
    num = input(prompt_string).strip()

    # Check if the entered number is numeric and is in the list
    if num.isnumeric():
        if ls and int(num) in range(1, len(ls) + 1):
            return int(num) - 1
        elif not ls:
            return int(num)

    print(f"{Bcolors.WARNING}Please put a valid number{Bcolors.END}")
    return num_input_validation(prompt_string, ls)


def select_again(prompt_string: str) -> bool:
    selection = input(
        f"\n{Bcolors.INFO}{prompt_string} If yes type Y otherwise hit enter to continue: {Bcolors.END}").strip().lower()
    if selection == "y":
        return True
    return False


def student_exists(first_name, last_name) -> bool or dict:
    available_students = []
    for student in students:
        if student["first_name"] == first_name and last_name == student["last_name"]:
            available_students.append(student)

    return available_students


# Print student's details in a table
def student_table(students_list: list):
    spaces = " "
    spaces_num = len(students_list[0]["first_name"])
    dashes = "-"

    for student in students_list:
        if len(student["first_name"]) > spaces_num:
            spaces_num = len(student["first_name"])

        if len(student["last_name"]) > spaces_num:
            spaces_num = len(student["last_name"])
        spaces_num += 5

    print("\n", "ID", spaces * 5, "first name", spaces * (spaces_num - len("first name")), "last name")
    for student in students_list:
        print(dashes * (spaces_num * 3))
        print(student["id"], spaces * 6, student["first_name"], spaces * (spaces_num - len(student["first_name"])),
              student["last_name"])
    print(dashes * (spaces_num * 3))


def get_student_name() -> dict:
    while True:
        cls()
        first_name = name_validation("Enter student's first name: ").lower().strip()
        last_name = name_validation("Enter student's last name: ").lower().strip()

        if select_again("Do you want to edit your inputs?"):
            continue
        break
    return {"first_name": first_name, "last_name": last_name}


# ------- MAIN FUNCTIONS -------

def add_student():
    student_name = get_student_name()
    first_name = student_name["first_name"]
    last_name = student_name["last_name"]
    same_students = student_exists(first_name, last_name)

    if same_students:
        cls()
        print(
            f"The student {first_name.capitalize()} {last_name.capitalize()} is already in the record")
        student_table(same_students)
        if select_again("Would you like to add this student anyway?"):
            return {"first_name": first_name, "last_name": last_name, "id": id_count}

        return False

    return {"first_name": first_name, "last_name": last_name, "id": id_count}


def view_students():
    cls()
    if len(students) == 0:
        return print(f"{Bcolors.WARNING}There is no student in the record{Bcolors.END}\n")

    print(f"\n{Bcolors.INFO}Total Students: {len(students)} {Bcolors.END}")
    student_table(students)
    print("\n")


def search_student():
    cls()
    student_name = get_student_name()
    first_name = student_name["first_name"]
    last_name = student_name["last_name"]
    same_students = student_exists(first_name, last_name)

    # If there is one student with the entered name
    if len(same_students) == 1:
        print(
            f"{Bcolors.INFO}"
            f"The student {first_name.capitalize()} {last_name.capitalize()} is in the record."
            f"{Bcolors.END}")
        print("Student information: ")
        student_table(same_students)
        return

    # If there is more than one student with the same name in the record
    elif same_students:
        print(
            f"There are {len(same_students)} students with the name of {first_name.capitalize()} "
            f"{last_name.capitalize()} in the record.")
        print("Students information: ")
        student_table(same_students)
        return
    else:
        cls()
        print(
            f"{Bcolors.WARNING}"
            f"The student {first_name.capitalize()} {last_name.capitalize()} is not in the record."
            f"{Bcolors.END}")
        print(f"\nSimilar Search: ")

        similar_search = []
        for student in students:
            if similar(student["first_name"] + student["last_name"], first_name + last_name) > 0.4:
                similar_search.append(student)

        student_table(similar_search)
        similar_search.clear()


def remove_student():
    student_name = get_student_name()
    first_name = student_name["first_name"]
    last_name = student_name["last_name"]
    same_students = student_exists(first_name, last_name)

    # If there is one student with the entered name

    if len(same_students) == 1:
        return same_students[0]

    # If there is more than one student with the same name
    if same_students:
        print(f"There are {len(same_students)} students with the name of {first_name.capitalize()} "
              f"{last_name.capitalize()} in the record.")

        # print students table
        student_table(same_students)

        # Delete Student By Id
        while True:
            student_id = num_input_validation("Enter the ID of the student you wish to delete: ", False)
            for student in same_students:
                if student["id"] == student_id:
                    return student
            # Todo warn
            print("Please enter a valid ID from the above list.")

    # If there is no student with that name
    print(f"The student {first_name.capitalize()} {last_name.capitalize()} is not in the record.")
    return False


while True:

    print("---------Student Management System Methods---------\n")

    # Print Methods
    for i in range(len(options)):
        print(f"{i + 1}) {options[i]}")
    user_choice = num_input_validation("Select a number from the list: ", ls=options)

    # Add Student
    if user_choice == 0:
        new_student = add_student()
        if new_student:
            students.append(new_student)
            id_count += 1
            cls()
            print(
                f"{Bcolors.OK_GREEN}"
                f"The student {new_student['first_name'].capitalize()} {new_student['last_name'].capitalize()}"
                f" has been added to the record."
                f" {Bcolors.END}\n")
        continue

    # View Students
    if user_choice == 1:
        view_students()
        continue

    # Search Student
    if user_choice == 2:
        search_student()
        continue

    # Remove Student
    if user_choice == 3:
        removed_student = remove_student()
        if removed_student:

            print(f"{Bcolors.FAIL}Kindly note that this action will be final and cannot be undone{Bcolors.END}\n")
            if select_again("Please confirm if you intend to proceed with the deletion of this student."):
                students.remove(removed_student)
                print(
                    f"{Bcolors.OK_GREEN}"
                    f"You have successfully removed the student with this information"
                    f"{Bcolors.END}")
                student_table([removed_student])

        continue

    # Exit
    if user_choice == 4:
        print("Goodbye!")
        quit()
