def factorial(num):
    if (num == 1):
        return 1
    else:
        print(f"{num} into (factorial({num-1}))=")
        return num * factorial(num - 1)

print(factorial(7))
    