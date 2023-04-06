import random 

while True:
    user_input = str(input("Please enter your choice (Rock, Paper, Scissors, q to QUIT) : "))
    if user_input == "q":
        break
    user_input = user_input.lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    if user_input == "rock" or "paper" or "scissors":
        if user_input == computer_choice:
            print("Tie!")
        if user_input == "rock":
            if computer_choice == "paper":
                print("Lose!")
            elif computer_choice == "scissors":
                print("Victory!")
        elif user_input == "paper":
            if computer_choice == "rock":
                print("Victory!")
            elif computer_choice == "scissors":
                print("Lose!")
        else:
            if computer_choice == "paper":
                print("Victory!")
            elif computer_choice == "rock":
                print("Lose!")
    else:
        print("Enter a valid Choice!")

    print(user_input + ": User Choice")
    print(computer_choice + ": Computer Choice")

