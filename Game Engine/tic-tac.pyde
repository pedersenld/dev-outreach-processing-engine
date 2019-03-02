class Board:
    
    def __init__(self, numPlayers):
        
        self.playerOrder = []
        self.setPlayerOrder(numPlayers)
        self.playerTurn = playerOrder[0]
        self.mainLoop()
        
    def mainLoop(self):
        while(1):
            self.playerTurn.action()
            if self.playerTurn == self.playerOrder[-1]:
                self.playerTurn = self.playerOrder[0]
            else:
                self.playerTurn = self.playerOrder[self.playerOrder.index(self.playerTurn)+1]
        
    def setPlayerOrder(self, numPlayers):
        #TODO: For student to implement based on game
        for _ in range(numPlayers):
            self.playerOrder.append(Player())
        

class Player:
    
    def __init__(self):
        
        self.position
    
    def action(self):
        # choose square, check square
        # validate it is within bounds

        

class Piece:

    def __init__(self, type):
        self.type = type



def main():
    
    # make player 1
    # make player 2
    # make game board
    # game loop
    # 
