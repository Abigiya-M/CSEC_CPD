# Bear and Big Brother Problem Solution

## Problem Statement
Bear Limak wants to become the largest of bears, or at least to become larger than his brother Bob.

- Right now, Limak and Bob weigh `a` and `b` respectively.
- Limak eats a lot and his weight triples every year.
- Bob's weight doubles every year.
- We need to determine the number of years after which Limak becomes strictly heavier than Bob.

## Python Solution
```python
a, b = map(int, input().split())  # Read input
years = 0

while a <= b:
    a *= 3  # Limak triples in weight
    b *= 2  # Bob doubles in weight
    years += 1  # Increment year counter

print(years)  # Output the number of years
