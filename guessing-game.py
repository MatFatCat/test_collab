secret_word = "determination"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False
win_count = 0
loss_count = 0

def display_menu():
    print("Welcome to the Guessing Game!")
    print("1. Start Game")
    print("2. View Stats")
    print("3. Exit Game")

def start_game():
    global guess, guess_count, out_of_guesses, win_count, loss_count  # Use global to modify the variables outside the function
    guess = " "
    guess_count = 0
    out_of_guesses = False

    while guess != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("Out of guesses, you lost!")
        loss_count += 1
    else:
        print("You win!")
        win_count += 1

def view_stats():
    print(f"Total Wins: {win_count}")
    print(f"Total Losses: {loss_count}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            start_game()
        elif choice == '2':
            view_stats()
        elif choice == '3':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

def hello():
    print("Hello")

def new_feature_function():
    pass
    # some logic here

def factorial(val):
    if val == 1:
        return val
    else:
        return val * factorial(val - 1)

if __name__ == "__main__":
    main()
