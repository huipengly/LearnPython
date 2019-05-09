def print_max(x, y):
    # A string on the first logical line of a function is the docstring for that function.
    """Print the maximum of two numbers

    The two values musts be integers."""
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


print_max(3, 5)
print(print_max.__doc__)
help(print_max)
