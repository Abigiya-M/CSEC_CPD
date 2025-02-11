def compare_strings():
    # Read input strings and convert to lowercase
    str1 = input().strip().lower()
    str2 = input().strip().lower()

    # Compare lexicographically
    if str1 < str2:
        print(-1)
    elif str1 > str2:
        print(1)
    else:
        print(0)

# Example usage:
compare_strings()
