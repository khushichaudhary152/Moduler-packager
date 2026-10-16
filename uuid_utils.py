import uuid


def generate_uuid():
    unique_id = uuid.uuid4()
    print("Generated UUID:", unique_id)


def demonstrate_uuid4():
    print("UUID4:", uuid.uuid4())


if __name__ == "__main__":
    generate_uuid()
    demonstrate_uuid4()