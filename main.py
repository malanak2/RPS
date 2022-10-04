import random
import os

def chooseGame():
    print("1 for rock-paper-scissors")
    print("2 Available in full release")
    print("3 Available in full release")
    inp = input()
    if inp == "1":
        return "RPS"
    elif inp == "NULL":
        chooseGame()
    elif inp == "NULL":
        chooseGame()
    elif inp == "dev":
        return "dev"
    else:
        rturn = chooseGame()
        return rturn

class Game:
    def __init__(self):
        print("")
        #Intended for multi-games, but no ideas what they might be, so...

class RPS(Game):
    #Hands source: https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
    rock = """
                                _______
                            ---'   ____)
                                  (_____)
                                  (_____)
                                 (____)
                            ---.__(___)
                            (rock)"""
    paper = """
                            __________
                        ---'    ______)____
                                   ________)
                                  _________)
                                 _________)
                        ---.____________)
                        (paper)"""
    scissors = """
                            _______
                        ---'   ____)____
                                  ______)
                               __________)
                              (____)
                        ---.__(___)
                        (Scissors)"""
    def __init__(self):
        pass
    def choose(self):
        global rock
        global paper
        global scissors
        inptext = "Choose:\n1. Rock\n2. Paper\n3. Scissors\n"
        inp = input(inptext)
        match inp:
            case "1":
                return "1"
            case "2":
                return "2"
            case "3":
                return "3"
            case _:
                inc = self.choose()
                return inc

    def choosepc(self):
        pcchoice = random.randint(1, 3)
        return pcchoice

def play(game):
    if game == "RPS":
        rps = RPS()
        plchoice = rps.choose()
        pcchoice = rps.choosepc()
        match plchoice:
            case "1":
                plicon = rps.rock
            case "2":
                plicon = rps.paper
            case "3":
                plicon = rps.scissors
        match pcchoice:
            case 1:
                pcicon = rps.rock
            case 2:
                pcicon = rps.paper
            case 3:
                pcicon = rps.scissors
        print("You:")
        print(plicon)
        print("Opponent:")
        print(pcicon)
        if plchoice == "1" and pcchoice == 1:
            print("Its a draw!")
        elif plchoice == "1" and pcchoice == 2:
            print("Opponent won!")
        elif plchoice == "1" and pcchoice == 3:
            print("You won!")
        elif plchoice == "2" and pcchoice == 1:
            print("You won!")
        elif plchoice == "2" and pcchoice == 2:
            print("Its a draw!")
        elif plchoice == "2" and pcchoice == 3:
            print("Opponent won!")
        elif plchoice == "3" and pcchoice == 1:
            print("Opponent won!")
        elif plchoice == "3" and pcchoice == 2:
            print("You won!")
        elif plchoice == "3" and pcchoice == 3:
            print("Its a draw!")
        else:
            print(f"An internal error has occured. Please conact the dev with the following info: plc: {plchoice}, pcc: {pcchoice}")
        rem = input("Want a rematch? yes or no?\n")
        if rem == "yes":
            play("RPS")
        else:
            print("See you next time!")

if __name__ == '__main__':
    print("Hello and welcome to The Gamer!")
    game = chooseGame()
    gm = Game()
    play(game)

