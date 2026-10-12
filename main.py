import random

choices = ["rock", "paper", "scissors"]

print("=" * 35)
print("ROCK PAPER SCISSORS GAME")
print("=" * 35)

while True:
    print("\nChoose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "4":
        print("Thanks for playing! Goodbye!")
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
        continue

    player = choices[int(choice) - 1]
    computer = random.choice(choices)

    print("\nYou chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("Result: It's a tie!")

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("Result: Congratulations! You win!")

    else:
        print("Result: Computer wins!")

print("\nGame ended.")
