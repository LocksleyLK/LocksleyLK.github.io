#Setup-
while True:
	word = input("Type a word for someone to guess: ")
	word = word.lower()
	if(word.isalpha() == False):
		print("That's not a word!")
	else:
		break

# Some useful variables
guesses = []
numfails = 0
maxfails = 7
wordToGuess = []

#set the underscore version of the word
for letter in word:
	wordToGuess.append("_")

#Space so the player can see the word!
for idx in range(0, 20):
	print(" ")

	done = False

while not done:
	#Print the status of the game
	print("____________________")
	print("Lives left: ", maxfails - numfails)
	print("Guesses so far: ", guesses)
	print("Current Word: ", wordToGuess)

	#user input user makes a guesses
	



#guess = input("Guess a letter: ")
