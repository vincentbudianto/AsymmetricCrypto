import math

def isPrime(num) -> bool:
    """
    Checks if said number is a prime.
    """
    if num > 1:
        for i in range(2, int(math.sqrt(num))):
            if (num % i) == 0: 
                return False
            else:
                return True
    else:
        return False