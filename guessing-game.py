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


def factorial(val):
    if val == 1:
        return val
    else:
        return val * factorial(val - 1)
