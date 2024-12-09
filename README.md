# Sudoku Solver Using A* Algorithm

This project is a Sudoku solver implemented in Python using the A\* search algorithm. It fills the empty cells in a Sudoku puzzle while following the game's rules.

## Problem Description

Sudoku is a 9x9 grid-based puzzle where the goal is to fill all cells with numbers from 1 to 9 such that:  
1. Each row contains numbers from 1 to 9 exactly once.  
2. Each column contains numbers from 1 to 9 exactly once.  
3. Each 3x3 subgrid contains numbers from 1 to 9 exactly once.  

### Input  
A 9x9 matrix representing the Sudoku puzzle. Empty cells are denoted by `0`.

### Output  
A solved 9x9 matrix where all empty cells are filled while following the Sudoku rules.

## Algorithm

The solver uses the A\* algorithm, which is a heuristic-based search method to find the optimal solution. The following are the key components:  

1. **State Representation:**  
   - Each state represents a partially filled Sudoku grid.  

2. **Heuristic Function:**  
   - The heuristic is the number of empty cells in the current state.  
   - Lower heuristic values are prioritized, as fewer empty cells mean the solution is closer.  

3. **Actions:**  
   - Filling an empty cell with a valid number (1 to 9) according to Sudoku rules.  

4. **Goal State:**  
   - A fully filled Sudoku grid with no violations of Sudoku rules.  

## Files

- `main.py`: Contains the implementation of the Sudoku solver.
- `README.md`: Project documentation.
- `requirements.txt`: List of dependencies (if any).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sudoku-solver.git
   cd sudoku-solver
