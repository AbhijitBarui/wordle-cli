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
H1 = "✅" #highlight1
H2 = "🔄" #highlight2
H3 = "❌" #highlight3


def wordleChecker(arrans: Array, arrsam: Array):
    wordle_return=[]
    wordle_word = ""
    for idx1, ltr1 in enumerate(arrsam):
        wordle_return.append(ltr1)
        for idx2,ltr2 in enumerate(arrans):
            if ltr1 == ltr2: #H1/H2 filter
                if idx1 == idx2: #check_3_1: H1 filter
                    wordle_return.append(H1)
                    arrans.pop(idx2)
                    arrans.insert(idx2,'%')
                    break
                else:
                    wordle_return.append(H2)
                    break
            if ltr1 not in arrans:
                wordle_return.append(H3)
                break
    even_count = 0
    for wordle_letters in wordle_return:
        wordle_word+=str(wordle_letters) + "   "

    return wordle_word

print(word_answer)
for attempt in range(attempt_count):
    sample = input(f'attempt no. {attempt + 1}, enter the word: ')
    if sample.upper()==word_answer:
        print("correct guess")
        break
    if len(sample) == 5:
        #check 1 check of same words: whether the words are same
        arr_answer = list(word_answer.upper())
        arr_sample = list(sample.upper())
        print(wordleChecker(arr_answer, arr_sample))
    else:
        print("less than 5 letters")
    if attempt == 5:
            wordleflag = True
            print(f'answer is {word_answer}')