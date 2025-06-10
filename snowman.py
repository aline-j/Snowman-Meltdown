# Main module to start the game Snowman Meltdown

import game_logic    # Module for game logic

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

if __name__ == "__main__":
    game_logic.play_game()    # Starts a round of the game