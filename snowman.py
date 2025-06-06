import random

from numpy.ma.core import correlate

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    count_of_attempts = 0
    correct_letters = set()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    while count_of_attempts < 3:
        guess = input("Guess a letter: ").lower()
        if guess in secret_word:
            print(f'Letter ✅ – count_of_attempts: {count_of_attempts}')
            correct_letters.add(guess)
            if len(set(secret_word)) == len(correct_letters):
                break
            continue
        else:
            count_of_attempts += 1
            print(f'Letter ❌ – count_of_attempts: {count_of_attempts}')


if __name__ == "__main__":
    play_game()