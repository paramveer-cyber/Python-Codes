print("This is a program to check if a no. is Palindromic or not")

while True:
    number = int(input("Please enter the number : "))

    reversed_number = str(number)[::-1]

    if number == int(reversed_number):
        print("Yes, This is a Palindromic number")
        print(reversed_number)

    elif number != reversed_number:
        print("Nop, This is not a Palindromic number")
        print(reversed_number)
