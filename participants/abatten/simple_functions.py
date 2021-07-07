def fibonacci(max):
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)

def is_a_prime(value):

    max_quotient = math.ceil(math.sqrt(value))

    for i in range(max_quotient):
        if value % i == 0:
            return False
    return True
    


