__author__ = "Gregory Chekler"
import time

"Creates a story using inputted words"

def main():
    # User Interface greeting
    print("Hello! Welcome to Greg's mad libs game.") 

    print("                                                              ")


    # differentiating gender
    gender = input("What is your gender(male or female)? ")
    if gender == "male":
        pronoun_1 = "he"
        pronoun_2 = "him"
        pronoun_3 = "his"
    else:
        pronoun_1 = "she"
        pronoun_2 = "her"
        pronoun_3 = "her"

    # define variables
    month = input("Please 'input' a month: ")
    name = input("Please 'input' a name(uppercase): ")
    name = str("\"" + name + "\"") # quotes around name
    animal = input("Please 'input' an animal: ")
    nickname = input("Please 'input' a nickname(uppercase): ")
    nickname = str("\"" + nickname + "\"") # quotes around nickname
    past_verb = input("Please 'input' a past verb: ")
    location = input("Please 'input' a location: ")
    building = input("Please 'input' a building: ") 
    food = input("Please 'input' a food: ")
    sound = input("Please 'input' a sound: ")
    verb_two = input("Please 'input' a verb: ")
    household_appliance = input("Please 'input' a household appliance: ")
    noun = input("Please 'input' a noun: ")
    verb_three = input("Please 'input' a verb: ")
    noun_two = input("Please 'input' a noun: ")
    descriptive = input("Please 'input' a adjective: ")
    TV_show = input("Please 'input' a TV show: ")
    number = float(input("Please 'input' a number: "))# convert to float
    thing = input("Please 'input' a thing: ")
    base = float(input("Please 'input' a number: "))# convert to float

    # User interface
    print("                                                              ")
    time.sleep(.2)
    print("Generating ... " )
    print("                                                              ")
    time.sleep(.2)
    print("Generating ... " )
    time.sleep(1)
    print("                                                              ")
    print("Great! I will now make a mad libs out of your inputted words.")
    print("                                                              ")

    # printing story
    print("Once upon a time in the month of", month.capitalize(), ",", name,
          " was walking", pronoun_3, "animal",
          nickname, "down the street.", "The", animal, 
          "was on a leash but it soon got loose. The",
         animal, past_verb, "away leaving", name, "alone.", 
         name, "went to", location, "in search of", pronoun_3, "pet.", 
          "While walking down a street", pronoun_1, "saw a", building,
          "being torn down.", 
          name,  "ran into the", building, "and started searching for",
          pronoun_3, animal + ".",  
          pronoun_1.capitalize(), "yelled,", nickname, "over and over but could not find"
          , nickname + ".", 
          pronoun_1.capitalize() + " took out some " + food + " in hopes that " + nickname +
          " would come. " + 
          name + " heard a " + sound + " that " + pronoun_1 + " knew was " +
          nickname[0:-1] + "’s\". " + 
          "It was coming from the " + household_appliance +
          " and there " + pronoun_1 + " found " + nickname + ". " +
          "The " + building + " started " + verb_two +
          "ing and everything was begining to collapse." + 
          " A", noun, "fell on", name[0:-1] + "’s\" head but", name, "kept", 
          verb_three + "ing.", 
          "They came across a",  thing,  "that was",  number, "feet tall. " +
          name + " was such a math enthusiast that " + pronoun_1 +
          " calculated the area of the "
          + thing + " by figuring out its base. " +
          name + " measured the " + thing + "'s base and determined it was ", base,
          " feet. " +
          "The total area of the", thing, "was",  (base * number), 
          " feet. Just as " + name +  " and " + nickname +
          " ran out of the " + building + " it exploded. " + 
          "Peices of " + noun_two +  " flew everywhere. " + 
          name +  " and " + nickname + " went back to their " + descriptive +
          " house and turned on the TV to watch " + TV_show +
          " which had a character length of",  int(len(TV_show)), ".")

    time.sleep(15)

    #UI
    print(" ")
    print("I hope you enjoyed the story. Have a nice day!!!")

main()
