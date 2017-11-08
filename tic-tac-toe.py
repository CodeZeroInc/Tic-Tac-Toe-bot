#=========================================
#               TIC-TAC-TOE
#=========================================

from random import choice

#=========================================
# Check if a win has occured
#=========================================
def win(x):
    if x[0] == x[1] == x[2]:
        return True
    elif x[3] == x[4] == x[5]:
        return True
    elif x[6] == x[7] == x[8]:
        return True
    elif x[0] == x[3] == x[6]:
        return True
    elif x[1] == x[4] == x[7]:
        return True
    elif x[2] == x[5] == x[8]:
        return True
    elif x[1] == x[5] == x[8]:
        return True
    elif x[3] == x[5] == x[7]:
        return True
    return False

#=========================================
#check if next move can be win for "X"
#=========================================
def isNextMoveWin():
    global x
    global emptySlots

    for e in emptySlots:
        if win(play(x, e)):
            return e                        # returns the index to play "O"

        return 0                            # next move is not win

#=========================================
# Bot plays to win an edge
#=========================================





#=========================================
# print the table on the screen
#=========================================
def printTable(x):
    print("\t",x[0]," ",x[1]," ",x[2],"\n")
    print("\t",x[3]," ",x[4]," ",x[5],"\n")
    print("\t",x[6]," ",x[7]," ",x[8],"\n")

#=========================================
# place the 'X' at the given position
#=========================================
def play(x, pos, player="X"):
    x = x[:pos-1] + (player,) + x[pos:]
    return x

#=========================================
# place the "O" using FOL to ensure a draw
#=========================================
def botPlay(tmp):

    global x
    global Ohistory
    global emptySlots
    global count

    rand = 0
    Ohistory = []

#-------------------1st Move-------------------
    if count == 0:
        if tmp==1 or tmp==3 or tmp==7 or tmp==9:        # X plays corners
            x = play(x, 5, "O")
            Ohistory.append(5)
            emptySlots.remove(5)
            printTable(x)
            return x

        elif tmp==2 or tmp==4 or tmp==6 or tmp==8:      # X plays edges
            if tmp == 2:
                rand = choice([5,8,1,3])
                x = play(x, rand, "O")
                Ohistory.append(rand)
                emptySlots.remove(rand)
                printTable(x)
                return x

            elif tmp == 4:
                rand = choice([1,5,6,7])
                x = play(x, rand, "O")
                Ohistory.append(rand)
                emptySlots.remove(rand)
                printTable(x)
                return x

            elif tmp == 6:
                rand = choice([3,4,5,9])
                x = play(x, rand, "O")
                Ohistory.append(rand)
                emptySlots.remove(rand)
                printTable(x)
                return x

            elif tmp == 8:
                rand = choice([5,2,1,3])
                x = play(x, rand, "O")
                Ohistory.append(rand)
                emptySlots.remove(rand)
                printTable(x)
                return x
        else:                                           # X plays centre
            rand = choice([1,3,5,7])
            x = play(x, rand, "O")
            Ohistory.append(rand)
            emptySlots.remove(rand)
            printTable(x)
            return x

#-------------2nd Move-----------------------
    playPos = isNextMoveWin()

    if playPos:
        x = play(x, playPos, "O")
        Ohistory.append(playPos)
        emptySlots.remove(playPos)
        printTable(x)
        return x

##    else:
##        playtoWinEdge()

    


#========================================
# main function
#========================================

(a,b,c,d,e,f,g,h,i) = (1,2,3,4,5,6,7,8,9)
x = (a,b,c,d,e,f,g,h,i)

count = 0

Xhistory = []
Ohistory = []
emptySlots = [1,2,3,4,5,6,7,8,9]


printTable(x)

print("\nYou play 'X'")

while not (win(x) or count == 4):
    tmp = int(input("Enter position of 'X' to play :  "))

    x = play(x, tmp)
    Xhistory.append(tmp)
    emptySlots.remove(tmp)

    x = botPlay(tmp)
    count += 1
    break
