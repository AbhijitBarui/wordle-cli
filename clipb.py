from multiprocessing.dummy import Array
import random

def load_dict(file_name):
    file = open(file_name)
    words = file.readlines()
    file.close()
    return [word[:5].upper() for word in words]

words_dict = load_dict("wordle_words.txt")
word_answer = random.choice(words_dict)

wordleflag = False
attempt_count = 6
H1 = "👍" #highlight1
H2 = "✋" #highlight2
H3 = "👎" #highlight3


def wordleChecker(arrans: Array, arrsam: Array):
    wordle_return=[]
    for ltr1 in arrsam:
        for ltr2 in arrans:
            if ltr1 == ltr2: #H1/H2 filter
                if arrans.index(ltr1) == arrsam.index(ltr2): #check_3_1: H1 filter
                    print(f'{ltr1} {H1}')
                    break
                else:
                    print(f"{ltr1} {H2}")
                    break
            if ltr1 not in arrans:
                print(f"{ltr1} {H3}")
                break
    return wordle_return

while wordleflag == False:
    for attempt in range(attempt_count):
        sample = input(f'attempt no. {attempt + 1}, enter the word: ')
        #check 1 check of same words: whether the words are same
        if sample == word_answer:
            print("you guessed it right")
            wordleflag = True
            break
        else:
            #check 2 check of same letters: whether there are common letters or not
            arr_answer = list(word_answer.upper())
            arr_sample = list(sample.upper())
            wordleChecker(arr_answer, arr_sample)
        if attempt == 5:
            wordleflag = True
            print(f'answer is {word_answer}')

