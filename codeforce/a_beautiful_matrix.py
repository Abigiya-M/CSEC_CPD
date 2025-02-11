matrix = []  
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find the position of '1'
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            x, y = i, j  # Store its position (0-based indexing)

# Calculate the Manhattan distance to the center (2,2 in 0-based indexing)
moves = abs(x - 2) + abs(y - 2)

# Print the result
print(moves)