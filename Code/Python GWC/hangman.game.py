word = input("Type a word for someone to guess: ")

print("The word has", len(word), "letters.")

# Converts the word to lowercase
word = word.lower()

# Checks if only letters are present
if(word.isalpha() == False):
	print("That's not a word!")

# Some useful variables

guesses = [1, 2, 3, 4, 5]
maxfails = 6

guess = 1
while True:
	print("Guess a letter:")
	user_Input = input()
	print(user_Input in word)
	#guess += 1
