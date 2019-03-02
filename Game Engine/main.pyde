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
        while(1): #Termination Condition
            self.action()
            #Change to next player
            if self.playerTurn == self.playerOrder[-1]:
                self.playerTurn = self.playerOrder[0]
            else:
                playerIndex = self.playerOrder.index(self.playerTurn)
                self.playerTurn = self.playerOrder[playerIndex+1]
        
    def action(self):
        #TODO: For student to implement based on game
        
        
        
                                        
    def setupBoard(self):
        #TODO: For student to implement based on game
        temp = []
        for _ in range(self.boardSize):
            temp.append(Tile())
        return temp
        
    def setPlayerOrder(self, numPlayers):
        #TODO: For student to implement based on game
        temp = []
        for _ in range(numPlayers):
            temp.append(Player())
        return temp
        
#Used by the student to store information between the states of each player
class Player:
    
    def __init__(self):
        pass
        
class Tile:
    
    def __init__(self):
        pass
        
class Piece:
    
    def __init__(self):
        pass

app = Board(players, boardSize)
app.mainLoop()
