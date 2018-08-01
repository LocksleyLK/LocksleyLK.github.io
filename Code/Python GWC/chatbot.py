# --- Define your functions below! ---
def isGreetingValidInput(input, response):
    if input in response:
        return True

def introduction():
    print("Hi!")
    hiInput = input()
    hiResponse = ["Hi", "Hello", "hi", "hello"]
    isGreetingValidInput(hiInput, hiResponse)
    print("My name is Colin the chatbot!")
    print("What is your name?")
    name_input = input()
    print("Hi, " + name_input + "!")
    print("We are going to talk about movies.")
    print("Do you want to talk about animated movies or live-action movies?")
    print("Type 'animated' to learn about animated movies or 'live action' to learn about live action movies!")

def printAnimatedMovieList():
    print("Ralph Breaks the Internet")
    print("The Lego Movie 2")
    print("How to Train Your Dragon 3")
    print("Toy Story 4")
    print("Frozen 2")

def printLiveActionMovieList():
    print("Fantastic Beasts and the Crimes of Grindelwald")
    print("Mary Poppins Returns")
    print("Aquaman")
    print("Captain Marvel")
    print("Star Wars: Episode IX")
    print("Spider-Man: Homecoming 2")

def firstInput():
    user_input = input()
    if user_input == "animated":
        print("")
        print("I love animated movies!")
        print("")
        print("Some animated movies that are coming out soon are:")
        printAnimatedMovieList()
        print("")
        print("Which movie are you looking forward to the most?")
        print("What movie are you most looking forward to?")
    elif user_input == "live action":
        print("")
        print("Live action movies are great!")
        print("")
        print("Some live action movies that are coming out soon are:")
        printLiveActionMovieList()
        print("")
        print("What movie are you most looking forward to?")

def areAnimatedMoviesValidInput(animatedMovieInput, animatedMovieResponse):
    if input in response:
        return True

def secondInput():
    animated_movie_input = input()
    hiInput = input()
    animatedMovieResponse = ["Hi", "Hello", "hi", "hello"]
    isGreetingValidInput(hiInput, hiResponse)
    if animated_movie_input == ["Ralph Breaks the Internet", "ralph breaks the internet"]:
        print("I also can't wait for " + animated_movie_input + "!")
        print("Ralph Breaks the Internet comes out November 21, 2018")
        print("Do you want to learn more about " + animated_movie_input + "?")
    elif animated_movie_input == "The Lego Movie 2":
        print("I also can't wait for " + animated_movie_input + "!")
        print("The Lego Movie 2 comes out February 8, 2019")
    elif animated_movie_input == "How to Train Your Dragon 3":
        print("I also can't wait for " + animated_movie_input + "!")
        print("How to Train Your Dragon 3 comes out March 1, 2019")
    elif animated_movie_input == "Toy Story 4":
        print("I also can't wait for " + animated_movie_input + "!")
        print("Toy Story 4 comes out June 21, 2019")
    elif animated_movie_input == "Frozen 2":
        print("I also can't wait for " + animated_movie_input + "!")
        print("Frozen 2 comes out November 27, 2019")

def thirdInput():
    live_action_movie_input = input()
    if live_action_movie_input == "Fantastic Beasts and the Crimes of Grindelwald":
        print("Fantastic Beasts and the Crimes of Grindelwald comes out November 16, 2018")
    elif live_action_movie_input == "Mary Poppins Returns":
        print("Mary Poppins Returns comes out December 19, 2018")
    elif live_action_movie_input == "Aquaman":
        print("Aquaman comes out December 21, 2018")
    elif live_action_movie_input == "Captain Marvel":
        print("Captain Marvel comes out March 8, 2019")
    elif live_action_movie_input == "Star Wars: Episode IX":
        print("Star Wars: Episode IX comes out December 20, 2019")
    elif live_action_movie_input == "Spider-Man: Homecoming 2":
        print("Spider-Man: Homecoming 2 comes out July 5, 2019")


# --- Put your main program below! ---
def main():
    introduction()
    firstInput()
    secondInput()
    thirdInput()
    #while True:
        #answer = input("(What will you say?) ")
        #print("That's cool!")


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
