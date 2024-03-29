import random

title = "The Great Very Super Original Word Game"

#initializing and populating word bank
bank = []
numWords = 281

#opening word bank file - may have to change path name 
file = open(r"word-bank.txt","r") 

for x in range(numWords - 1):
    bank.append((file.readline()).lower().strip())

file.close()

#choosing word to be guessed
word = random.choice(bank)

#initializing variables
misplacedLetters = []
incorrectLetters = []
maxTurns = 5
currentTurns = 0
rightGuess = False 

#welcome 
print(f"Welcome to {title}. The secret word has 5 letters.\n")
print(f"You have {maxTurns - currentTurns} remaining guess(es).\n")

#game
while currentTurns < maxTurns and rightGuess == False:
    inputGuess = input("What is your guess? ")
    userGuess = inputGuess.lower()
    if userGuess.isalpha() and len(userGuess) == 5: #valid guess
        currentTurns += 1
        if userGuess == word:
            rightGuess = True
        index = 0 #initial index
        while not rightGuess and index < 5:
            if userGuess[index] == word[index]:
                print(word[index], end="")
                if word[index] in misplacedLetters:
                    misplacedLetters.remove(word[index])
                index += 1
            elif userGuess[index] in word:
                print("_", end="")
                if userGuess[index] not in misplacedLetters:
                    misplacedLetters.append(userGuess[index])
                index += 1
            else:
                print("_", end="")
                if userGuess[index] not in incorrectLetters:
                    incorrectLetters.append(userGuess[index])
                index += 1
        if not rightGuess:
            print("\n")
            print(f"Misplaced letters: {misplacedLetters}")
            print(f"Incorrect letters: {incorrectLetters}")
            print(f"You have {maxTurns - currentTurns} remaining guess(es).\n")
    else: #invalid guess
        print("Guess must contain only letters and be 5 letters long.\n")

#win/loss messages
if rightGuess:
    print(f"\nCongratulations! The word was {word}!\n")
else:
    print(f"\nYou're an idiot. The word was {word}.\n")
