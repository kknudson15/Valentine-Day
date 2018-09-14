#Exercise 36
#Focus: Create your own game

from sys import exit

def breakfast():
    print("""
    Good decision. You avoided sure demise for a little bit longer. Tread carefully! What is your next move?
                 Suggest a Special Lady Day or Try to fool around.
    """)
    choice2 = input(">")
    if "Suggest" in choice2:
        SLD()
    elif "Try" in choice2:
        sex()
    else:
        print("Her anger boils over and kills you before you can act!!!")

def sleep():
    print("""
    What were you thinking? You haven't done anything yet!! Be careful she is getting more angry better do something! What do you do now?
    Suggest a Special Lady Day or Try to fool around.
    """)
    choice2 = input(">")
    if "Suggest" in choice2:
        SLD()
    elif "Try" in choice2:
        sex()
    else:
        print("Her anger boils over and kills you before you can act!!!")

def SLD():
    print("""
    You bought yourself some time to figure out what to do for dinner.  Lucky you, don't screw this up! What are you going to decide to do?
        Try to make a last minute reservation or Have a candlelight dinner?
    """)
    choice3 = input(">")
    if "Try" in choice3:
        reservation()
    elif "Have" in choice3:
        candledinner()
    else:
        print("Her anger boils over and kills you before you can act!!!")

def sex():
    print("""
    You get shut down! What were you thinking? You really are thick in the skull. Better salvage the situation or the couch it is! What do you do?
        Try to make a last minute reservation or Have a candlelight dinner?
    """)
    choice3 = input(">")
    if "Try" in choice3:
        reservation()
    elif "Have" in choice3:
        candledinner()
    else:
        print("Her anger boils over and kills you before you can act!!!")
def reservation():
    print("""
    All of the restaurants in town are booked up! You have no plans you idiot! prepare to face the wrath of your lady. 
    """)
    dead()
def candledinner():
    print("You sly fox!! you survived another day ;)")
    happyending()
def happyending():
    print("You made the day special for your girlfriend! You avoid sleeping on the couch")

def dead():
    print("""
    You are banished to the couch with little hope of returning from this lost land! Maybe next time don't be an idiot!
    """)
    exit(0)

def start():
    print("""                           
                                            Valentine's Day 
    _________________________________________________________________________________________________________________________
    
    It is valentine's day, you awake from a deep slumber. you have not done anything for your girlfriend yet. What do you do? 
                 Sneak out of bed to cook her breakfast or Go back to sleep?
    """)
    choice1 = input(">")

    if "Sneak" in choice1:
        breakfast()

    elif "Go" in choice1:
        sleep()
    else:
        print("Her anger boils over and kills you before you can act!!!")

start()