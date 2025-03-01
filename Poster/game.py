import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    
    while True:
        print("\n👊 Rock, 📄 Paper, ✂️ Scissors - Shoot!")
        player_choice = input("Enter rock, paper, or scissors: ").lower()

        if player_choice not in choices:
            print("❌ Invalid choice! Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"\n🤖 Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("😐 It's a draw!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win!")
        else:
            print("💀 You lose!")

        replay = input("\nPlay again? (yes/no): ").lower()
        if replay != "yes" or replay != "y":
            print("👋 Thanks for playing!")
            break

# Start the game
play_game()
