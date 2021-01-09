from random import randint, choice

class AIProject:
    MaxStillHn = 30

    def __init__(self, nQueens):
        self.nQueens = nQueens
        self.initBoard()

    def initBoard(self):
        self.board = [randint(0,self.nQueens-1) for i in range(self.nQueens)]
        self.noOffStillHn = 0
        self.lastHn = self.noOffAttacks(self.board)

    def printBoard(self, board):
        print(self.board)
        for i in range(len(board)):
            for j in range(len(board)):
                if (len(board)-i) - 1 - board[j] == 0: print("Q", end=" ")
                else: print(".", end=" ")
            print()

    def noOffAttacks(self, board):
        totAttack = 0
        for i in range(len(board)):
            queen_row = board[i]
            for j in range(len(board)):
                if board[j] == queen_row and i != j: totAttack+=1
                if board[j] == (j-i)+queen_row and i != j: totAttack+=1
                if board[j] == -(j-i)+queen_row and i != j: totAttack+=1
        return totAttack//2

    def findHn(self, move):
        if move[1] == self.board[move[0]]:
            return self.lastHn
        moveHn = self.lastHn
        newRow = self.board[move[0]]
        for i in range(self.nQueens):
            if self.board[i] == newRow and i != move[0]: moveHn -= 1
            elif self.board[i] == (i-move[0])+newRow and i != move[0]: moveHn -= 1
            elif self.board[i] == -(i-move[0])+newRow and i != move[0]: moveHn -= 1
            if self.board[i] == move[1] and i != move[0]: moveHn += 1
            elif self.board[i] == (i-move[0])+move[1] and i != move[0]: moveHn += 1
            elif self.board[i] == -(i-move[0])+move[1] and i != move[0]: moveHn += 1
        return moveHn

    def makeNextMove(self):
        bestHn = self.lastHn
        bestMoves = [(0, self.board[0])]
        for i in range(self.nQueens):
            for j in range(self.nQueens):
                if j != self.board[i]:
                    newHn = self.findHn((i, j))
                    if newHn < bestHn:
                        bestHn = newHn
                        bestMoves = [(i, j)]
                    elif newHn == bestHn:
                        bestMoves.append((i, j))
        if bestHn == self.lastHn:
            self.noOffStillHn += 1
        else:
            self.noOffStillHn = 0
        newMove = choice(bestMoves)
        self.board[newMove[0]] = newMove[1]
        self.lastHn = bestHn

    def solve(self):
        while self.lastHn > 0:
            if self.noOffStillHn >= AIProject.MaxStillHn:
                print("Failed to find solution. Trying new board...")
                self.initBoard()
            self.makeNextMove()

if __name__ == '__main__':
    nQueen = int(input("Enter the Number of Queens : "))
    aiProject = AIProject(nQueen)
    print("Init Board")
    aiProject.printBoard(aiProject.board)
    aiProject.solve()
    print("Solution Board")
    aiProject.printBoard(aiProject.board)