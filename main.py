import random

def load_dict(file_name):
    file = open(file_name)
    words = file.readlines()
    file.close()
    return [word[:5].upper() for word in words]

words_dict = load_dict("wordle_words.txt")
word_answer = random.choice(words_dict)