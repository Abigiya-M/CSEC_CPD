n = int(input())  # Number of columns
a = list(map(int, input().split()))  # Cube counts in each column

a.sort()  # Sort the list in ascending order

print(*a)  
