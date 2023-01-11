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


def student_exists(first_name, last_name):
    for student in students:
        if student["first_name"] == first_name and last_name == student["last_name"]:
            return True
    return False


students = []


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


def add_student():
    first_name = name_validation("Enter student's first name: ").lower().strip()
    last_name = name_validation("Enter student's last name: ").lower().strip()
    if student_exists(first_name, last_name):
        print(
            f"The student {first_name.capitalize()} {last_name.capitalize()} you have entered is already in the record")
    return {"first_name": first_name, "last_name": last_name, "id": len(students)}


def view_students():
    print(f"Total students is: {len(students)}")
    for student in students:
        print(f"{student['id']} - {student['first_name']} {student['last_name']}")


def search_student():
    first_name = name_validation("Enter student's first name: ").lower().strip()
    last_name = name_validation("Enter student's last name: ").lower().strip()
    if student_exists(first_name, last_name):
        print(f"The student {first_name.capitalize()} {last_name.capitalize()} you have entered is in the record.")
    else:
        print(f"The student {first_name.capitalize()} {last_name.capitalize()} you have entered is not in the record.")


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
        if new_student:
            students.append(new_student)
            print(f"You have added a new student: {new_student} to your record")
        continue
    if choice == 1:
        view_students()
        continue
    if choice == 2:
        search_student()
        continue
    if choice == 3:
        print("Worked")
        removed_student = remove_student()
        if removed_student:
            students.remove(removed_student)
            print(f"You have removed the student: {removed_student} from your record")

        continue
