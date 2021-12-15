from sys import exit

def gold_room():
    ''' A truck is full to the top with cash '''
    print "This truck is full of cash.  How much do you take?"

    next = raw_input("> ")

    try:
         how_much = int(next)
    except ValueError:
        dead("Bro, do you know how to type.")

    if how_much < 50:
        print "Great, you are not that greedy, you win!"
        exit(0)
    else:
        dead("You bastard took more money than you needed!")


def bear_room():
    ''' A truck with a gaurd outside of it '''
    print "There is money here in a truck."
    print "How are you going to move the truck?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take truck":
            dead("The gaurd looks at you then points his gun.")
        elif next == "shoot guard" and not bear_moved:
            print "The gaurd has moved, you must shoot him now!"
            bear_moved = True
        elif next == "taunt gaurd" and bear_moved:
            dead("The gaurd gets pissed off and shoots your arm off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I don't think that's a good idea..."

def dead(why):
    ''' Call this when the hero dead '''
    print why, "Good job!"
    exit(0)

def start():
    ''' Begining of the story '''
    print "You are on a dark road."
    print "There is a road to your right and left."
    print "Which one do you take?"

    next = raw_input()

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
