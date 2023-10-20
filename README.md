# Hangman
# Hangman Game

A classic word-guessing game where the player tries to guess the word by suggesting letters.

## How It Works

1. A word is selected randomly from a predefined list of words.
2. The player then suggests a letter, which they think might be a part of the word.
3. If the suggested letter is in the word, it is revealed in all its correct positions. Otherwise, the player loses a life.
4. The game continues until:
    - The player guesses the word correctly.
    - The player runs out of lives.

## Features

- Words are selected from a predefined list which currently includes fruits but can be expanded to include more categories.
- The game has a validation system that checks if the input is a valid guess (a single alphabetical character that hasn't been guessed before).
- For each wrong guess, the player loses a life.
- A running display shows the current state of the word being guessed.

## Usage

1. Clone/download the repository.
2. Navigate to the directory containing the game file.
3. Run the game using Python with the command: `python filename.py`
4. Follow the on-screen prompts to guess letters and try to uncover the hidden word!

## Dependencies

- Python's built-in libraries. No additional libraries are required.

## Future Improvements

- Expand the word list or integrate an external dictionary API for a vast range of words.
- Introduce difficulty levels where the player can select the length or complexity of the word.
- Add graphics or a GUI for a more visually appealing experience.

## Contribution

Feel free to fork this repository and submit pull requests for any enhancements you might have in mind. All contributions are welcome!

## License

This project is open-source and free for all to use, modify, and distribute.

Enjoy playing and happy guessing!
