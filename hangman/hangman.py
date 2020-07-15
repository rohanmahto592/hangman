import random
name=input("enter you name!!")
print(f"so you are here to play hangman game{name}and good luck!!")
words=['rainbow','best','sunflower','sports','scooty','love']
word=random.choice(words)
gusses=' '
turns=10
while turns>0:
    fail=0
    for char in word:
        if char in gusses:
            print(char)
        else:
            print("_")
            fail+=1
    if fail==0:
        print("YOU WON")
        print(f"the word is:{word}")
        break
    guess=input("guess the character")
    gusses+=guess
    if gusses not in word:
        turns-=1
        print("wrong")
        print(f"you have only {turns} left for guessing")
        if turns==0:
            print("you loose")
            
