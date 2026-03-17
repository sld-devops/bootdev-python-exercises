def is_even(number):
    # return True if number is even, False otherwise
    return number % 2 == 0

def split_even_odd(numbers):
    # define empty lists for evens and odds
    even_numbers = []
    odd_numbers = []

    # loop through each number in the list
    for n in numbers:
        # classify each number and append to the appropriate list
        if is_even(n):
            even_numbers.append(n)
        else:
            odd_numbers.append(n)

    return even_numbers, odd_numbers