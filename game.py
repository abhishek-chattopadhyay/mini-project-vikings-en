import time
import sys
import random
from vikingsClasses import Soldier, Viking, Saxon, War
import names

#Intro
def star_wars_intro():
    intro_text = """
    A long time ago in a land far, far away
    The mighty Vikings, fierce and relentless, have set sail 
    from the frozen north, seeking conquest and glory. 
    Meanwhile, the Saxons, stalwart defenders of their fertile lands,
    stand ready to repel the invaders.
    A great battle is about to begin, a clash of steel and willpower
    that will determine the fate of the realm.
    Who will emerge victorious in this epic war?
    Let the battle begin!
    """

    for line in intro_text.split("\n"):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print()

#User imput
def get_user_input():

    # Input Vikings
    while True:
        try:
            viking_warriors = int(input("Enter the number of Viking warriors: "))
            if viking_warriors <= 0:
                print("Viking armie must have at least one warrior. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    #Input Saxons
    while True:
        try:
            saxon_warriors = int(input("Enter the number of Saxon warriors: "))
            if saxon_warriors <= 0:
                print("Saxon armie must have at least one warrior. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
        
    return [viking_warriors, saxon_warriors]

#User bet
def get_user_bet():
    while True:
        user_bet = input("Who do you think will win? Type 'Vikings' or 'Saxons': ").strip().lower()
        if user_bet in ["vikings", "saxons"]:
            return user_bet.capitalize()
        print("Invalid choice. Please type 'Vikings' or 'Saxons'.")

# Generate a random list of names
def generate_realistic_names(count):
    return [names.get_full_name() for name in range(count)]

def main():

    #Intro
    
    star_wars_intro()

    ########################### Enter an image to start the war ######################################

    #User imput
    army_count = get_user_input()
    user_bet = get_user_bet()

    ########################### Enter a sound to start the battle ######################################
    
    time.sleep(1)
    print("\nLet the battle decide the fate of the realm\n")
    time.sleep(1.5)

    #Let's begin the army construction
    great_war = War()

    #Create Vikings
    list_names = generate_realistic_names(army_count[0])
    for i in range(0,army_count[0]):
        if i:
            great_war.addViking(Viking(random.choice(list_names),100,random.randint(0,100)))

    #Create Saxons
    for i in range(0,army_count[1]):
        if i:
            great_war.addSaxon(Saxon(100,random.randint(0,100)))
    
    #Let's begin the war
    round = 0
    war_result = ""
    while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        great_war.vikingAttack()
        great_war.saxonAttack()
        #print(f"round: {round} // Viking army: {len(great_war.vikingArmy)} warriors",f"and Saxon army: {len(great_war.saxonArmy)} warriors")
        #print(great_war.showStatus())
        war_result = great_war.showStatus()
        round += 1

    ########################### Enter a sound to finish the battle ######################################

    print("War has ended\n")
    #Lets show the war results 
    print (war_result)

    #Lets se the bet results
    if user_bet.lower() in war_result.lower():
        print(f"Congratulations! You guessed right, {user_bet} won!\n")
        ########################### Enter a happy face ######################################

        ########################### Enter a happy sound ######################################
    else:
        print(f"\nBetter luck next time!\n") 
        ########################### Enter a sad face ######################################   

        ########################### Enter a sad sound ######################################

    print(f"Let's play again!")

# Run the game
if __name__ == "__main__":
    #playsound('/Users/debbie/Downloads/Ironhack2.m4a')
    main()