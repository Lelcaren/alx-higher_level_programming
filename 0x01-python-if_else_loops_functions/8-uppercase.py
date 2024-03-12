def uppercase(s):
    """Prints a string in uppercase followed by a new line."""
    for char in s:
        # Check if the character is lowercase
        if 'a' <= char <= 'z':
            # Convert the lowercase character to uppercase using ASCII manipulation
            print(chr(ord(char) - 32), end="")
        else:
            # Print the character as it is (if it's not lowercase)
            print(char, end="")
    print()  # Print a new line after printing the uppercase string

