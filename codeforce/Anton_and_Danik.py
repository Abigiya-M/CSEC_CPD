# Read inputs
n = int(input())  # The number of games played
s = input()  # A string representing the outcomes of the games

# Count the number of wins for Anton and Danik
anton_wins = s.count('A')
danik_wins = s.count('D')

# Compare the counts and print the result
if anton_wins > danik_wins:
    print("Anton")
elif danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")
