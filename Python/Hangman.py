import string
from words import words
import random

def current_word(word):
    word=random.choice(words)
    if "_" in word and " " in word:
        word=random.choice(words)
    return word
def hangman():
    counter=0
    ans=set()
    word=current_word(words)
    letters=set(word)
    while counter<=7:
        user=input("Guess a letter: ").upper()
        valid=string.ascii_uppercase
        if len(user) == 1 and user in valid:
            if user.upper() in ans:
                print("You have already guessed this letter")
                counter+=1
            
                
            elif user.upper() in word.upper():
                ans.add(user.lower())
                print("Good ")
            
            else:
                print("Wrong, You have "+ str(7-counter)+" chances left")
                counter+=1
            if ans==letters:
                print("Congratulations")
                print("The word was "+ str(word))
        else:
            print("That is a wrong input,  "+ str(7-counter)+" chances left")
            counter+=1
    print("Time is up")
    print("The word was "+ str(word))
hangman()
                
                
            
    