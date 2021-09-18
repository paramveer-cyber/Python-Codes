def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("select the operation you want to choose :-")
print("press 1 to add")
print("press 2 to subtract")
print("press 3 to multiply")
print("press 4 to divide")
print("press 5 to stop the calculator")

while True:
    choice = input("please Enter Your Choice: ")

    if choice == "5":
        break

    num1 = int(input("please Enter The First No. \n"))
    num2 = int(input("please Enter The Second No. \n"))

    if choice == "1":
        print(num1, "+", num2, "=", add(num1, num2))

    if choice == "2":
        print(num1, "-", num2, "=", sub(num1, num2))

    if choice == "3":
        print(num1, "*", num2, "=", multiply(num1, num2))

    if choice == "4":
        print(num1, "/", num2, "=", divide(num1, num2))

