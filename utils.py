## important modules ##


#help text
help_text = '''
                        :Welcome to Wordle:
The rules are simple
You have 6 attempts, using those you have to guess the 5 letter word by entering valid 5 letter words
to help you guess there are 3 highlights:
highlight 1: 🇼 hen the letter is in the word and in right position
highlight 2: 🅷 🆆 en the letter is in the word but not in position
highlight 3: 🄿 hen the letter is not in the word
highlight 4: when its not even a letter
type help to see this message again but remember it takes away a valuable attempt!!
warning: inputs below lettercount of 5, invalid words or invalid characters are counted as attempt!!
lets begin!!
'''

#dictionary loader function
def load_dict(file_name, r, flg="Foo"):
    file = open(file_name)
    words = file.readlines()
    file.close()
    if flg.lower() == "u":
        return [word[:r].upper() for word in words]
    elif flg.lower() == "l":
        return [word[:r].lower() for word in words]
    else:
        return [word[:r] for word in words]


#highlighter function
def highlighter(word, dict_h):
    for letter in word:
        if letter in dict_h.keys():
            for key, value in dict_h.items():
                if letter.lower() == key: return value ;break
        else: return "❓"


#wordleChecker function
def wordleChecker(answer, sample, h1, h2, h3):
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