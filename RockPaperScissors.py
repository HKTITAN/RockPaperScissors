import random

print("Winning Rules of the Rock paper scissor game: \n"
                                +"Rock vs paper -> Paper wins \n"
                                +"Rock vs scissor -> Rock wins \n"
                                +"Paper vs scissor -> Scissor wins \n")

while True:
    user_name = input("What's your name?: ")
    
    print("\nEnter choice (1-3): \n 1. Rock\n 2. Paper\n 3. Scissors\n")

    choice = int(input(user_name + "'s turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input (1-3): "))

    if choice == 1:
        choice_name = "Rock"
    
    elif choice == 2:
        choice_name = "Paper"
    
    else:
        choice_name = "Scissors"

    print(user_name + "'s choice is: " + choice_name)
    print("Now it's computer's turn...")

    computer_choice = random.randint(1,3)

    while computer_choice == choice:
        comp_choice = random.randint(1,3)
    
    if computer_choice == 1:
        computer_choice_name = "Rock"
    
    elif computer_choice == 2:
        computer_choice_name = "Paper"
    
    else:
        computer_choice_name = "Scissors"
    
    print("Computer's choice is: " + computer_choice_name)
    print(choice_name + " V/S " + computer_choice_name)

    if((choice == 1 and computer_choice == 2) or
        (choice == 2 and computer_choice == 1)):
            print("Choice: Paper => ", end = "")
            result = "Paper"
    
    elif((choice == 1 and computer_choice == 3) or
        (choice == 3 and computer_choice == 1)):
            print("Choice: Rock => ", end = "")
            result = "Rock"
    
    else:
        print("Choice: Scissor => ", end = "")
        result = "Scissors"
    if result == choice_name:
        print(user_name + " Wins!")
    else:
        print("Computer Wins")
    
    print("Better luck Next Time!\n")

    ans = input("Do you want to play again? (Y for Yes / N for No): ")

    if ans == "N" or ans == "n":
        break

print("\nThanks for Playing " + user_name + "!")
print("Made by Harshit Khemani")