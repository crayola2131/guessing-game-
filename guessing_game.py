secret_word = "python"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("\nGuess a word: ")
        guess_count += 1

    else:
        out_of_guesses = True

if out_of_guesses:
    print("\nOut of guesses, better luck next time")
else:
    print("\nYou got it!")


