
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != secret_word and not out_of_guesses:
    if guess_count == 1:
        print("Tip: It's an animal with a long neck!")
    elif guess_count == 2:
        print("Tip: The secret word starts with the letter g!")
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if secret_word == guess:
    print("YOU WON MAN!1!")
else:
    print("You lost you dumb shit!")
