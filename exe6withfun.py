player1=(str(input("Enter your choice:")))
player2=(str(input("Enter your choice:")))

def rock(input1,input2):
   
    if player1== "rock" and player2 == "scisssors":
        print ("p1 won the game")
    elif player1 == "paper" and player2 == "rock":
        print ("p1 won the game")
    elif player1 == "scissors" and player2 == "paper":
        print("p1 won the game")
    elif player2== "rock" and player1 == "scisssors":
        print ("p1 won the game")
    elif player2 == "paper" and player1 == "rock":
        print ("p1 won the game")
    elif player2 == "scissors" and player1 == "paper":
        print("p1 won the game")
    elif player1== "rock" and player2 == "rock":
        print ("the match is drawn between 2")
    elif player1 == "paper" and player2 == "paper":
        print ("the match is drawn between 2")
    elif player1 == "scissors" and player2 == "scissors":
        print("the match is drawn between 2")
rock(player1,player2)
