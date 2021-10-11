import random

# Opening and importing words and definitions from the configuration files
unstrippedWordsToGuess = []
unstrippedDefinitions = []

wordsToGuess = []
definitions = []

wordsFile = open('config.txt','r',encoding='utf-8-sig')
unstrippedWords = wordsFile.readlines()
for i in range(0,len(unstrippedWords) - 1,3):
  unstrippedWordsToGuess.append(unstrippedWords[i])

for i in range(1,len(unstrippedWords) - 1,3):
  unstrippedDefinitions.append(unstrippedWords[i])

for word in unstrippedWordsToGuess:
  wordsToGuess.append(word.strip('\n'))

for definition in unstrippedDefinitions:
  definitions.append(definition.strip('\n'))

# Greeting the player
def greeting():
  print("Word guessing\n")
  print("You will be given a word encoded in underscores. You have a certain number of tries to guess the letter. For every guess, you are required to enter ONLY 1 letter. For each letter guessed correctly, you are given 50 points. For each letter guessed incorrectly, 25 points will be taken from you. Try your best to make sure that you have the highest score in the least tries.\n")

# Selecting a word and its corresponding definition
wordToGuess = ""
definition = ""
def selection():
  global wordToGuess
  global definition
  wordToGuess = random.choice(wordsToGuess)
  definition = definitions[wordsToGuess.index(wordToGuess)]

# Main game mechanics:
def main():
  greeting()
  selection()
  
  # Preparation
  textBox = []
  positions = []
  correctlyGuessedLetters = []
  check = False
  tries = len(wordToGuess) * 2
  start = True
  repeat = False
  score = 0

  # Filling the textbox
  for a in range(len(wordToGuess)):
    textBox.append("*")
  print ("This word has ", len(wordToGuess), "letters")
  print(''.join(textBox))
  print("Definition:", definition)
  
  while start == True:
    while True:
      print("You have", tries, "tries")
      print("Score:", score)
      guessedLetter = input("Enter a letter to guess the word here: ")
      guessedLetter = guessedLetter.lower()
      if len(guessedLetter) == 1:
        for position in range(len(wordToGuess)):
          if guessedLetter == wordToGuess[position]:
            positions.append(position)
            check = True

        for correctlyGuessedLetter in correctlyGuessedLetters:
          if guessedLetter == correctlyGuessedLetter:
            repeat = True
              
        if check == True and repeat == False:
          for position in positions:
            textBox[position] = guessedLetter
            correctlyGuessedLetters.append(guessedLetter)
            score += 50
          print("You have guessed", len(correctlyGuessedLetters), "letters correctly.\n")
          tries -= 1

        elif repeat == True:
          print("This letter has already been guessed\n")
        
        else:
          print("Incorrect guess\n")
          tries -= 1
          if score >= 25:
            score -= 25

        check = False
        positions = []
        repeat = False

        print(''.join(textBox))
          
        if len(correctlyGuessedLetters) == len(wordToGuess):
          print("You have successfully guessed the word with", tries, "tries left! Congrats! The word was \"",wordToGuess,"\"")
          print("Your score was:", score)
          break

        if tries == 0:
          print("You have run out of tries. Game over. The word was \"",wordToGuess,"\"")
          break

      else:
        print("Invalid input. Requires only 1 letter.\n")

    startQuestion = input("Do you want to play again? Enter Y or N: ")
    startQuestion = startQuestion.upper()
    while startQuestion != "Y" and startQuestion != "N":
      startQuestion = input("Please enter only Y or N: ")
      startQuestion = startQuestion.upper()
    if startQuestion == "Y":
      greeting()
      selection()

      textBox = []
      positions = []
      correctlyGuessedLetters = []
      check = False
      tries = len(wordToGuess) * 2
      start = True
      repeat = False
      score = 0
      
      for a in range(len(wordToGuess)):
        textBox.append("*")
      print ("This word has ", len(wordToGuess), "letters")
      print(''.join(textBox))
      print("Definition:", definition)
    else:
      start = False

main()
wordsFile.close()