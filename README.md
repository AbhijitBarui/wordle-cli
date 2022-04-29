# WORDLE CLI VERSION (Python) - 
# Assignment Submission related to the post of Associate Software Developer @ Coditation Systems 
By Abhijit Barui            Ph: +91-8335076174              email: abhijitongit@gmail.com

# Description:
        This project is based on the popular game called Wordle. The goal is to guess a 5 letter word and one is given a certain number of attempts(6). Whenever one makes a guess, all those letters in the guess that also appears in the correct answer are highlighted, if they are in the right spot they are highlighted seperately. 

# requirements
        Python programming language installed in the desktop environment
        Terminal

# how-to-play:
        To play this game first you have to navigate to wordle.py after cloning this repository
        (../clone_folder/wordle-cli/wordle.py) and then run ~$ /bin/python3 wordle.py
        the game should be up and working perfectly. Type in your attempts in the terminal and press enter key.

# Challenges faced while making this:
        •First challenge was to read the text file of words and form a list of words. Learnt about pyhon file handling    methods as well as single-line return statement while completing this task.

        •While working with the highlighter I learned more about iterating methods through dictionary in python(used to scan highlight dictionaries and replace the letters with highlighted characters).

        •While facing list of emotes to be served as a dict I learned about the zip() and dict() methods to use two list of keys and values respectively and create a python dictionary.

        •After creating utility module(utils.py) and moving functions over there, I faced error: 
        NameError: name 'h3' is not defined
        It means my imported module isn't recognising the variables(Visibility of global variables in imported modules)

        •Learned about enumerate() method while facing indexing error(presence of duplicate is ignored and index of first duplicate is always taken into account). Solved.