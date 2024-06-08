secret_word = "determination"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess:")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("out of guess,you lost")
else:
    print("you win!")


def hello():
    print("hello")


def new_feature_function():
    pass
    # some logic here
def display_menu():
    print("Welcome to the Guessing Game!")
    print("1. Start Game")
    print("2. exit Game")

def start_game():
    global guess, guess_count, out_of_guesses  # Use global to modify the variables outside the function
    while guess != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
        else:
            out_of_guesses = True
    if out_of_guesses:
        print("Out of guesses, you lost!")
    else:
        print("You win!")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            start_game()
            break  # Exit the menu after the game ends
        elif choice == '2':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")



def factorial(val):
    if val == 1:
        return val
    else:
        return val * factorial(val - 1)
