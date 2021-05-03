def fibonacci(max):
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1

def isprime(value):    
    print("I didn't finish this so thats why it doesn't work")
    if value == 1:
        print("Nice try, buddy. That aint prime")
    elif value == 2:
        print("Great things can come from even the littlest prime :)")
    else:
        divisor = 2
        for divisor < value:
            if value % divisor == 0:
                print("I'm so sorry to tell you that this number is not prime :(")
            else:
                divisor += 1
      
        
