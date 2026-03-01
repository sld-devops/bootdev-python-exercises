def is_even(number):
    """Return True if number is even, False otherwise."""
    return number % 2 == 0


def split_even_odd(numbers):
    """
    Split a list of integers into two lists (evens first, odds second)
    Preserving the original order within each group.
    """
    even_numbers = []
    odd_numbers = []

    for n in numbers:
        # Classify each number once, then append it to the appropriate list.
        if is_even(n):
            even_numbers.append(n)
        else:
            odd_numbers.append(n)

    return even_numbers, odd_numbers
