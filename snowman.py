import random

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(count_of_mistakes, secret_word, guessed_letters):
    print(STAGES[count_of_mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print(f'Word: {display_word}')
    print()


def play_game():
    secret_word = get_random_word()
    count_of_mistakes = 0
    guessed_letters = set()
    print("Welcome to Snowman Meltdown!")
    display_game_state(count_of_mistakes, secret_word, guessed_letters)
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    while count_of_mistakes < 3:
        guess = input("Guess a letter: ").lower()
        if guess in secret_word:
            guessed_letters.add(guess)
            print(f'Letter ✅ – count_of_attempts: {count_of_mistakes}')
            display_game_state(count_of_mistakes, secret_word, guessed_letters)
            if len(set(secret_word)) == len(guessed_letters):
                break
            continue
        else:
            count_of_mistakes += 1
            display_game_state(count_of_mistakes, secret_word, guessed_letters)
            print(f'Letter ❌ – count_of_attempts: {count_of_mistakes}')


if __name__ == "__main__":
    play_game()