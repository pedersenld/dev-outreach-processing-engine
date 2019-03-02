#Player buys every property they land on, everything costs the same, no unique squares, if players cant afford to pay rent they just go into negative money
#No money for going around go(implemented but values need to change on rent/purchase as otherwise game does not end because they gain too much money)


import random
import time

players = 4
boardSize = 40
canvasSize = 440

class Board:
    
    
    def __init__(self, numPlayers, boardSize):
        
        self.boardSize = boardSize
        self.board = self.setupBoard()
        self.playerOrder = self.setPlayerOrder(numPlayers)
        self.playerTurn = self.playerOrder[0]
        
        
    def mainLoop(self):
        #Terminate the game if only 1 player is left
        while(len(self.playerOrder) > 1):
            self.action()
            #Change to next player and remove the current player if they are out of money
            if self.playerTurn == self.playerOrder[-1]:
                if self.playerTurn.money <= 0:
                    self.playerOrder.remove(self.playerTurn)
                self.playerTurn = self.playerOrder[0]
            else:
                playerIndex = self.playerOrder.index(self.playerTurn)
                self.playerTurn = self.playerOrder[playerIndex+1]
                if self.playerOrder[playerIndex].money <= 0:
                    del self.playerOrder[playerIndex]
        print self.playerOrder[0].name, "is the winner"
        
    def action(self):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        reroll = dice1 == dice2 if True else False
        self.playerTurn.position += dice1 + dice2
        #determine if player passes go
        if self.playerTurn.position >= self.boardSize:
            self.playerTurn.position %= self.boardSize
            self.playerTurn.money += 0
        #determine who owns the property and pay rent/buy property
        boardTile = self.board[self.playerTurn.position]
        if boardTile.owner == None:
            if self.playerTurn.money >= boardTile.cost:
                boardTile.owner = self.playerTurn
                self.playerTurn.money -= boardTile.cost
        else:
            self.playerTurn.money -= boardTile.rent
            boardTile.owner.money += boardTile.rent
        #if player rolled doubles then reroll
        if reroll:
            self.action()
        
        
        
        #Creates the board full of tiles                                
    def setupBoard(self):
        #TODO: For student to implement based on game
        temp = []
        names = [str(x) for x in range(self.boardSize)]
        prices = [x for x in range(self.boardSize)]
        for i in range(self.boardSize):
            temp.append(Tile(names[i],prices[i]))
        return temp
        
        #Creates a player object for each player
        #If order needs to be decided then should also be done inside of this function
    def setPlayerOrder(self, numPlayers):
        #TODO: For student to implement based on game
        temp = []
        for i in range(numPlayers):
            temp.append(Player(i, 0))
        return temp
        
#Player and Tile are used to store information about each tile/player
#This is beneficial as it makes it easy for the player to interact with the board as their position corresponds to a tile on the board


class Player:
    
    def __init__(self, name, position):
        
        self.name = name
        self.money = 1500
        self.position = position
        
class Tile:
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.cost = 300
        self.rent = 50
        self.owner = None
        
class Piece:
    
    def __init__(self):
        pass

app = Board(players, boardSize)
app.mainLoop()
    
    
    
def setup():
    global f
    size(canvasSize,5*canvasSize/4)
    background(0)
    f = createFont("Arial",16)
#drawing math should be cleaned up
#general idea is to divide the board into how many tiles are needed in each spot from squares and using this
#with canvas size to proportion the size of each square
def draw():
    global f
    textFont(f,16)
    squares = (boardSize-4)/4 + 2
    startX = canvasSize-canvasSize/squares
    startY = canvasSize-canvasSize/squares
    for i in range(boardSize/4+1):
        rect(startX, startY, canvasSize/squares, canvasSize/squares)
        fill(0)
        textAlign(CENTER)
        text(app.board[i].name, startX+canvasSize/(2*squares), startY+canvasSize/(2*squares))
        fill(255)
        startX -= canvasSize/squares
    for i in range(boardSize/4):
        rect(startX, startY, canvasSize/squares, canvasSize/squares)
        fill(0)
        textAlign(CENTER)
        text(app.board[i+boardSize/4].name, startX+canvasSize/(2*squares), startY+canvasSize/(2*squares))
        fill(255)
        startY += canvasSize/squares
    rect(canvasSize/squares, canvasSize/squares, canvasSize-2*canvasSize/squares, canvasSize-2*canvasSize/squares)
    #for player in app.playerOrder:
        #stroke
