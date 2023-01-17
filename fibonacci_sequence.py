def fibonacci(num):
    if (num == 1):
        return 1
    elif(num == 0):
        return 0
    else:
        return fibonacci(num-1)+fibonacci(num-2)

print(fibonacci(18))