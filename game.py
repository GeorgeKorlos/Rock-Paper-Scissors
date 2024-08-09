import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
comp_choice = random.randint(0,2)

if choice == 0 and comp_choice == 0:
    print("Rock\nComputer chose Rock\nTie.")
elif choice == 0 and comp_choice == 1:
    print("Rock\nComputer chose Paper\nYou lose.")
elif choice ==0 and comp_choice ==2:
    print("Rock\nComputer chose Scissors\nYou win.")
elif choice == 1 and comp_choice == 0:
    print("Paper\nComputer chose Rock\nYou win.")
elif choice == 1 and comp_choice == 1:
    print("Paper\nComputer chose Paper\nTie.")
elif choice == 1 and comp_choice ==2:
    print("Paper\nComputer chose Scissors\nYou lose.")
elif choice == 2 and comp_choice == 0:
    print("Scissors\nComputer chose Rock\nYou lose.")
elif choice == 2 and comp_choice == 1:
    print("Scissors\nComputer chose Paper\nYou win.")
else:
    print("Scissors\nComputer chose Scissors\nTie.")
