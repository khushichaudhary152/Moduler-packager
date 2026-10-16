import math


def factorial(n):
    return math.factorial(n)


def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return amount


def trigonometric_calculations(angle):
    radians = math.radians(angle)

    print("sin(", angle, ") =", math.sin(radians))
    print("cos(", angle, ") =", math.cos(radians))
    print("tan(", angle, ") =", math.tan(radians))


def area_of_circle(radius):
    return math.pi * radius * radius


def area_of_rectangle(length, width):
    return length * width


def area_of_triangle(base, height):
    return 0.5 * base * height