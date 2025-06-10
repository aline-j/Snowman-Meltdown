# Main module to start the game Snowman Meltdown

import game_logic    # Module for game logic

# List of secret words
WORDS = ['python', 'git', 'github', 'snowman', 'meltdown']


def main():
    # Loop for game play
    while True:
        game_logic.play_game()  # Starts a round of the game
        new_game = input('Would you try another word? (yes/no): \n').strip().lower()
        if new_game not in ['yes', 'y']:
            if new_game not in ['yes', 'y', 'no', 'n']:
                print('Please enter "yes" or "no".')
                continue
            print('Bye!')
            break


if __name__ == '__main__':
    main()