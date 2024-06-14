def add(num1, num2):
    print(num1, "+", num2, "=", num1 + num2)


def subtract(num1, num2):
    print(num1, "-", num2, "=", num1 - num2)


def multiply(num1, num2):
    print(num1, "*", num2, "=", num1 * num2)


def divide(num1, num2):
    print(num1, "/", num2, "=", num1 / num2)


num1 = int(input("첫번째 수는 얼마입니까? "))
num2 = int(input("두번째 수는 얼마입니까? "))
operator = input("어떤 계산을 할까요?(+,-,* /)")

if operator == "+":
    add(num1, num2)
elif operator == "-":
    subtract(num1, num2)
elif operator == "*":
    multiply(num1, num2)
elif operator == "/":
    divide(num1, num2)
