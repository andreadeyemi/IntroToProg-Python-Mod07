# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   Andre Adeyemi, 2/26/2024, Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.

# Data Classes -------------------------------------------- #
# ... (Person and Student classes) ...

class FileProcessor:
    """Processes data to and from a file"""
    
    @staticmethod
    def read_data_from_file(file_name: str, student_list: list) -> list:
        """
        Reads data from a file and converts it into a list of Student objects.
        
        :param file_name: The name of the file to read from.
        :param student_list: The list where the student data will be stored.
        :return: The updated list of students.
        :raises: Exception if file reading fails.
        """
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                student_list.clear()
                for student_data in data:
                    student = Student(
                        student_data['FirstName'],
                        student_data['LastName'],
                        student_data['CourseName']
                    )
                    student_list.append(student)
        except FileNotFoundError:
            print(f"No existing file named {file_name}. A new one will be created upon saving.")
        except Exception as e:
            raise Exception(f"An error occurred while reading from file: {e}")
        return student_list

    @staticmethod
    def write_data_to_file(file_name: str, student_list: list):
        """
        Writes the list of student objects to a file in JSON format.
        
        :param file_name: The name of the file to write to.
        :param student_list: The list of students to write to the file.
        :raises: Exception if file writing fails.
        """
        try:
            with open(file_name, 'w') as file:
                data = [student.to_dict() for student in student_list]
                json.dump(data, file, indent=4)
            print("Data saved successfully.")
        except Exception as e:
            raise Exception(f"An error occurred while writing to file: {e}")

class IO:
    """Handles Input/Output tasks"""
    
    @staticmethod
    def output_menu(menu_text: str):
        """
        Prints the menu text to the console.
        
        :param menu_text: The menu text to be displayed.
        """
        print(menu_text)

    @staticmethod
    def input_menu_choice() -> str:
        """
        Gets the user's menu choice.
        
        :return: A string representing the user's menu choice.
        """
        return input("Please select a menu option: ").strip()

    @staticmethod
    def output_student_and_course_names(student_list: list):
        """
        Prints the names of the students and their courses to the console.
        
        :param student_list: The list of students to display.
        """
        print("--- Current Student Enrollments ---")
        for student in student_list:
            print(student)
        print("-----------------------------------")

    @staticmethod
    def input_student_data(student_list: list):
        """
        Captures input for a new student and adds them to the student list.
        
        :param student_list: The list where the new student will be added.
        """
        try:
            first_name = input("Enter the student's first name: ").strip()
            last_name = input("Enter the student's last name: ").strip()
            course_name = input("Enter the course name: ").strip()
            # Create and add the new student object
            student = Student(first_name, last_name, course_name)
            student_list.append(student)
            print(f"{student} has been registered.")
        except ValueError as e:
            print(f"An error occurred while adding the student: {e}")

# Main Body of Script  ------------------------------------------------------ #
# ... (Code to load data and run the menu loop) ...

# Ensure the script doesn't run if it's imported as a module
if __name__ == "__main__":
    # Your existing script to load data and run the menu loop
    pass
