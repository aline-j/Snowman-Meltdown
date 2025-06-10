# Main module to start the game Snowman Meltdown

import game_logic    # Module for game logic

# List of secret words
WORDS = ['python', 'git', 'github', 'snowman', 'meltdown']


def main():
    # loop for game play
    while True:
        game_logic.play_game()  # Starts a round of the game
        new_game = input('Would you try another word? (yes/no): \n').strip().lower()
        if new_game not in ['yes', 'y'] or new_game == '':
            print('Bye!')
            break
        elif new_game not in ['yes', 'no', 'n']:
            print('Please enter "yes" or "no".')
            continue


if __name__ == '__main__':
    main()