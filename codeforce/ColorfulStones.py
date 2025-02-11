def final_position(stones, instructions):
    position = 0  # Liss starts at the first stone (0-based index)

    for move in instructions:
        if position < len(stones) and stones[position] == move:
            position += 1  # Move to the next stone

    print(position + 1)  # Convert to 1-based index

# Input reading
stones = input().strip()
instructions = input().strip()

# Compute and print the result
final_position(stones, instructions)
