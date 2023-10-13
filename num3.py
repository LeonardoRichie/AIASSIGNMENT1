#tictactoe class
class TicTacToe:
    
    
    def __init__(self):#start state
        self.state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
    def display_board(self):#display board
        for row in self.state:
            print(" ".join(["X" if cell == 1 else "O" if cell == -1 else "-" for cell in row]))
            
    def make_move(self, row, col, val):#moving
        made_move = False
        if (isinstance(row, int)) and (row >= 0) and (row <= 2):
            if (isinstance(col, int)) and (col >= 0) and (col <= 2):
                if self.state[row][col] == 0:
                    if (val == -1) or (val == 1):
                        self.state[row][col] = val
                        made_move = True
        return made_move

    def try_move(self, state, row, col, val):
        if (isinstance(row, int)) and (row >= 0) and (row <= 2):
            if (isinstance(col, int)) and (col >= 0) and (col <= 2):
                if state[row][col] == 0:
                    if (val == -1) or (val == 1):
                        state[row][col] = val
        return state

    def check_winner(self):
        for row in self.state:#check rows
            if row[0] == row[1] == row[2] and row[0] != 0:
                return row[0]

        for col in range(3):#Check columns
            if self.state[0][col] == self.state[1][col] == self.state[2][col] and self.state[0][col] != 0:
                return self.state[0][col]

        if self.state[0][0] == self.state[1][1] == self.state[2][2] and self.state[0][0] != 0:
            return self.state[0][0]#Check diagonals
        if self.state[0][2] == self.state[1][1] == self.state[2][0] and self.state[0][2] != 0:
            return self.state[0][2]

        #drawcondition
        if all(cell != 0 for row in self.state for cell in row):
            return 0

        #progressing process
        return None

    def minimax(self, state, depth, is_maximizing):#minimax algorithm
        winner = self.check_winner()

        if winner is not None:
            return winner * (10 - depth)

        if is_maximizing:
            max_eval = float('-inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j] == 0:
                        state[i][j] = 1
                        eval = self.minimax(state, depth + 1, False)
                        state[i][j] = 0
                        max_eval = max(max_eval, eval)
            return max_eval

        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j] == 0:
                        state[i][j] = -1
                        eval = self.minimax(state, depth + 1, True)
                        state[i][j] = 0
                        min_eval = min(min_eval, eval)
            return min_eval

    def bot_move(self):
        best_move = None
        best_eval = float('-inf')

        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    self.state[i][j] = 1
                    eval = self.minimax(self.state, 0, False)
                    self.state[i][j] = 0
                    if eval > best_eval:
                        best_eval = eval
                        best_move = (i, j)

        if best_move:
            self.make_move(best_move[0], best_move[1], 1)


game = TicTacToe()#start the game

start = "yes"#looping
while True:
    if start=="yes":#when the game starts
        print( "- - -")
        print( "- - -")
        print( "- - -")
    start = "no"
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    if not game.make_move(row, col, -1):
        print("Invalid move, try again.")
        continue

    game.display_board()

    winner = game.check_winner()#checking win or lose
    if winner == -1:
        print("Player wins!")
        break
    elif winner == 0:
        print("It's a draw!")
        break

    #bots turn
    print("Bot's move:")
    game.bot_move()
    game.display_board()

    #check bot win or lose
    winner = game.check_winner()
    if winner == 1:
        print("Bot wins!")
        break
    elif winner == 0:
        print("It's a draw!")
        break
