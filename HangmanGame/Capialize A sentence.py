def getupperCase(sentence):
    sentence = sentence.capitalize()
    return sentence


def main():
    try:
        upperCase = ""
        sentence = str(input("Please enter a sentence: " ))
        while sentence.isalpha():

            upperCase = getupperCase(sentence)
            print(upperCase)

    except SyntaxError:
        print("Please type alphabet ")



# def getupperCase(sentence):
#     sentence = sentence.capitalize()
#     return sentence

main()