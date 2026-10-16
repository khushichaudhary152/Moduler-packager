from datetime import datetime
import math
import random
import uuid
import os

from utilities.file_operations import create_file, write_file, read_file, append_file


def datetime_operations():
    print("\nDatetime and Time Operations")
    print("Current Date and Time:", datetime.now())


def mathematical_operations():
    print("\nMathematical Operations")

    number = float(input("Enter a number: "))

    print("Square Root:", math.sqrt(number))
    print("Power:", math.pow(number, 2))
    print("Factorial:", math.factorial(int(number)))


def random_data_generation():
    print("\nRandom Data Generation")

    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    print("Random Number:", random.randint(start, end))


def generate_uuid():
    print("\nUnique Identifier (UUID)")
    print("Generated UUID:", uuid.uuid4())


def file_operations():
    print("\nFile Operations")
    print("1. Create File")
    print("2. Write File")
    print("3. Read File")
    print("4. Append File")

    file_choice = input("Enter your choice: ")

    filename = input("Enter filename: ")

    if file_choice == "1":
        create_file(filename)

    elif file_choice == "2":
        content = input("Enter content: ")
        write_file(filename, content)

    elif file_choice == "3":
        read_file(filename)

    elif file_choice == "4":
        content = input("Enter content to append: ")
        append_file(filename, content)

    else:
        print("Invalid choice.")


def explore_module_attributes():
    print("\nModule Attributes using dir()")

    print("\nDatetime Module:")
    print(dir(datetime))

    print("\nMath Module:")
    print(dir(math))

    print("\nRandom Module:")
    print(dir(random))

    print("\nUUID Module:")
    print(dir(uuid))


def main():

    while True:

        print("\n================================")
        print("Welcome to Multi-Utility Toolkit")
        print("================================")

        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_operations()

        elif choice == "2":
            mathematical_operations()

        elif choice == "3":
            random_data_generation()

        elif choice == "4":
            generate_uuid()

        elif choice == "5":
            file_operations()

        elif choice == "6":
            explore_module_attributes()

        elif choice == "7":
            print("Thank you for using Multi-Utility Toolkit.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()