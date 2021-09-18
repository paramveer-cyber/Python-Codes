import random

the_number = random.randint(1, 100)
print("This is a No. guessing game")

for i in range(5):
    try:
        guess = int(input("Please enter the guess: "))
        if guess == the_number:
            print("You Have gueesed the right Number!!", the_number)
            break
        else:
            if guess == the_number-1:
                print("too close")
                print(f"{i} Guesses done")
            elif guess == the_number+1:
                print("too close")
                print(f"{i} Guesses done")
            elif guess <= the_number:
                print("Guess too Low")
                print(f"{i} Guesses done")
            elif guess >= the_number:
                print("Guess too high")
                print(f"{i} Guesses done")
            elif i == 4:
                print(f"You Lost the number was {the_number}")
            elif guess == 110:
                print(the_number)
    except Exception as e:
        print("Please recheck there was some error")
        i = i-1

