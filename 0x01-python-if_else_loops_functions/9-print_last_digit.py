def print_last_digit(number):
    """Prints the last digit of a number and returns its value."""
    last_digit = abs(number) % 10  # Get the last digit using the modulus operator
    print(last_digit, end="")
    return last_digit

