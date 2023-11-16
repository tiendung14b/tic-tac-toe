import random
import os

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# AI class
class AI:
    def __init__(self, **args):
        self.movePos = args["pos"]
        self.aiValue = args["aiValue"]
        self.pos = args["pos"]
        self.step = args["step"]
    
    def get_random_move(self, board):
        moves = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] == ' '):
                    moves.append(Pos(i, j))
        return random.choice(moves);
    
    def get_best_move(self, board):
        bestScore = -99999
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] == ' '):
                    board[i][j] = self.aiValue
                    score = self.minimax(board = board, step = self.step, isMaxNode = False)
                    board[i][j] = ' '
                    if score > bestScore:
                        bestScore = score
                        self.movePos.x = i
                        self.movePos.y = j
                         
        return self.movePos

    #alpha beta pruning
    def minimax(self, board, step, isMaxNode, alpha = -99999, beta = 99999):
        if (step == 0):
            return 0
        elif (game.check_winner(3) == 'x'):
            return -1*(self.step - step)
        elif (game.check_winner(3) == 'o'):
            return 1*(self.step - step)
        if (isMaxNode):
            bestScore = -99999
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if (board[i][j] == ' '):
                        board[i][j] = self.aiValue
                        score = self.minimax(board = board, step = step - 1, isMaxNode = False)
                        board[i][j] = ' '
                        bestScore = max(score + 1, bestScore)
                        alpha = max(alpha, bestScore)
                        if (beta <= alpha):
                            break
            return bestScore
        else:
            bestScore = 99999
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if (board[i][j] == ' '):
                        board[i][j] = 'x'
                        score = self.minimax(board = board, step = step - 1, isMaxNode = True)
                        board[i][j] = ' '
                        bestScore = min(score, bestScore)
                        beta = min(beta, bestScore)
                        if (beta <= alpha):
                            break
            return bestScore
# Game class
class Game:
    def __init__(self, **args):
        self.board = args["board"]
        self.compValue = args["compValue"]
        self.turn = args["turn"]
        self.end = False
        self.ai = AI(pos = Pos(-1, -1), aiValue = args['aiValue'], step = 3)
    
    # uncomplete
    def launch(self):
        winner = None
        self.show_board()
        while (not self.end and winner == None):
            if (self.turn == 'comp'):
                x = (int)(input("x: "))
                y = (int)(input("y: "))
                # if (not self.is_valid_move({x, y})):
                #     continue
                board[x][y] = self.compValue
                self.turn = 'ai'
            elif (self.turn == 'ai'):
                self.ai.pos = self.ai.get_best_move(board=board)
                # if (not self.is_valid_move({x, y})):
                #     continue
                board[self.ai.pos.x][self.ai.pos.y] = self.ai.aiValue
                os.system("cls")
                self.turn = 'comp'
            winner = self.check_winner(4)
            self.end = self.is_board_full()
            self.show_board()
        print("The winner is ", winner)
    # check valid position
    def is_valid_move(self, pos):
        if (not isinstance(pos, Pos)):
            return False
        length = len(self.board)
        if (pos.x >= length or pos.y >= length):
            return False
        return True
    
    # function show the board 
    def show_board(self):
        line = '  '
        for i in range(len(self.board)):
            line = line + i.__str__().zfill(2) + '  '
            
        print(line)
        line = ""
        for i in range(len(self.board)):
            line = "| "
            for j in range (len(self.board[i])):
                line = line + self.board[i][j] + ' | '
            print(line, i)
            line = ""
            for j in range (len(self.board[i])):
                line = line + '----'
            print(line)
            
    # function
    def is_board_full(self):
        return not any(' ' in row for row in board)
    
    # function to check who is winner
    def check_winner(self, k):
        n = len(self.board)
        def check_line(line):
            # Check if the first cell is non-empty and equal to all others
            first_cell = line[0]
            if first_cell == ' ':
                return None
            elif all(cell == first_cell for cell in line):
                return first_cell
            else:
                return None

        # Check rows
        for row in self.board:
            winner = check_line(row[:k])
            if winner:
                return winner
            
            for i in range(1, n-k+1):
                winner = check_line(row[i:i+k])
                if winner:
                    return winner

        # Check columns
        for col_index in range(n):
            col = [self.board[row_index][col_index] for row_index in range(n)]
            winner = check_line(col[:k])
            if winner:
                return winner
            
            for i in range(1, n-k+1):
                winner = check_line(col[i:i+k])
                if winner:
                    return winner

        # Check diagonals
        for start_row in range(n-k+1):
            for start_col in range(n-k+1):
                diagonal = [self.board[start_row+i][start_col+i] for i in range(k)]
                winner = check_line(diagonal)
                if winner:
                    return winner

        for start_row in range(n-k+1):
            for end_col in range(k-1, n):
                diagonal = [self.board[start_row+i][end_col-i] for i in range(k)]
                winner = check_line(diagonal)
                if winner:
                    return winner

        # No winner found
        return None

board = []
size = 6
for i in range(size):
    board.append([' ']*size)

game = Game(board = board, aiValue = 'o', compValue = 'x', turn = 'comp')
game.launch()
