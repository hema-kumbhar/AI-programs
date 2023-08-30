# Function to check if a queen can be placed on the board
def isSafe(board, row, col, n):
    # Check the row
    for i in range(col):
        if board[row][i]:
            return False

    # Check the upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check the lower diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # If it's safe, return True
    return True

# Function to solve the N-Queens problem using Branch and Bound
def solveNQueens(n):
    # Initialize the board
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Initialize the variables
    solutions = []
    q = []
    q.append((board, 0))

    # While the queue is not empty
    while q:
        # Get the current board and column
        curr_board, col = q.pop()

        # If all queens are placed, add the solution to the list
        if col == n:
            solutions.append(curr_board)
            continue

        # Iterate over all possible rows to place a queen
        for row in range(n):
            # If it's safe to place a queen, add the board to the queue
            if isSafe(curr_board, row, col, n):
                new_board = [r[:] for r in curr_board]
                new_board[row][col] = 1
                q.append((new_board, col+1))

    # Print the solutions
    for solution in solutions:
        for row in solution:
            print(row)
        print()


#Number of queens
print ("Enter the number of queens")
N = int(input())
solveNQueens(N)
