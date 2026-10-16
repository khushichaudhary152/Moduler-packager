import random
import string


def random_number():
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    number = random.randint(start, end)
    print("Random Number:", number)


def random_list():
    size = int(input("Enter list size: "))
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    numbers = [random.randint(start, end) for _ in range(size)]
    print("Random List:", numbers)


def random_password():
    length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    print("Random Password:", password)


def random_otp():
    otp = random.randint(100000, 999999)
    print("Random OTP:", otp)


def random_sampling():
    size = int(input("Enter sample size: "))

    data = list(range(1, 21))
    sample = random.sample(data, size)

    print("Random Sample:", sample)


def game_simulation():
    print("Simple Dice Game")

    player = random.randint(1, 6)
    computer = random.randint(1, 6)

    print("Your Dice:", player)
    print("Computer Dice:", computer)

    if player > computer:
        print("You Win!")
    elif player < computer:
        print("Computer Wins!")
    else:
        print("It's a Draw!")


if __name__ == "__main__":
    random_number()