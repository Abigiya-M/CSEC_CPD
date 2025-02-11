def convert_case():
    word = input().strip()  # Read input and remove unnecessary spaces
    
    # Count uppercase and lowercase letters
    upper_count = sum(1 for c in word if c.isupper())
    lower_count = len(word) - upper_count  # Remaining are lowercase

    # Apply transformation rule
    if upper_count > lower_count:
        print(word.upper())
    else:
        print(word.lower())

# Example usage:
convert_case()
