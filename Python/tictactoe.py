import random
def tictactoe():
    spcd={
        "1":"1",
        "2":"2",
        "3":"3",
        "4":"4",
        "5":"5",
        "6":"6",
        "7":"7",
        "8":"8",
        "9":"9"
    }
    #print(" |",spcd["1"],"|",spcd["2"],"|",spcd["3"],"\n","|",spcd["4"],"|",spcd["5"],"|",spcd["6"],"\n","|",spcd["7"],"|",spcd["8"],"|",spcd["9"],)

    b=True
    avaiSpc=[1,2,3,4,5,6,7,8,9]
    ai=False
    print(" |",spcd["1"],"|",spcd["2"],"|",spcd["3"],"\n","|",spcd["4"],"|",spcd["5"],"|",spcd["6"],"\n","|",spcd["7"],"|",spcd["8"],"|",spcd["9"],"\n\n")
    aiChoice=int(input("Choose Your Opponent \n 1.Ai \n 2.Player 2 \n 1 for Ai or 2 for Player 2 \n"))
    while (b==True):
        
        a=True
        def check():
            if ( spcd["1"]==spcd["2"] and spcd["1"]==spcd["3"]):
                b=False
                print(" |",spcd["1"],"|",spcd["2"],"|",spcd["3"],"\n","|",spcd["4"],"|",spcd["5"],"|",spcd["6"],"\n","|",spcd["7"],"|",spcd["8"],"|",spcd["9"],)
                print("We have a winner")
                return
            #--- mid  
            elif(spcd["4"]==spcd["5"] and spcd["4"]==spcd["6"]):
                b=False
                print(" |",spcd["1"],"|",spcd["2"],"|",spcd["3"],"\n","|",spcd["4"],"|",spcd["5"],"|",spcd["6"],"\n","|",spcd["7"],"|",spcd["8"],"|",spcd["9"],)
                print("We have a winner")
                return
            #--- down
            elif(spcd["7"]==spcd["8"] and spcd["7"]==spcd["9"]):
                b=False
                print(" |",spcd["1"],"|",spcd["2"],"|",spcd["3"],"\n","|",spcd["4"],"|",spcd["5"],"|",spcd["6"],"\n","|",spcd["7"],"|",spcd["8"],"|",spcd["9"],)
                print("We have a winner")
                return
            #\
            elif(spcd["1"]==spcd["5"] and spcd["1"]==spcd["9"]):
                b=False
                print(" |",spcd["1"],"|",spcd["2"],"|",spcd["3"],"\n","|",spcd["4"],"|",spcd["5"],"|",spcd["6"],"\n","|",spcd["7"],"|",spcd["8"],"|",spcd["9"],)
                print("We have a winner")
                return
            #/
            elif(spcd["3"]==spcd["5"] and spcd["3"]==spcd["7"]):
                b=False
                print(" |",spcd["1"],"|",spcd["2"],"|",spcd["3"],"\n","|",spcd["4"],"|",spcd["5"],"|",spcd["6"],"\n","|",spcd["7"],"|",spcd["8"],"|",spcd["9"],)
                print("We have a winner")
                return
            # |
            elif(spcd["2"]==spcd["5"] and spcd["2"]==spcd["8"]):
                b=False
                print(" |",spcd["1"],"|",spcd["2"],"|",spcd["3"],"\n","|",spcd["4"],"|",spcd["5"],"|",spcd["6"],"\n","|",spcd["7"],"|",spcd["8"],"|",spcd["9"],)
                print("We have a winner")
                return
            #|
            elif(spcd["1"]==spcd["4"] and spcd["1"]==spcd["7"]):
                b=False
                print(" |",spcd["1"],"|",spcd["2"],"|",spcd["3"],"\n","|",spcd["4"],"|",spcd["5"],"|",spcd["6"],"\n","|",spcd["7"],"|",spcd["8"],"|",spcd["9"],)
                print("We have a winner")
                return
            #  |
            elif(spcd["3"]==spcd["6"] and spcd["3"]==spcd["9"]):
                b=False
                print(" |",spcd["1"],"|",spcd["2"],"|",spcd["3"],"\n","|",spcd["4"],"|",spcd["5"],"|",spcd["6"],"\n","|",spcd["7"],"|",spcd["8"],"|",spcd["9"],)
                print("We have a winner")
                return
        while(a==True):
            p1spc=int(input("P1. Where do you want to play \n"))
            if p1spc in avaiSpc :
                spcd[str(p1spc)]="X"
                #print(" |",spcd["1"],"|",spcd["2"],"|",spcd["3"],"\n","|",spcd["4"],"|",spcd["5"],"|",spcd["6"],"\n","|",spcd["7"],"|",spcd["8"],"|",spcd["9"],)
                check()
                a=False
                avaiSpc.pop(avaiSpc.index(p1spc))
            else:
                print("That space has been taken")
        
        if (aiChoice==1):
            while(a==False):
                    aispc=random.choice(avaiSpc)
                    if aispc in avaiSpc:
                        spcd[str(aispc)]="O"
                        print(" |",spcd["1"],"|",spcd["2"],"|",spcd["3"],"\n","|",spcd["4"],"|",spcd["5"],"|",spcd["6"],"\n","|",spcd["7"],"|",spcd["8"],"|",spcd["9"],)
                        check()
                        a=True
                        avaiSpc.pop(avaiSpc.index(aispc))
                    else:
                        a=False
        else:
            
            while(a==False):
                    p2spc=int(input("P2 Where do you want to play \n"))
                    if p2spc in avaiSpc:
                        spcd[str(p2spc)]="O"
                        print(" |",spcd["1"],"|",spcd["2"],"|",spcd["3"],"\n","|",spcd["4"],"|",spcd["5"],"|",spcd["6"],"\n","|",spcd["7"],"|",spcd["8"],"|",spcd["9"],)
                        check()
                        a=True
                        avaiSpc.pop(avaiSpc.index(p2spc))
                    else:
                        print("That space has been taken")
        #--- up
        
        
 #p2spc=int(input("Where do you want to play \n"))
    
#print("",spcd["1"],"|",spcd["2"],"|",spcd["3"],"\n","|",spcd["4"],"|",spcd["5"],"|",spcd["6"],"\n","|",spcd["7"],"|",spcd["8"],"|",spcd["9"],)
tictactoe()
    