from datetime import datetime
import time


def current_date_time():
    now = datetime.now()
    print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))


def date_difference():
    first_date = input("Enter the first date (YYYY-MM-DD): ")
    second_date = input("Enter the second date (YYYY-MM-DD): ")

    date1 = datetime.strptime(first_date, "%Y-%m-%d")
    date2 = datetime.strptime(second_date, "%Y-%m-%d")

    difference = abs((date2 - date1).days)
    print("Difference:", difference, "days")


def custom_date_format():
    date_input = input("Enter date (YYYY-MM-DD): ")

    date = datetime.strptime(date_input, "%Y-%m-%d")

    print("Formatted Date:", date.strftime("%d-%m-%Y"))


def stopwatch():
    print("Stopwatch started...")
    input("Press Enter to stop the stopwatch.")

    print("Stopwatch stopped.")


def countdown_timer():
    seconds = int(input("Enter countdown time in seconds: "))

    while seconds > 0:
        print("Time remaining:", seconds)
        time.sleep(1)
        seconds -= 1

    print("Time's up!")


if __name__ == "__main__":
    current_date_time()