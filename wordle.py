from multiprocessing.dummy import Array
import random
from highlights import h1, h2, h3

print('''
                        :Welcome to Wordle:
The rules are simple
You have 6 attempts, using those you have to guess the 5 letter word by entering valid 5 letter words
to help you guess there are 3 highlights:
highlight 1: 🇼 hen the letter is in the word and in right position
highlight 2: 🅷 🆆 en the letter is in the word but not in position
highlight 3: 🄿 hen the letter is not in the word
highlight 4: when its not even a letter
lets begin!!
''')

def load_dict(file_name):
    file = open(file_name)
    words = file.readlines()
    file.close()
    return [word[:5].upper() for word in words]

words_dict = load_dict("wordle_words.txt")
word_answer = random.choice(words_dict)

wordleflag = False
attempt_count = 6

def highlighter(word, dict_h):
    for letter in word:
        if letter in dict_h.keys():
            for key, value in dict_h.items():
                if letter.lower() == key: return value ;break
        else: return "❓"

def wordleChecker(answer, sample):
    arrans = list(answer.lower())
    arrsam = list(sample.lower())
    wordle_return=[]
    wordle_word = ""
    for idx1, ltr1 in enumerate(arrsam):
        for idx2,ltr2 in enumerate(arrans):
            if ltr1 == ltr2: #H1/H2 filter
                if idx1 == idx2: #check_3_1: H1 filter
                    wordle_return.append(highlighter(ltr1, h1))
                    arrans.pop(idx2)
                    arrans.insert(idx2,'%')
                    break
                else:
                    wordle_return.append(highlighter(ltr1, h2))
                    break
            if ltr1 not in arrans:
                wordle_return.append(highlighter(ltr1, h3))
                break
    even_count = 0
    for wordle_letters in wordle_return:
        wordle_word+=str(wordle_letters) + "   "

    return wordle_word

for attempt in range(attempt_count):
    sample = input(f'attempts left {6 - attempt}, enter the word: ')
    if sample.upper()==word_answer:
        print("correct guess")
        break
    if len(sample) == 5:
        #check 1 check of same words: whether the words are same
        print(wordleChecker(word_answer, sample))
    elif sample.lower() == 'help':
        print('''
The rules are simple
You have 6 attempts, using those you have to guess the 5 letter word by entering valid 5 letter words
to help you guess there are 3 highlights:
highlight 1: 🇼 hen the letter is in the word and in right position
highlight 2: 🅷 🆆 en the letter is in the word but not in position
highlight 3: 🄿 hen the letter is not in the word
highlight 4: when its not even a letter
lets begin: 
''')
    else:
        print("less than 5 letters")
    if attempt == 5:
            wordleflag = True
            print(f'answer is {word_answer}')