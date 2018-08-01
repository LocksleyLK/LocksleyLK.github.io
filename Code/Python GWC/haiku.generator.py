#imports the ability to get a random number (we will learn more about this later!)
from random import *

print("We are going to generate a Haiku today.")
print("Do you want to generate a modern haiku or a traditional haiku?")
print("Type 'modern' for a modern haiku and 'traditional' for a traditional haiku!")
print("")
user_input = input()
if user_input == "traditional":
    line1 = ["An old silent pond...", "Autumn moonlight--", "In the twilight rain", "A summer river being crossed", "Light of the moon", "In the moonlight", "O snail", "Trusting the Buddha, good and bad", "Everything I touch"]
    line2 = ["A frog jumps into the pond,", "a worm digs silently", "these brilliant-hued hibiscus--", "how pleasing", "Moves west, flower's shadows", "The color and scent of the wisteria", "Climb Mount Fuji", "I bid farewell", "with tenderness, alas,"]
    line3 = ["splash! Silence again.", "into the chestnut", "A lovely sunset", "with sandals in my hands!", "Creep eastward.", "Seems far away.", "But slowly, slowly!", "To the departing year.", "pricks like a bramble"]

    #Generates a random integer.
    aRandomIndex1 = randint(0, len(line1)-1)
    aRandomIndex2 = randint(0, len(line2)-1)
    aRandomIndex3 = randint(0, len(line3)-1)

    print("")
    print(line1[aRandomIndex1])
    print(line2[aRandomIndex2])
    print(line3[aRandomIndex3])

    print("")
    print("Credit to Basho Matsuo, Yosa Buson, and Kobayashi Issa for their haikus!")

elif user_input == "modern":
    modernline1 = ["From across the lake,", "Lily:", "ground squirrel", "Nightfall," "meteor shower"]
    modernline2 = ["Past the black winter trees,", "out of the water", "balancing its tomato", "Too dark to read the page", "a gentle wave"]
    modernline3 = ["Faint sounds of a flute.", "out of itself", "on the garden fence", "Too cold.", "wets our sandals"]

    aModernRandomIndex1 = randint(0, len(modernline1)-1)
    aModernRandomIndex2 = randint(0, len(modernline2)-1)
    aModernRandomIndex3 = randint(0, len(modernline3)-1)

    print("")
    print(modernline1[aModernRandomIndex1])
    print(modernline2[aModernRandomIndex2])
    print(modernline3[aModernRandomIndex3])

    print("")
    print("Credit to Richard Wright, Nick Virgilio, Don Eulert, Jack Kerouac, and Michael Dylan Welch for their haikus!")
