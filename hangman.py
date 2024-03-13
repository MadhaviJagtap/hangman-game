import os
import random
import hangman_words as hw
import hangman_art as ha

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main function to execute Hangman game."""
    chosen_word = random.choice(hw.word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    print(ha.logo)

    # Create blanks
    display = ["_" for _ in range(word_length)]

    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        clear_screen()

        if guess in display:
            print(f"You have guessed '{guess}' already!")

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        # Check if user is wrong.
        if guess not in chosen_word:
            print(f"'{guess}' is not in the word. You lose a life!")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"You lose. The word was {chosen_word}")

        # Join all the elements in the list and turn it into a String.
        print(' '.join(display))

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(ha.stages[lives])

if __name__ == "__main__":
    main()
