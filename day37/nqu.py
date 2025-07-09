# n = 4
# board = [["."]*n for _ in range(n)]

# def display():
#     for i in board:
#         print(i)
#     print("\n")

# def backtrack(row , colSet , posDiagonal , negDiagonal , board):
#     if row == n:
#         display()
#         return
    
#     for col in range(0,n):
#         neg = row - col
#         pos = row + col
#         if col not in colSet and pos not in posDiagonal and neg not in negDiagonal :
#             colSet.add(col)
#             posDiagonal.add(pos)
#             negDiagonal.add(neg)
#             board[row][col] = "Q"
#             backtrack(row + 1 ,colSet , posDiagonal , negDiagonal , board)
#             colSet.remove(col)
#             posDiagonal.remove(pos)
#             negDiagonal.remove(neg)
#             board[row][col] = "."
# backtrack(0, set() , set() , set() , board)






def solve_n_queens(n):
    board = [ ["."] * n for _ in range(n) ]

    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == "Q": return False
        for i,j in zip(range(row-1,-1,-1), range(col-1,-1,-1)):
            if board[i][j] == "Q": return False
        for i,j in zip(range(row-1,-1,-1), range(col+1,n)):
            if board[i][j] == "Q": return False
        return True

    def backtrack(row):
        if row == n:
            for line in board: print("".join(line))
            print("\n")
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"
                backtrack(row+1)
                board[row][col] = "."

    backtrack(0)
