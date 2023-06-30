import random
import asciart


asci_hangman = list(reversed(asciart.hangman))

asci_hangman_logo = asciart.hangman_logo

def hangman_start():
    word_list = ["ardvark","baboon", "camel"]
    chosen_word = random.choice(word_list)
    display = []

    for _ in range(len(chosen_word)):
        display.append("_")

    print(asci_hangman_logo + "\n")
    print(display)

    guesses_left = 7
    hangman_game(guesses_left, display, chosen_word)

def hangman_game(guesses_left, display, chosen_word):
    correct_flag = False
    if guesses_left == 0:
        print("Game Over. You lost. Exiting")
        return
    else:
        guess = input("Guess a letter: ").lower()
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter== guess:
                display[position] = letter
                correct_flag = True
        if correct_flag == False:
            guesses_left -= 1
            print(asci_hangman[guesses_left])
        else:
            if "_" in display:
                print("Still more to go")
            else:
                print(f'You\'ve guessed the word "{chosen_word}! You\'ve won!')
                return
    print(f"{' '.join(display)}")
    hangman_game(guesses_left, display, chosen_word)