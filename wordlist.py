import random
words = ["aardvark",
             "air",
             ...,
             ...,
             "zipper",
             "zoo"]

def get_random_word():
    word = random.choice(words)
    print(word)
    return word

