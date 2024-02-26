# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: Python program that demonstrates using constants, variables, and print statements to 
#       display a message about a student's registration for a Python course. This program is 
#       very similar to Assignment05, but it adds the use of functions, classes, and using the 
#       separation of concerns pattern.
# Change Log: (Who, When, What)
#   Andre Adeyemi, 2/26/2024, Created Script
# ------------------------------------------------------------------------------------------ #

import json
from dataclasses import dataclass
import os  # Import os module to check file existence

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
@dataclass
class Person:
    """Represents a person"""
    first_name: str
    last_name: str

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

@dataclass
class Student(Person):
    """Represents a student, inherits from Person"""
    course_name: str

class FileProcessor:
    """
    A collection of processing layer functions that work with Json files
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows """
        try:
            if os.path.exists(file_name):  # Check if the file exists
                with open(file_name, "r") as file:
                    student_data = json.load(file)
            else:
                print(f"File '{file_name}' not found.")
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows """
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)

# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message
        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student.first_name} '  # Update to use attribute access
                  f'{student.last_name} is enrolled in {student.course_name}')  # Update to use attribute access
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should only contain alphabetic characters.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should only contain alphabetic characters.")
            course_name = input("Please enter the name of the course: ")
            student = Student(first_name=student_first_name, last_name=student_last_name, course_name=course_name)
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="Error: One of the values was not of the correct type!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with the entered data.", error=e)
        return student_data

# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
