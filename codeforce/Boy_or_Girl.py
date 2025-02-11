def determine_gender():
    username = input().strip()  # Read input and remove unnecessary spaces
    unique_chars = set(username)  # Extract distinct characters
    if len(unique_chars) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

# Example usage:
determine_gender()
