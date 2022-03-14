# hangman
import random

displayWord = []
wordList = ["hello", "goodbye", "yesterday", "today", "tomorrow"]
chosenWord = random.choice(wordList)
endgame = False
lilguy = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6

for letter in range(len(chosenWord)):
    displayWord.append("_")

while not endgame:

    userGuess = input("Guess a letter: ").lower()  # turn lowercase

    for i in range(len(chosenWord)):  # i is for num index, x is for string
        letter = chosenWord[i]
        if letter == userGuess:
            displayWord[i] = letter
    if userGuess not in chosenWord:
        lives -= 1
        print(lilguy[lives])
        if lives == 0:
            endgame = True

    print(f"{''.join(displayWord)}")

    if "_" not in displayWord:
        endgame = True
        print("You win!")

print(lilguy[lives])
print("you lose): ")
