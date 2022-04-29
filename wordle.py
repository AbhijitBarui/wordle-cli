import random
from highlights import h1, h2, h3
from utils import help_text, load_dict, highlighter, wordleChecker

#introductory text
print(help_text)

#loading arrays for word checking and answer selecting
words_dict = load_dict("wordle_words.txt")
words_checker = load_dict("wordle_words.txt")
word_answer = random.choice(words_dict)

#attempt count
attempt_count = 6

#attempt iterations
for attempt in range(attempt_count):
    sample = input(f'attempts left {6 - attempt}, enter the word: ') #taking input
    if sample.upper()==word_answer: #check to see whether we got it in first try
        print(wordleChecker(word_answer, sample, h1, h2, h3))
        print("correct guess, you WON!! Thanks for playing")
        break
    if len(sample) == 5: #check to see whether the entered string is of length 5
        if sample.upper() in words_checker:
            print(wordleChecker(word_answer, sample, h1, h2, h3))
        else:
            print("not a valid word")
    elif sample.lower() == 'help': #help command
        print(help_text)
    else:
        print("less than 5 letters")

#print answer in the end
print(f'answer is {word_answer}')