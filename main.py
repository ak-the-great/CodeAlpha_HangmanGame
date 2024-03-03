import random

def choose_word():
    words = ['benz', 'bmw', 'toyota', 'rollsroyce', 'nissan', 'mazda', 'ford']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter

        else:
            display += "_"

    return display

def hang_man():
    word = choose_word()
    guessed_letters = []
    attempts_left = 5

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while attempts_left > 0:
        print("Word", display_word(word, guessed_letters))
        print("Attempts left: ", attempts_left)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single lettr.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            if display_word(word, guessed_letters) == word:
                print("Congratulations! You've guessed the word:", word)
                break

        else:
            print("Incorrect guess.")
            attempts_left -= 1

    else:
        print("Sorry, you've run out of attempts. The word was:", word)

hang_man()
