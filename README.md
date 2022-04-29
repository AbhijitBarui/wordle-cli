# wordle-cli

how game works?

you will be given 6 chances
you have to enter a valid 5-letter word each try
you will be informed each time whether the letters in the word-
> highlight1 if letter is in correct place
> highlight2 if letter is is word but not in correct place
> highlight3 if letter is not in word

algorithm:
resources needed:
wordlist

procedure:
start game
take one random word as answer from wordlist
take input of a 5 letter word call it sample
break the answer and sample into arrays
perform checks(detailed below)
provide necessary highlights to letters and make output
if correct word then celebrate
if not then continue next step till sixth attempt
stop game

checks:
two arrays arr_sample_x (x refers to xth trial) and arr_answer made up
of the letters of the words sample_x and answer respectively
check_1: check of same words: whether the words are same
check_2: check of same letters: whether there are common letters or not
check_2_1: if common letters: extract common letters
check_2_2: if not common letters: highlight all with H3 and print results breakloop then continue
check_3: if common letters are in correct places
check_3_1: if in correct place: highlight them with H1
check_3_2: if not in correct place: highlight them with H2
check_3_3: highlight rest with H3 print results then continue



input="space"
ans="sweet"
output=s[1] p[3] a[3] c[3] e[2]
