# Function to check if a player has won
def check_winner(grid, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(grid[i][j] == player for j in range(3)) or all(grid[j][i] == player for j in range(3)):
            return True
    if all(grid[i][i] == player for i in range(3)) or all(grid[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to solve a single test case
def solve_test_case():
    grid = [list(input().strip()) for _ in range(3)]

    # Check if Mike, Hawk, or Selena has won
    if check_winner(grid, "X"):
        print("X")
    elif check_winner(grid, "O"):
        print("O")
    elif check_winner(grid, "+"):
        print("+")
    else:
        print("DRAW")

# Main function
def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        solve_test_case()

if __name__ == "__main__":
    main()
