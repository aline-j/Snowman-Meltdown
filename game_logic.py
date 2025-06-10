import random    # # Module for selecting a random word
import snowman    # Module with ASCII art for the snowman levels
import ascii_art    # Module with the list of words and start of game


def get_random_word():
    """
    Selects and returns a random word from the predefined list
    in snowman.WORDS
    """
    return random.choice(snowman.WORDS)


def display_game_state(count_of_mistakes, secret_word, guessed_letters):
    """
    Displays the current state of the snowman and the word being guessed.
    count_of_mistakes (int): Number of incorrect guesses made so far.
    secret_word (str): The word the player is trying to guess.
    guessed_letters (set): The set of letters the player has guessed correctly.
    """
    print(ascii_art.STAGES[count_of_mistakes])    # Show snowman based on mistakes
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter    # Show correct letter
        else:
            display_word += "_"   # Hide unguessed letter
    print(f'Word: {display_word}')
    print()


def play_game():
    """
    Main game logic for playing a single round of Snowman Meltdown.
    Handles input, game state, win/loss detection, and user feedback.
    """
    secret_word = get_random_word()
    count_of_mistakes = 0
    guessed_letters = set()
    won = False    # Flag to track if the player has won

    print("Welcome to Snowman Meltdown!")
    display_game_state(count_of_mistakes, secret_word, guessed_letters)

    # Game loop: Continues until the snowman melts completely
    # or the word is guessed
    while count_of_mistakes < 3:
        guess = input("Guess a letter: ").lower()
        print()

        # Correct guess
        if guess in secret_word:
            guessed_letters.add(guess)
            print(f'✅ Letter "{guess}" is in the secret word!')
            display_game_state(count_of_mistakes, secret_word, guessed_letters)

            # Check if all letters have been guessed
            if len(set(secret_word)) == len(guessed_letters):
                # display message if the game was won
                print(f"🥳 Congratulations, you saved the snowman!")
                won = True
                break
            continue

        # Incorrect guess
        else:
            count_of_mistakes += 1
            print(f'❌ Letter "{guess}" is not in the secret word!')
            display_game_state(count_of_mistakes, secret_word, guessed_letters)

    # display message if the game was lost
    if not won:
        print(f"☹️ Game Over! The word was: {secret_word}")
