# Read input
s1, s2, s3, s4 = map(int, input().split())

# Use a set to count unique colors
unique_colors = len(set([s1, s2, s3, s4]))

# The number of horseshoes to buy is 4 - unique_colors
print(4 - unique_colors)
