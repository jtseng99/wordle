import random
from colorama import init, Fore, Back, Style

#initialize colors
init(autoreset=True)

#read word file
infile = open("words2.txt","r")
words = [line.rstrip("\n").upper() for line in infile]
infile.close()

#choose random word
word = random.choice(words)

#remain letters
letters = [chr(k) for k in range(65,91)]

#start game
for j in range(5):
    print("\nGuess",j+1)
    print("Remaining letters:",letters)
    guess = input().upper()
    
##    #validate the guess word
##    while guess != words:
##        print("Invalid word! Try again:",end='')
##        guess = input().upper()

    if guess == word:
        print("Nice work!",Fore.BLACK + Back.GREEN + guess)
        break
    
    for i in range(5):
        if guess[i] == word[i]:
            print(Fore.BLACK + Back.GREEN + guess[i],end='')
        elif guess[i] in word:
            print(Fore.BLACK + Back.YELLOW + guess[i],end='')
        else:
            print(Fore.WHITE + Back.BLACK + guess[i],end='')
            if guess[i] in letters:
                letters.remove(guess[i])

    print()

print("Correct word:", Fore.BLACK + Back.GREEN + word)
