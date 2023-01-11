from prettytable import PrettyTable

students = []
id_count = 0

table = PrettyTable(["ID", "First Name", "Last Name"])
options = ["Add student", "View Students", "Search Student", "Remove Student", "Exit"]


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


def student_exists(first_name, last_name) -> bool or dict:
    available_students = []
    for student in students:
        if student["first_name"] == first_name and last_name == student["last_name"]:
            available_students.append(student)

    return available_students


def list_students(students_list):
    table.clear_rows()
    for student in students_list:
        table.add_row([student["id"], student["first_name"], student["last_name"]])
    print(table)


class StudentManagement:
    students_record = []

    def __init__(self, name):
        self.name = name

    def add_student(self):
        if self.name in self.students_record:
            print(f"The student's name: {self.name} you have entered already is in the record ")
            return False
        return self.name

    def view_students(self):
        print(f"Total students is: {len(self.students_record)}")
        for index, student in enumerate(self.students_record):
            print(f"{index + 1} - {self.students_record}")

    def search_student(self, name):
        if name in self.students_record:
            print(f"The student {name} is in the record")
            return True
        else:
            print(f"The student {name} is not in the record ")
            # if select_again("Would you like to add the student to the record? "):
            #     add_student()
            return False

    def remove_student(self, name):

        if name in self.students_record:
            return name
        else:
            print(f"The student {name} is not in the record ")
            return False


# todo edit options
def add_student():
    first_name = name_validation("Enter student's first name: ").lower().strip()
    last_name = name_validation("Enter student's last name: ").lower().strip()
    same_students = student_exists(first_name, last_name)

    if same_students:
        print(
            f"The student {first_name.capitalize()} {last_name.capitalize()} is already in the record")
        list_students(same_students)
        if select_again("Would you like to add this student anyway?"):
            return {"first_name": first_name, "last_name": last_name, "id": id_count}

        return False

    return {"first_name": first_name, "last_name": last_name, "id": id_count}


def view_students():
    if len(students) == 0:
        return print("There is no student in the record")

    print(f"Total Students: {len(students)}")
    list_students(students)
    print("\n")


def search_student():
    first_name = name_validation("Enter student's first name: ").lower().strip()
    last_name = name_validation("Enter student's last name: ").lower().strip()
    same_students = student_exists(first_name, last_name)

    # If there is one student with the entered name
    if len(same_students) == 1:
        print(f"The student {first_name.capitalize()} {last_name.capitalize()} is in the record.")
        print("Student information: ")
        list_students(same_students)
        return

    # If there is more than one student with the same name in the record
    elif same_students:
        print(
            f"There are {len(same_students)} students with the name of {first_name.capitalize()} "
            f"{last_name.capitalize()} in the record.")
        print("Students information: ")
        list_students(same_students)
        return
    else:
        print(f"The student {first_name.capitalize()} {last_name.capitalize()} is not in the record.")


# todo make sure to ask the user before deletion
def remove_student():
    first_name = name_validation("Enter student's first name: ").lower().strip()
    last_name = name_validation("Enter student's last name: ").lower().strip()
    same_students = student_exists(first_name, last_name)

    # If there is one student with the entered name

    if len(same_students) == 1:
        return same_students[0]

    # If there is more than one student with the same name
    if same_students:
        print(f"There are {len(same_students)} students with the name of {first_name.capitalize()} "
              f"{last_name.capitalize()} in the record.")

        # print students table
        list_students(same_students)

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
    for i in range(len(options)):
        print(f"{i + 1}) {options[i]}")
    user_choice = num_input_validation("Select a number from the list: ", ls=options)

    if user_choice == 0:
        new_student = add_student()
        if new_student:
            students.append(new_student)
            id_count += 1
            print(
                f"The student {new_student['first_name'].capitalize()} {new_student['last_name'].capitalize()}"
                f" has been added to the record.")
        continue
    if user_choice == 1:
        view_students()
        continue
    if user_choice == 2:
        search_student()
        continue
    if user_choice == 3:
        removed_student = remove_student()
        if removed_student:
            # todo danger

            print("Kindly note that this action will be final and cannot be undone")
            if select_again("Please confirm if you intend to proceed with the deletion of this student."):
                students.remove(removed_student)
                print(f"You have successfully removed the student with this information")
                list_students([removed_student])

        continue
    if user_choice == 4:
        print("Goodbye!")
        quit()
