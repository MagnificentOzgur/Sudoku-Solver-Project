import heapq

class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.size = 9
        self.subgrid_size = 3

    def is_valid(self, row, col, num):
        """Check if placing 'num' at board[row][col] is valid."""
        # Check row
        for c in range(self.size):
            if self.board[row][c] == num:
                return False

        # Check column
        for r in range(self.size):
            if self.board[r][col] == num:
                return False

        # Check subgrid
        start_row = (row // self.subgrid_size) * self.subgrid_size
        start_col = (col // self.subgrid_size) * self.subgrid_size
        for r in range(start_row, start_row + self.subgrid_size):
            for c in range(start_col, start_col + self.subgrid_size):
                if self.board[r][c] == num:
                    return False

        return True

    def find_empty_cell(self):
        """Find the first empty cell on the board."""
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return r, c
        return None

    def heuristic(self):
        """Calculate the heuristic: count the number of empty cells."""
        return sum(row.count(0) for row in self.board)

    def a_star_search(self):
        """Solve Sudoku using A* algorithm."""
        # Priority queue for A* (f = g + h)
        pq = []
        heapq.heappush(pq, (self.heuristic(), self.board))

        while pq:
            _, current_board = heapq.heappop(pq)
            self.board = current_board

            # If no empty cells, the board is solved
            if self.heuristic() == 0:
                return True

            # Find the next empty cell
            empty_cell = self.find_empty_cell()
            if not empty_cell:
                continue

            row, col = empty_cell

            # Try all possible numbers (1-9)
            for num in range(1, 10):
                if self.is_valid(row, col, num):
                    # Place the number and calculate heuristic
                    new_board = [row[:] for row in self.board]
                    new_board[row][col] = num
                    heapq.heappush(pq, (self.heuristic(), new_board))

        return False

    def print_board(self):
        """Print the Sudoku board."""
        for row in self.board:
            print(" ".join(str(num) if num != 0 else '.' for num in row))

# Example Sudoku puzzle (0 represents empty cells)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solver = SudokuSolver(puzzle)
print("Sudoku Puzzle:")
solver.print_board()

if solver.a_star_search():
    print("\nSolved Sudoku:")
    solver.print_board()
else:
    print("\nNo solution exists.")
