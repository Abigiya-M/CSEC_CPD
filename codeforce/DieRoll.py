import math

# Read input
y, w = map(int, input().split())

# The highest roll Dot needs to at least tie
highest_roll = max(y, w)

# Favorable outcomes (rolling highest_roll or higher)
favorable = 6 - highest_roll + 1
total = 6

# Simplify the fraction
gcd = math.gcd(favorable, total)
print(f"{favorable // gcd}/{total // gcd}")
