#import HangmanGame.wordlist
#Get  a random word from the word list
from HangmanGame import wordlist


def get_word():
    word = wordlist.get_random_word()
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
        if guess == "" or len(guess) >1:
            print("Invalid entry."+ "Please enter one and only one letter.")
            continue
        elif guess in guessed_letter:
            print("You already tried that letter")
            continue
        else:
            return guess
#The input/process/draw techniques is common in game programming
def  play_Game():
    word = get_word()
    word_length = len(word)
    remainig_letters = word_length
    displayed_word = "_" *word_length

    number_wrong = 0
    number_guess = 0
    guessed_letter = ""
    draw_screen(number_wrong, number_guess, guessed_letter, displayed_word)

    while number_wrong < 10 and remainig_letters >0:
        guess = get_letter(guessed_letter)
        guessed_letter += guess

        pos = word.find(guess, 0)
        if pos != 1:
            displayed_word = ""
            remainig_letters = word_length
            for char in word:
                if char in guessed_letter :
                    displayed_word += char
                    remainig_letters -= 1
                else:
                    displayed_word += "_"
        else:
            number_wrong +=1
        number_guess +=1
        draw_screen(number_wrong, number_guess, guessed_letter, displayed_word)

    print("-" *79)
    if remainig_letters == 0:
        print("Congrats ! you got it in ", number_guess, "guesses")
    else:
        print("Sorry, you lost.")
        print("The word was ", word)
def main():
    print("Play the H A N G M A N")
    while True:
        play_Game()
        print()
        again = input("Do you want to play again (y/n)?: ").lower()
        if again != "y":
            break
main()

