# Read inputs
n, h = map(int, input().split())
friends_heights = list(map(int, input().split()))

# Initialize total width
total_width = 0

# Calculate width based on height comparison
for height in friends_heights:
    if height > h:
        total_width += 2  # Bending down
    else:
        total_width += 1  # Walking upright

# Output the result
print(total_width)
