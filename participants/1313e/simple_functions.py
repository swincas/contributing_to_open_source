def fibonacci(n):
    values = [0, 1]
    while values[-2] + values[-1] < n:
        values.append(values[-2] + values[-1])
    return values


def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)


# Define function that determines if a given number is a prime number
def is_prime(n):
    """
    Determines if the provided value `n` is a prime number.

    Parameters
    ----------
    n : int
        The number for which must be determined if it is a prime number.

    Returns
    -------
    is_prime : bool
        Whether or not provided `n` is a prime number.

    """

    # Check if provided n is an integer
    if not isinstance(n, int):
        # Raise ValueError if not
        raise ValueError("Input argument 'n' must be an integer!")

    # Check if n is positive
    if(n <= 0):
        # If not, raise Valueerror
        raise ValueError("Input argument 'n' must be positive!")

    # Check if n 1
    if(n == 1):
        # If so, return False
        return(False)

    # Loop over all numbers from 2 to n-1
    for i in range(2, n):
        # Check if n can be divided by this number
        if not n % i:
            # If so, return False
            return(False)
    # If for-loop finishes, it is a prime number
    else:
        return(True)
