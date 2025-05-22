import random


while(True):
    print("\n\n")
    print("1. Start Game!!")
    print("2. Exit!!")
    choice = int(input("Enter you choice : "))

    if choice == 1:
        number = int(input("Enter a number between 1 to 5 : "))
        rand = random.randint(1,5)

        if number >= 1 and number <= 5:
            if number == rand:
                print("Congo! You Win!!")
            else:
                print("You Loss!!")
        else:
            print("Invalid Input!!")


    elif choice == 2:
        print("Thank You!!")
        break
    else:
        print("Invalid Input!!")