def create_file(filename):
    with open(filename, "w") as file:
        file.write("")
    print("File created successfully.")


def write_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    print("Data written successfully.")


def read_file(filename):
    with open(filename, "r") as file:
        content = file.read()
    print("File Content:")
    print(content)


def append_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)
    print("Data appended successfully.")