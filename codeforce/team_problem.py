n = int(input())  # Read the number of problems
count = 0  # Counter for problems they will solve

for _ in range(n):
    a, b, c = map(int, input().split())  # Read three values
    if a + b + c >= 2:  # If at least two friends are sure
        count += 1  # Increase counter

print(count)  # Output the result