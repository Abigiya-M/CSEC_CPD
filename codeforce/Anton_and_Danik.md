# Anton and Danik - Codeforces Solution

## Problem Statement
Anton and Danik played `n` games. Each game's result is given as a string of 'A' (Anton wins) and 'D' (Danik wins). Determine who won more games or if it's a tie.

## Input
- An integer `n` (1 ≤ n ≤ 100000) — the number of games.
- A string `s` of length `n`, consisting only of 'A' and 'D'.

## Output
- Print "Anton" if Anton won more games.
- Print "Danik" if Danik won more games.
- Print "Friendship" if they won the same number of games.

## Python Solution
```python
# Read input
n = int(input())  # Number of games
s = input()  # Game results

# Count wins
anton_wins = s.count('A')
danik_wins = s.count('D')

# Determine the winner
if anton_wins > danik_wins:
    print("Anton")
elif danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")

