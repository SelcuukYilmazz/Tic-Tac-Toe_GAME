def tableset():
    a = 0
    b = -1
    for i in range(y):
        print("")
        for z in range(y):
            a = a + 1
            b = b + 1

            print((" ".join(str(k) for k in x[b:a])).rjust(5), "", end="")
def moveset(Player,value,Opponent,Symbol,Desymbol):
    while 1:
        print("")
        if value >= 0 and value < y * y:
            if x[value] == Symbol:
                print(Player," have made this choice before.")
                break
            elif x[value] == Desymbol:
                print(Opponent, " select this cell before.")
                break
            else:
                x[value] = Symbol
                break
        else:
            print("Please enter a valid number.")
            break
def winset(Symbol,Player):
    a = 0
    b = -y
    for i in range(y):
        a = a+y
        b = b+y
        if x[b:a] == [Symbol]*y:
            print("")
            print("Winner : ",Symbol)
            input("Press enter to quit.")
            quit()
        elif x[0:y*y:y+1] == [Symbol]*y:
            if x[0] == [Symbol]:
                pass
            else:
                print("")
                print("Winner : ",Symbol)
                input("Press enter to quit.")
                quit()
        elif x[y - 1:(y * y) - 1:y - 1] == [Symbol] * y:
            if x[y - 1] == [Symbol]:
                pass
            else:
                print("")
                print("Winner : ",Symbol)
                input("Press enter to quit.")
                quit()
        for q in range(y):
            if x[q:y*y:y] == [Symbol]*y:
                print("")
                print("Winner : ",Symbol)
                input("Press enter to quit.")
                quit()
        else:
            pass
def drawset():
    if all(type(st) is str for st in x):
        print("")
        print("No winner")
        input("Press enter to quit.")
        quit()
while 1:
    y = int(input("What Size Game GoPy?"))
    x = list(range(y*y))
    a = 0
    b = -1
    if y < 3:
        print("Your value must be greater than 2")
        continue
    else:
        for i in range(y):
            print("")
            for z in range(y):
                a = a + 1
                b = b + 1
                print((" ".join(str(k) for k in x[b:a])).rjust(5), "", end="")
        while 1:
            print("")
            moveset("You",int(input("Player 1 turn--> ")),"The other player","X","O")
            tableset()
            winset("X","P1")
            drawset()
            print("")
            moveset("You",int(input("Player 2 turn--> ")),"The other player","O","X")
            tableset()
            winset("O","P2")
            drawset()
            continue