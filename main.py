# Created by:   Patrick Archer
# Date:         21 December 2018
# Copyright to the above author. All rights reserved.

"""

Directions - COMPLETE:
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game).

"""

# ################################################# start_funcs

def calcWhoWins (p1Selection, p2Selection):

    try:
        # if p1 selects rock
        if (p1Selection == "r"):
            if (p2Selection == "r"):
                return "tie"
            elif (p2Selection == "p"):
                return "p2"
            elif (p2Selection == "s"):
                return "p1"
            else:
                print("\n<ERROR>: Invalid response received for at least 1 player. Aborting operation.\n")
                return "err"
        # if p1 selects paper
        elif (p1Selection == "p"):
            if (p2Selection == "r"):
                return "p1"
            elif (p2Selection == "p"):
                return "tie"
            elif (p2Selection == "s"):
                return "p2"
            else:
                print("\n<ERROR>: Invalid response received for at least 1 player. Aborting operation.\n")
                return "err"
        # if p1 selects scissors
        elif (p1Selection == "s"):
            if (p2Selection == "r"):
                return "p2"
            elif (p2Selection == "p"):
                return "p1"
            elif (p2Selection == "s"):
                return "tie"
            else:
                print("\n<ERROR>: Invalid response received for at least 1 player. Aborting operation.\n")
                return "err"
        # if input error
        else:
            print("\n<ERROR>: Invalid response received for at least 1 player. Aborting operation.\n")
            return "err"
    except (ValueError):
        print("\n<ERROR>: Invalid sequence of events. Aborting operation.\n")
        return "err"



# ################################################# end_funcs/start_main

trigger_gameExit = False

while (trigger_gameExit == False):

    pause_beginGame = input("\nPress \"Enter\" when you would like to begin playing!\n")

    player1Selection = str(input("\nP1, please select your move. (Type the letter, then press \"Enter\")\n"
                             "\tR - Rock\n"
                             "\tP - Paper\n"
                             "\tS - Scissors\n")).lower()

    player2Selection = str(input("\nP2, please select your move. (Type the letter, then press \"Enter\")\n"
                             "\tR - Rock\n"
                             "\tP - Paper\n"
                             "\tS - Scissors\n")).lower()

    # run calcWhoWins
    result = calcWhoWins(player1Selection, player2Selection)

    print("\n#######################")

    # parse results, react according to outcome returned
    if (result == "p1"):
        print("\nP1 chose: " + str(player1Selection).upper() +
              "\nP2 chose: " + str(player2Selection).upper() +
              "\nThe result is: Player 1 wins!\n")
    elif (result == "p2"):
        print("\nP1 chose: " + str(player1Selection).upper() +
              "\nP2 chose: " + str(player2Selection).upper() +
              "\nThe result is: Player 2 wins!\n")
    elif (result == "tie"):
        print("\nP1 chose: " + str(player1Selection).upper() +
              "\nP2 chose: " + str(player2Selection).upper() +
              "\nThe result is: a tie!\n")
    elif (result == "err"):
        print("\n<CONSOLE>: The program has successfully recovered from a reported error.\n"
              "Continuing operation.\n")
    else:
        print("\n<ERROR>: Invalid sequence of events. Aborting operation.\n")

    print("#######################\n")

    # prompt user to play again or quit
    pause_playAgain = str(input("Would you would like to play again?\n"
                            "--> Please type \"Y\" or \"N\" and press enter.\n")).lower()

    # handle what to do if user does/does not want to play again; handle errors from user input
    if (pause_playAgain == "y"):
        trigger_gameExit = False
    elif (pause_playAgain == "n"):
        trigger_gameExit = True
        print("\nThanks for playing! Please restart the program to play again.")
        print("\n<CONSOLE>: Now exiting program.")
    else:
        print("\n<ERROR>: Invalid response received. Aborting program to prevent further catastrophe.\n")
        trigger_gameExit = True
        print("\nThanks for playing! Please restart the program to play again.")
        print("\n<CONSOLE>: Now exiting program.")

# ################################################# end_main





