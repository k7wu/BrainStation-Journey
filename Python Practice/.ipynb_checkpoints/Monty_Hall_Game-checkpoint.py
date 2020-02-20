#import Numerical Python to use some of it's features
import numpy as np

#Set Up Game Function
def monty():
    '''
    the Monty Hall game is a game show game where three doors are available to choose.
    Behind one door is a price (a car) and the other two are empty

    The player chooses a door. The show host, Monty, then opens an unchosen door.
    This door is revealed to be empty. Monty then offers the player an opportunity
    to keep their original choice, or to switch and go with the un-yet chosen door.
    '''

    #creating a list to represent door choices - this will also serve as the list of possible
    #door choices
    doors = [1, 2, 3]

    #let's choose a winning door number
    winningdoor = np.random.randint(1,4)

    #remove the winning door number from our door list
    doors.remove(winningdoor)

    #Let's set up a dictionary to declare what is behind each door
    winning_dict = {winningdoor: "Car"}

    #input time! choose a door
    choice = int(input("Please choose a door - '1', '2', or '3': "))

    #if the choice is the winning door, it won't be able to be removed
    #from the doors list as it was removed aboce. Let's skip this line if so.
    try:
        doors.remove(choice) #for the switch stay moment
    except ValueError:
        pass

    montydoor = np.random.choice(doors) #monty can reveal any door but the prize door
    print('Monty has opened door',str(montydoor))
    print('Door', str(montydoor),'is empty')
    choice2 = str(input("Would you like to 'switch' or 'stay'"))
    if choice2 == 'switch':
        doors.append(winningdoor)
        doors.remove(montydoor)
        choice = doors[0]
        print('Your choice is now door',str(choice))
        if choice == winningdoor:
            print('You Win a', winning_dict[winningdoor])
        else:
            print('The door is empty. You Lose.')
    elif choice2 == 'stay':
        if choice == winningdoor:
            print('You Win a', winning_dict[winningdoor])
        else:
            print('The door is empty. You Lose.')
    else:
        print('That is not a valid choice')

    assert isinstance(choice,int) #input must be an integer
    assert isinstance(choice2,str) #input must be a string
