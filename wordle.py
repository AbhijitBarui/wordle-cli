import random
from utils import help_text, load_dict, highlighter, wordleChecker

#introductory text
print(help_text)

#loading arrays for word checking and answer selecting
words_dict = load_dict("wordle_words.txt", 5, 'u')
words_checker = load_dict("wordle_words.txt", 5, 'u')
word_answer = random.choice(words_dict)

#loading arrays for highlighter
h0_list = load_dict('h0.txt', 1)
h1_list = load_dict('h1.txt', 1)
h2_list = load_dict('h2.txt', 1)
h3_list = load_dict('h3.txt', 1)

#merging lists into dict
zip_iter_1 = zip(h0_list,h1_list)
zip_iter_2 = zip(h0_list,h2_list)
zip_iter_3 = zip(h0_list,h3_list)

h1 = dict(zip_iter_1)
h2 = dict(zip_iter_2)
h3 = dict(zip_iter_3)

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