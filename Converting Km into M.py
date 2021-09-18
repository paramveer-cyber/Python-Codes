while True:
    try:
        num1 = float(input('''Please enter the number
You want to convert in meters: '''))
        print(f"{num1} multiply by 1000 = {num1*1000} meters")
    except:
        print("Please enter a valid no.")    