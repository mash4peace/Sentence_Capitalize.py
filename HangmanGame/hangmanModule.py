import HangmanGame.wordlist
#Get  a random word from the word list
def get_word():
    word = HangmanGame.wordlist.get_random_word()
    return word.upper()
#Add spaces between letters
def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces
#Draw the display
def draw_screen(num_wrong, number_guesses, guessed_letter, displayed_word):
    print("_" * 79)
    print("Word:", add_spaces(displayed_word),
          " Guesses :", number_guesses,
          " Wrong:", num_wrong,
          " Tried:", add_spaces(guessed_letter)
          )
#Get next letter from user
def get_letter(guessed_letter):
    while True:
        guess = input("Enter a letter: ").strip().upper()
        #Make sure the user enters a letter and only one letter
