#imports the ability to get a random number (we will learn more about this later!)
from random import *

print("What Disney movie should you watch?")#Create the list of words you want to choose from.
aList = ["Moana", "Incredibles 2", "Incredibles", "The Little Mermaid", "Frozen", "Coco", "A Wrinkle in Time", "Wreck-It Ralph", "Zootopia"]

#Generates a random integer.
aRandomIndex = randint(0, len(aList)-1)
print(aList[aRandomIndex])

print("What should you eat today?")
firstCourse = ["Oysters au gratin", "Seared scallops and fruit", "Stuffed mushrooms"]
secondCourse = ["Bouillabaisse", "French onion soup", "Ratatouille"]
thirdCourse = ["Grilled salmon", "Pork chops with mushroom sauce", "Filet mignon"]
fourthCourse = ["Caesar salad" "Mimosa salad", "Salad with a strawberry poppyseed vinagrette"]
fifthCourse = ["Aged Cheddar, Camembert, and Parmigiano Cheese", "Comte, Brie, and Manchego Cheese", "Goat Gouda, Brillat-Savarin, and Mimolette Cheese"]
sixthCourse = ["Cheesecake", "Devil's food cake", "German chocolate cake"]

aRandomIndex1 = randint(0, len(firstCourse)-1)
aRandomIndex2 = randint(0, len(secondCourse)-1)
aRandomIndex3 = randint(0, len(thirdCourse)-1)
aRandomIndex4 = randint(0, len(fourthCourse)-1)
aRandomIndex5 = randint(0, len(fifthCourse)-1)
aRandomIndex6 = randint(0, len(sixthCourse)-1)

print("First course: " + firstCourse[aRandomIndex1])
print("Second course: " + secondCourse[aRandomIndex2])
print("Third course: " + thirdCourse[aRandomIndex3])
print("Fourth course: " + fourthCourse[aRandomIndex4])
print("Fifth course: " + fifthCourse[aRandomIndex5])
print("Sixth course: " + sixthCourse[aRandomIndex6])
