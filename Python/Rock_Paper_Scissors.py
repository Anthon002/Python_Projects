import random
'''
rock=1
paper=2
scissors=3
2>1,3>2,1>3
'''
user=input("What's your username?")
user_points=0
pc_points=0
user_choice_int={
        "rock":1,
        "paper":2,
        "scissors":3
    }


print('First to get a max point of 3')
while user_points < 3 or pc_points < 3:
    a=random.randint(1,3)
    user_choice=input("Rock...Paper...Scissors...")
    pc_choice=a
    
    
    #if user wins or loses
    if (user_choice_int.get(user_choice.lower())==1 and pc_choice == 1):
        print("That's a draw \n Pc = "+ str(pc_points) + user+" = " + str(user_points))
        
    elif(user_choice_int.get(user_choice.lower())==1 and pc_choice == 2):
        pc_points+=1
        print("Pc Picks Paper and Paper Beats Rock \n"+str(pc_points) + " point for pc " +str(user_points) + " point for "+user)
       
    elif(user_choice_int.get(user_choice.lower())==1 and pc_choice == 3):
        user_points+=1
        print(user+" Picks Rock and Rock Beats Scissors\n "+str(user_points) + " point for "+user +" "+str(pc_points) + " point for pc ")
        
    elif(user_choice_int.get(user_choice.lower())==2 and pc_choice == 1):
        user_points+=1
        print(user+" Picks Paper and Paper Beats Rock \n"+str(user_points) + " point for "+user +" "+str(pc_points) + " point for pc ")
        
    elif(user_choice_int.get(user_choice.lower())==2 and pc_choice == 2):

        print("Both Pc and "+user+"Picked Paper and  That's a draw \n Pc = "+ str(pc_points) + user+" = " + str(user_points))
    elif(user_choice_int.get(user_choice.lower())==2 and pc_choice == 3):
        pc_points+=1
        print("Pc Picks Scissors and Scissors Beats Paper \n "+str(pc_points) + " point for pc " +str(user_points) + " point for "+user)
       
    elif(user_choice_int.get(user_choice.lower())==3 and pc_choice == 1):
        pc_points+=1
        print("Pc Picks Rock and Rock Beats Scissors\n "+str(pc_points) + " point for pc " +str(user_points) + " point for "+user)
       
    elif(user_choice_int.get(user_choice.lower())==3 and pc_choice == 2):
        user_points+=1
        print(user+" Picks Scissors and Scissors Beats Paper \n "+str(user_points) + " point for "+user +" "+str(pc_points) + " point for pc ")
        
    elif(user_choice_int.get(user_choice.lower())==3 and pc_choice == 3):

        print("Both Pc and "+user+" Picks Scissors and That's a draw \n Pc = "+ str(pc_points) + user+" = " + str(user_points))
    else:
        print("Put in a valid input")

if(user_points> pc_points):
    print("And the winner is " + user +". \n Scores: Pc = "+str(pc_points)+ user +" = "+str(user_points))
else:
    print("And the winner is Pc" +" \n Scores: Pc = "+str(pc_points)+ user +" = "+str(user_points))
    


