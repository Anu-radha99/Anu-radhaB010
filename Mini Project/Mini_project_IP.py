#-------------> Tic Tac Toe Game in Python <-----------------

#importing random module for computer mode
import random

#setting up the global variables

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

currentplayer = "X"
winner = None
gamerunning = True


#defining a function to print the board
def printboard(board):
    print(board[0]+"|"+ board[1]+"|"+ board[2])
    print("-----")
    print(board[3]+"|"+ board[4]+"|"+ board[5])
    print("-----")
    print(board[6]+"|"+ board[7]+"|"+ board[8])

    
#A function to take the input of the position where he wants to play
def playerinput(board):
    inp=int(input("Enter a Number 1-9: "))
    if inp<1 or inp>9:
        print("Invalid Spot")
    elif board[inp-1]!="-":
        print("Spot is occupied")
    else:
        board[inp-1]=currentplayer
        
#checking whether any player won horizontally
def checkhorizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="-":
        winner = board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner = board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner = board[6]
        return True

    
#checking whether any player won vertically
def checkvertical(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner = board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner = board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner = board[2]
        return True

    
#checking whether any player won diagonally
def checkdiagonal(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner = board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!="-":
        winner = board[2]
        return True


#checking the game result if its a win
def checkwin():
    global gamerunning
    if checkhorizontal(board) or checkvertical(board) or checkdiagonal(board):
        print("The winner is: ", winner)
        gamerunning = False
        return True

    
#checking the game result if its a tie
def checktie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("Game is Drawn")
        gamerunning=False

        
#switching the player after a move for computer mode
def switchplayer():
    global currentplayer
    if currentplayer=="X":
        currentplayer="O"
    else:
        currentplayer="X"

        
#switching the player after a move for two player mode
def switchplayer2():
    global currentplayer
    if currentplayer=="X":
        currentplayer="O"
    else:
        currentplayer="X"
    print(currentplayer,"Turn")

        
#creating a bot to play with the player
def computer(board):
    while currentplayer=="O":
        position=random.randint(0,8)
        if board[position]=="-":
            board[position]="O"
            switchplayer()

            
#function for the game to run in two player mode
def twoplayermode(board):
    while gamerunning:
        printboard(board)
        playerinput(board)
        checkwin()
        checktie(board)
        if gamerunning==False:
            break
        switchplayer2()

        
#function for The game to run in computer mode
def ComputerMode(board):
    while gamerunning:
        printboard(board)

# Player X's turn
        playerinput(board)
        checkwin()
        checktie(board)
        if gamerunning==False:
            break

# Computer O's turn
        switchplayer()
        computer(board)
        checkwin()
        checktie(board)
        if gamerunning==False:
            break

        
#printing the user interface and Menu
        
print("Welcome to Tic Tac Toe!")
print("Menu")
print("1. Play with Computer")
print("2. Two Player Mode")

#taking the coice of the user for the mode in which he/she wants to play

ch=int(input("Enter Choice(1-2): "))
if ch==1:
    ComputerMode(board)
elif ch==2:
    twoplayermode(board)
else:
    print("Invalid Choice")
