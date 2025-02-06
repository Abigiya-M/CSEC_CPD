a, b = map(int, input().split())  # Read input
years = 0

while a <= b:
    a *= 3  # Limak triples in weight
    b *= 2  # Bob doubles in weight
    years += 1  # Increment year counter

print(years)  # Output the number of years
