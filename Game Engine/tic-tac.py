class Board:
    
    def __init__(self, numPlayers):
        """
        playerOrder is the list of players in order
        playerTurn is the current player whos turn it is
        mainLoop is the main action turn loop
        board is the game board
        """
                
        self.shapes = ['x', 'o']
        self.playerOrder = []
        self.setPlayerOrder(numPlayers)
        self.playerTurn = self.playerOrder[0]
        self.board = self.initBoard() 
        self.mainLoop()

    def initBoard(self):
        # makes the game board at start of game
        board = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append('.')
            board.append(row)
        print(board)

    def displayBoard(self):
        # prints the board
        for row in self.board:
            print(row)
        
    def mainLoop(self):
        # main action turn loop
        while True:
            self.displayBoard() 
            # do the action
            self.playerTurn.action()
            if self.playerTurn == self.playerOrder[-1]:
                self.playerTurn = self.playerOrder[0]
            else:
                self.playerTurn = self.playerOrder[self.playerOrder.index(self.playerTurn)+1]
            self.displayBoard()
            # check end game condition
            if isGameOver():
                break

    def isGameOver(self):
        # check if the game is over
        # check if theres 3 of either shape in a diagonal, 
        # a column, or a row
        # check columns first
        for shape in self.shapes:
            # check rows
            for row in self.board:
                count = 0
                for place in row:
                    if place == shape:
                        count += 1
                if count == 3:
                    return True
            # check columns 
            for i in range(3):
                count = 0
                for row in self.board:
                    if row[i] == shape:
                        count += 1
                if count == 3:
                    return True
            # check diag right up 
            count = 0
            for i in range(3):
                for j in range(3):
                    if i == j and self.board[i][j] == shape:
                        count += 1
            if count == 3:
                return True
            # check diag right down
            place = self.board
            if place[0][2] == shape and place[1][1] == shape and place[2][0] == shape:
                return True


        
    def setPlayerOrder(self, numPlayers):
        #TODO: For student to implement based on game
        for i in range(numPlayers):
            self.playerOrder.append(Player(self.shapes[i]))

    def action(self):
        # place piece down on given spot 
        # of get postion and shape from 
        # player
        position = self.playerTurn.getPosition()
        self.board[position[0]][position[1]] = self.playerTurn.getShape()
        
class Player:
    
    def __init__(self, shape):
        
        self.position = None
        self.shape = shape
    
    def getPosition(self):
        # choose square, check square
        # validate it is within bounds
        # return chosen position
        while True:
            position = input('Input position, format: row# column #')
            position = position.split()
            for i in range(len(position)):
                position[i] = int(position[i])
            for num in position:
                if position < 0 or position > 5:
                    print('Position out of bounds')
                elif self.board[position[0]][position[1]] == '.':
                    print('Board spot full')
                else:
                    break
        self.position = position
        return position
    
    def getShape(self):
        # returns colour
        return self.shape
        
            
class Piece:

    def __init__(self, type):
        self.type = type


def main():

    board = Board(2)
   
main()
