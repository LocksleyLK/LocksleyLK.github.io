#imports the ability to get a random number (we will learn more about this later!)
from random import *

print("What Disney movie should you watch?")#Create the list of words you want to choose from.
aList = ["Moana", "Incredibles 2", "Incredibles", "The Little Mermaid", "Frozen", "Coco", "A Wrinkle in Time", "Wreck-It Ralph", "Zootopia"]

#Generates a random integer.
aRandomIndex = randint(0, len(aList)-1)
print(aList[aRandomIndex])
