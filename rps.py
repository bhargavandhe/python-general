import random

print("'R' - ROCK\n'P' - PAPER\n'S' - SCISSOR\n'quit' - TO EXIT")
print("--------------------------------------------")
inp = input("Enter your Choice : ")
ls = ['R', 'P', 'S']
h_scr = c_scr = 0
while inp.lower() != "quit":
    if inp not in ls:
        print("INVALID CHOICE! TRY AGAIN")
        pass
    else:
        comp = ls[random.randint(0, 2)]
        if inp == 'R':
            if comp == 'R':
                print("STONE, TIE!")
                pass
            elif comp == 'P':
                print("PAPER, YOU LOSE!")
                c_scr += 1
                pass
            else:
                print("SCISSORS, YOU WIN!")
                h_scr += 1

                pass
        elif inp == 'P':
            if comp == 'P':
                print("PAPER, TIE!")
                pass
            elif comp == 'R':
                print("STONE, YOU WIN!")
                h_scr += 1
                pass
            else:
                print("SCISSORS, YOU LOSE!")
                c_scr += 1
        else:
            if comp == 'S':
                print("SCISSORS, TIE!")
                pass
            elif comp == 'P':
                print("PAPER, YOU WIN!")
                h_scr += 1
                pass
            else:
                print("STONE, YOU LOSE!")
                c_scr += 1
                pass
    inp = input("Enter your Choice : ")
print("+-----------------------------+")
print("|HUMAN                COMPUTER|")
print("| ", h_scr, "                    ", c_scr, "  |")
print("+-----------------------------+")
if h_scr > c_scr:
    print("YOU WON!")
else:
    print("YOU LOST, BETTER LUCK NEXT TIME!")
